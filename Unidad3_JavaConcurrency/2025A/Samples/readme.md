# Lenguajes de Programación, 2025A
## Unidad 3. Programación Concurrente / Sincronización de Hilos en Java

## Introducción

En el desarrollo de videojuegos, la sincronización de hilos es crucial para manejar múltiples tareas concurrentes como la renderización gráfica, la actualización de la lógica del juego, el procesamiento de entrada del usuario y la comunicación de red. Java ofrece mecanismos de sincronización intrínsecos (candados implícitos) que nos permiten coordinar estos hilos de manera segura usando `synchronized` y variables `volatile`.

---

## Ejemplo Completo: Sistema de Juego Multijugador

### Clase Principal: GameServer

```java
import java.util.ArrayList;
import java.util.List;

/**
 * Servidor de juego que maneja múltiples jugadores concurrentemente
 * Demuestra sincronización usando candados implícitos (intrínsecos) en Java
 */
public class GameServer {
    // 1. VARIABLE VOLÁTIL - Para el estado del servidor
    private volatile boolean serverRunning = true;
    
    // 2. VARIABLES PROTEGIDAS POR CANDADOS IMPLÍCITOS
    private int gameScore = 0;
    private final Object scoreLock = new Object(); // Monitor específico para el score
    
    // 3. BLOQUE SINCRONIZADO - Para proteger colecciones
    private final List<Player> players = new ArrayList<>();
    private final Object playersLock = new Object(); // Monitor específico para jugadores
    
    // 4. CONFIGURACIÓN CON SU PROPIO MONITOR
    private GameConfig config = new GameConfig();
    private final Object configLock = new Object(); // Monitor específico para configuración
    
    public static void main(String[] args) {
        GameServer server = new GameServer();
        server.startServer();
    }
    
    public void startServer() {
        System.out.println("🎮 Iniciando servidor de juego...");
        
        // Crear hilos del sistema de juego
        Thread gameLoop = new Thread(this::gameLoop, "GameLoop");
        Thread playerManager = new Thread(this::manageConnections, "PlayerManager");
        Thread configUpdater = new Thread(this::updateConfig, "ConfigUpdater");
        Thread scoreTracker = new Thread(this::trackScores, "ScoreTracker");
        
        // Iniciar hilos
        gameLoop.start();
        playerManager.start();
        configUpdater.start();
        scoreTracker.start();
        
        // Simular tiempo de ejecución
        try {
            Thread.sleep(10000); // 10 segundos
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        
        // Detener servidor
        serverRunning = false;
        System.out.println("🔴 Cerrando servidor...");
    }
    
    /**
     * MECANISMO 1: VARIABLE VOLÁTIL
     * La variable 'serverRunning' es volátil para garantizar visibilidad
     * entre hilos sin necesidad de sincronización completa
     */
    private void gameLoop() {
        int tickCount = 0;
        while (serverRunning) { // Variable volátil - lectura segura
            try {
                // Actualizar lógica del juego
                updateGameLogic();
                tickCount++;
                
                if (tickCount % 5 == 0) {
                    System.out.println("⚡ Game tick #" + tickCount);
                }
                
                Thread.sleep(500); // 2 FPS para demo
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        System.out.println("🎯 GameLoop terminado");
    }
    
    /**
     * MECANISMO 2: MÉTODOS SINCRONIZADOS
     * Estos métodos usan el monitor intrínseco del objeto (candado implícito)
     */
    private synchronized void updateGameLogic() {
        // Solo un hilo puede ejecutar métodos sincronizados a la vez
        
        // Procesar acciones de jugadores usando su propio monitor
        synchronized (playersLock) {
            for (Player player : players) {
                if (player.isActive()) {
                    player.processActions();
                    // Actualizar score basado en acciones del jugador
                    updateScore(player.getLastActionScore());
                }
            }
        }
    }
    
    /**
     * MECANISMO 3: BLOQUES SINCRONIZADOS CON MONITORES ESPECÍFICOS
     * Usar objetos específicos como monitores permite granularidad fina
     */
    private void updateScore(int points) {
        synchronized (scoreLock) { // Monitor específico para el score
            gameScore += points;
            if (gameScore > 1000) {
                System.out.println("🏆 ¡Score máximo alcanzado: " + gameScore + "!");
            }
        }
    }
    
    public int getGameScore() {
        synchronized (scoreLock) {
            return gameScore;
        }
    }
    
    public void resetScore() {
        synchronized (scoreLock) {
            gameScore = 0;
            System.out.println("🔄 Score reiniciado");
        }
    }
    
    /**
     * MECANISMO 4: SINCRONIZACIÓN DE MÚLTIPLES RECURSOS
     * Usando wait() y notify() para coordinación avanzada
     */
    private void manageConnections() {
        int connectionAttempts = 0;
        
        while (serverRunning) {
            try {
                // Simular nueva conexión de jugador
                if (connectionAttempts < 5) {
                    addPlayer("Player_" + (connectionAttempts + 1));
                    connectionAttempts++;
                }
                
                // Limpiar jugadores inactivos
                removeInactivePlayers();
                
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        System.out.println("👥 PlayerManager terminado");
    }
    
    private void addPlayer(String name) {
        Player newPlayer = new Player(name);
        
        synchronized (playersLock) {
            players.add(newPlayer);
            playersLock.notifyAll(); // Notificar a hilos esperando
            System.out.println("✅ Jugador agregado: " + name + 
                             " (Total: " + players.size() + ")");
        }
    }
    
    private void removeInactivePlayers() {
        synchronized (playersLock) {
            int initialSize = players.size();
            players.removeIf(player -> !player.isActive());
            
            if (players.size() < initialSize) {
                System.out.println("❌ Jugadores inactivos removidos. Total actual: " + players.size());
                playersLock.notifyAll(); // Notificar cambio en la lista
            }
        }
    }
    
    /**
     * MECANISMO 5: WAIT/NOTIFY PATTERN
     * Coordinación avanzada entre hilos usando monitores intrínsecos
     */
    private void trackScores() {
        while (serverRunning) {
            try {
                synchronized (playersLock) {
                    // Esperar hasta que haya al menos un jugador
                    while (players.isEmpty() && serverRunning) {
                        System.out.println("📊 ScoreTracker esperando jugadores...");
                        playersLock.wait(2000); // Esperar máximo 2 segundos
                    }
                    
                    if (!players.isEmpty()) {
                        // Mostrar estadísticas de jugadores
                        showPlayerStats();
                    }
                }
                
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        System.out.println("📊 ScoreTracker terminado");
    }
    
    private void showPlayerStats() {
        synchronized (playersLock) {
            synchronized (scoreLock) {
                System.out.println("\n📈 === ESTADÍSTICAS DEL JUEGO ===");
                System.out.println("Score total del servidor: " + gameScore);
                System.out.println("Jugadores activos: " + players.size());
                
                for (Player player : players) {
                    if (player.isActive()) {
                        System.out.println("  👤 " + player.getName() + 
                                         " - Score: " + player.getScore());
                    }
                }
                System.out.println("================================\n");
            }
        }
    }
    
    /**
     * CONFIGURACIÓN CON SINCRONIZACIÓN SEPARADA
     */
    private void updateConfig() {
        int updateCount = 0;
        
        while (serverRunning && updateCount < 3) {
            try {
                synchronized (configLock) {
                    config.setMaxPlayers(config.getMaxPlayers() + 1);
                    config.setGameMode("Mode_" + updateCount);
                    System.out.println("⚙️ Configuración actualizada: " + 
                                     config.getGameMode() + 
                                     " (Max players: " + config.getMaxPlayers() + ")");
                    updateCount++;
                }
                
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        System.out.println("⚙️ ConfigUpdater terminado");
    }
    
    public GameConfig getConfig() {
        synchronized (configLock) {
            return new GameConfig(config); // Retornar copia
        }
    }
    
    public int getPlayerCount() {
        synchronized (playersLock) {
            return players.size();
        }
    }
}

/**
 * Clase Player que representa un jugador en el juego
 */
class Player {
    private final String name;
    private volatile boolean active = true; // Variable volátil
    private int score = 0;
    private int lastActionScore = 0;
    private final Object playerLock = new Object(); // Monitor propio del jugador
    
    public Player(String name) {
        this.name = name;
    }
    
    public void processActions() {
        synchronized (playerLock) { // Cada jugador tiene su propio monitor
            // Simular procesamiento de acciones del jugador
            lastActionScore = (int)(Math.random() * 10) + 1;
            score += lastActionScore;
            
            // Simular desconexión aleatoria
            if (Math.random() < 0.08) {
                active = false;
                System.out.println("❌ " + name + " se desconectó");
            }
        }
    }
    
    public boolean isActive() {
        return active; // Lectura de variable volátil
    }
    
    public String getName() {
        return name;
    }
    
    public int getScore() {
        synchronized (playerLock) {
            return score;
        }
    }
    
    public int getLastActionScore() {
        synchronized (playerLock) {
            return lastActionScore;
        }
    }
}

/**
 * Configuración del juego con sincronización propia
 */
class GameConfig {
    private String gameMode = "Classic";
    private int maxPlayers = 10;
    
    public GameConfig() {}
    
    public GameConfig(GameConfig other) {
        this.gameMode = other.gameMode;
        this.maxPlayers = other.maxPlayers;
    }
    
    // Getters y setters - NO sincronizados aquí porque se sincronizan externamente
    public String getGameMode() { return gameMode; }
    public void setGameMode(String gameMode) { this.gameMode = gameMode; }
    public int getMaxPlayers() { return maxPlayers; }
    public void setMaxPlayers(int maxPlayers) { this.maxPlayers = maxPlayers; }
}
```

---

## Explicación de los Mecanismos de Sincronización Intrínsecos

### 1. Variables Volátiles (`volatile`)
```java
private volatile boolean serverRunning = true;
private volatile boolean active = true;
```
- **Propósito**: Garantiza visibilidad entre hilos sin sincronización completa
- **Características**: 
  - Las escrituras son inmediatamente visibles a otros hilos
  - Evita optimizaciones del compilador que podrían cachear el valor
  - No garantiza atomicidad para operaciones compuestas
- **Cuándo usar**: Para flags booleanos, contadores simples, referencias de objetos inmutables
- **En el ejemplo**: Control del estado del servidor y estado de jugadores

### 2. Métodos Sincronizados (`synchronized`)
```java
private synchronized void updateGameLogic() {
    // Solo un hilo puede ejecutar este método a la vez
}
```
- **Propósito**: Un solo hilo puede ejecutar métodos sincronizados del mismo objeto simultáneamente
- **Monitor**: Usa el monitor intrínseco del objeto (`this`)
- **Características**:
  - Bloqueo automático al entrar al método
  - Liberación automática al salir (incluso por excepción)
  - Permite reentrancia (el mismo hilo puede volver a adquirir el candado)
- **En el ejemplo**: Protege la lógica principal del juego

### 3. Bloques Sincronizados con Monitores Específicos
```java
private final Object scoreLock = new Object();

synchronized (scoreLock) {
    gameScore += points;
}
```
- **Propósito**: Sincronización más granular usando objetos específicos como monitores
- **Ventajas**:
  - Permite múltiples candados independientes en una clase
  - Reduce contención comparado con sincronizar en `this`
  - Mayor control sobre qué código se sincroniza
- **En el ejemplo**: Monitores separados para jugadores, score y configuración

### 4. Patrón Wait/Notify
```java
synchronized (playersLock) {
    while (players.isEmpty() && serverRunning) {
        playersLock.wait(2000); // Esperar condición
    }
}

// En otro hilo:
synchronized (playersLock) {
    players.add(newPlayer);
    playersLock.notifyAll(); // Despertar hilos esperando
}
```
- **Propósito**: Coordinación avanzada entre hilos
- **Métodos**:
  - `wait()`: Libera el monitor y espera notificación
  - `notify()`: Despierta un hilo en espera
  - `notifyAll()`: Despierta todos los hilos en espera
- **En el ejemplo**: ScoreTracker espera hasta que hay jugadores

### 5. Sincronización Múltiple (Orden de Candados)
```java
synchronized (playersLock) {
    synchronized (scoreLock) {
        // Acceso a ambos recursos
    }
}
```
- **Propósito**: Acceder a múltiples recursos protegidos
- **Importante**: Siempre adquirir candados en el mismo orden para evitar deadlocks
- **En el ejemplo**: Mostrar estadísticas requiere acceso a jugadores y score

## Ejercicio Preparación Examen Final: Sistema de Batalla Multijugador

Complete el siguiente código implementando candados implícitos (intrínsecos):

```java
import java.util.List;
import java.util.ArrayList;

public class BattleArena {
    // PREGUNTA 1: ¿Qué tipo de variable debe ser battleActive y por qué?
    private _______ boolean battleActive = false;
    
    private int totalDamageDealt = 0;
    private final List<Warrior> warriors = new ArrayList<>();
    
    // PREGUNTA 2: ¿Qué monitores específicos necesitamos?
    private final Object _______ = new Object(); // Para el daño total
    private final Object _______ = new Object(); // Para la lista de guerreros
    
    public static void main(String[] args) throws InterruptedException {
        BattleArena arena = new BattleArena();
        arena.startBattle();
        Thread.sleep(8000); // Esperar 8 segundos
    }
    
    // PREGUNTA 3: ¿Debe ser sincronizado este método? ¿Por qué?
    public _______ void startBattle() {
        battleActive = true;
        System.out.println("⚔️ ¡La batalla ha comenzado!");
        
        // Crear hilos de guerreros
        for (int i = 0; i < 4; i++) {
            Warrior warrior = new Warrior("Warrior_" + i, this);
            
            // PREGUNTA 4: Complete la sincronización para agregar guerreros
            _______ (_______) {
                warriors.add(warrior);
                System.out.println("🛡️ " + warrior.getName() + " se unió a la batalla");
            }
            
            new Thread(warrior::fight, "Fighter_" + i).start();
        }
        
        // Iniciar hilo observador
        new Thread(this::battleObserver, "Observer").start();
    }
    
    public void dealDamage(int damage, String attackerName) {
        // PREGUNTA 5: Implemente usando candado implícito para totalDamageDealt
        _______ (_______) {
            totalDamageDealt += damage;
            System.out.println("💥 " + attackerName + " causó " + damage + 
                             " de daño (Total: " + totalDamageDealt + ")");
            
            // Si el daño total supera 150, terminar batalla
            if (totalDamageDealt >= 150) {
                battleActive = false;
                System.out.println("🏆 ¡Batalla terminada! Daño total: " + totalDamageDealt);
                
                // Notificar a observadores
                _______.notifyAll(); // Despertar hilos esperando
            }
        }
    }
    
    /**
     * Observador que usa wait/notify pattern
     */
    private void battleObserver() {
        try {
            synchronized (damageLock) {
                while (battleActive && totalDamageDealt < 150) {
                    System.out.println("👁️ Observador esperando... (Daño actual: " + totalDamageDealt + ")");
                    damageLock.wait(3000); // Esperar máximo 3 segundos
                }
            }
            System.out.println("👁️ Observador: La batalla ha terminado!");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    
    public boolean isBattleActive() {
        return battleActive; // Variable volátil
    }
    
    public int getWarriorCount() {
        synchronized (warriorsLock) {
            return warriors.size();
        }
    }
    
    public int getTotalDamage() {
        synchronized (damageLock) {
            return totalDamageDealt;
        }
    }
}

class Warrior {
    private final String name;
    private final BattleArena arena;
    private int damageDealt = 0;
    
    public Warrior(String name, BattleArena arena) {
        this.name = name;
        this.arena = arena;
    }
    
    public void fight() {
        while (arena.isBattleActive()) {
            try {
                int damage = (int)(Math.random() * 25) + 5; // 5-30 daño
                arena.dealDamage(damage, name);
                damageDealt += damage;
                
                Thread.sleep(800 + (int)(Math.random() * 1200)); // 0.8-2.0 segundos
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        System.out.println("⚡ " + name + " terminó la batalla (Daño total: " + damageDealt + ")");
    }
    
    public String getName() {
        return name;
    }
}
```

---

## Preguntas del Ejercicio

### 1. Variables Volátiles (2 puntos)
**¿Qué tipo de variable debe ser `battleActive` y por qué?**

*Analice la necesidad de visibilidad entre hilos. ¿Es suficiente `volatile` o se necesita sincronización adicional? Justifique considerando que múltiples hilos leen esta variable pero solo uno la modifica.*

### 2. Monitores Específicos (2 puntos)
**¿Qué monitores específicos necesitamos y cómo deben llamarse?**

*Identifique los recursos que requieren protección y explique por qué usar monitores separados es mejor que sincronizar en `this`.*

### 3. Métodos Sincronizados (2 puntos)
**¿Debe ser sincronizado el método `startBattle()`? ¿Por qué?**

*Considere qué pasa si múltiples hilos intentan iniciar la batalla simultáneamente. Analice las operaciones que realiza el método.*

### 4. Bloques Sincronizados (2 puntos)
**Complete la sincronización para agregar guerreros a la lista.**

*Implemente el bloque sincronizado correcto y explique por qué ArrayList requiere sincronización externa.*

### 5. Wait/Notify Pattern (2 puntos)
**Implemente el método `dealDamage()` con candado implícito y notificación.**

*Use el monitor apropiado, implemente el patrón wait/notify correctamente y explique cuándo usar `notify()` vs `notifyAll()`.*

---

## Comparación: Candados Implícitos vs Explícitos

| Aspecto | Candados Implícitos | Candados Explícitos |
|---------|-------------------|-------------------|
| **Sintaxis** | `synchronized` | `lock.lock()` / `try-finally` |
| **Facilidad de uso** | Más simple, automático | Más código, manual |
| **Control** | Limitado | Más flexible |
| **Timeout** | No disponible | `tryLock(timeout)` |
| **Interrupciones** | No configurable | `lockInterruptibly()` |
| **Condiciones** | Solo wait/notify | Múltiples condiciones |
| **Performance** | Optimizado por JVM | Ligeramente más lento |
| **Debugging** | Menos información | Mejor instrumentación |

**Recomendación**: Use candados implícitos (`synchronized`) para la mayoría de casos. Solo use explícitos cuando necesite características avanzadas específicas.

---

## Bibliografía

1. **Oracle Java Documentation**  
   *Java Concurrency Tutorial - Intrinsic Locks and Synchronization*  
   https://docs.oracle.com/javase/tutorial/essential/concurrency/locksync.html

2. **Goetz, Brian et al.**  
   *"Java Concurrency in Practice"* - Capítulos 2-4 (Intrinsic Locks)  
   Addison-Wesley Professional, 2006  
   ISBN: 978-0321349606

3. **Oracle Java Language Specification**  
   *Chapter 17: Threads and Locks*  
   https://docs.oracle.com/javase/specs/jls/se11/html/jls-17.html

4. **Bloch, Joshua**  
   *"Effective Java"* - Items 78-84 (Concurrency)  
   3rd Edition, Addison-Wesley Professional, 2017

5. **Lea, Doug**  
   *"Concurrent Programming in Java"* - Capítulos sobre Monitors  
   Addison-Wesley Professional, 2nd Edition, 1999

6. **Java Memory Model (JSR-133)**  
   *Specification for volatile and synchronized semantics*  
   https://jcp.org/en/jsr/detail?id=133
