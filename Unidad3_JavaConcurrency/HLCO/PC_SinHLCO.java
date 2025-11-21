import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class PC_SinHLCO {

    private static final int MAX_SIZE = 10;      // tamaño máximo del buffer compartido
    private static final int ITEMS_TO_PRODUCE = 30; // cuantos items se generarán en total

    private final List<Integer> buffer = new ArrayList<>(); // buffer manual
    private final AtomicInteger processed = new AtomicInteger(); // contador seguro de items procesados
    private volatile boolean done = false;   // bandera para indicar que no habrá más producción

    public static void main(String[] args) {
        new PC_SinHLCO().run();
    }

    public void run() {
        // Creamos los productores y consumidores como hilos independientes
        Thread producer1 = new Thread(new Producer(), "Producer-1");
        Thread producer2 = new Thread(new Producer(), "Producer-2");

        Thread consumer1 = new Thread(new Consumer(), "Consumer-1");
        Thread consumer2 = new Thread(new Consumer(), "Consumer-2");

        // Iniciamos los hilos
        producer1.start();
        producer2.start();
        consumer1.start();
        consumer2.start();

        try {
            // Esperamos a que ambos productores terminen
            producer1.join();
            producer2.join();

            // Cuando ya no habrán más items, activamos la bandera "done"
            done = true;

            // Avisamos a los consumidores que tal vez quedaron esperando
            synchronized (buffer) {
                buffer.notifyAll();
            }

            // Esperamos a que los consumidores terminen
            consumer1.join();
            consumer2.join();

        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Procesados: " + processed.get());
    }

    // ------------------- PRODUCTOR -------------------
    class Producer implements Runnable {
        @Override
        public void run() {
            for (int i = 0; i < ITEMS_TO_PRODUCE / 2; i++) {

                synchronized (buffer) { // bloqueamos el buffer completo
                    // Si el buffer está lleno, esperamos
                    while (buffer.size() == MAX_SIZE) {
                        try {
                            buffer.wait(); // libera el lock y queda esperando
                        } catch (InterruptedException e) { }
                    }

                    // Producir número
                    int n = (int) (Math.random() * 100);
                    buffer.add(n);

                    System.out.println(Thread.currentThread().getName() +
                            " produjo " + n);

                    // Despertamos a consumidores (u otros productores)
                    buffer.notifyAll();
                }
            }
        }
    }

    // ------------------- CONSUMIDOR -------------------
    class Consumer implements Runnable {
        @Override
        public void run() {
            while (true) {
                int value;

                synchronized (buffer) {
                    // Mientras no haya items y la producción no haya terminado
                    while (buffer.isEmpty() && !done) {
                        try {
                            buffer.wait(); // se bloquea
                        } catch (InterruptedException e) {}
                    }

                    // Si buffer vacío y done = true, no queda nada por hacer
                    if (buffer.isEmpty() && done) break;

                    // Consumir un item
                    value = buffer.remove(0);

                    // Avisar a productores que hay espacio
                    buffer.notifyAll();
                }

                System.out.println(Thread.currentThread().getName() +
                        " consumió " + value);

                processed.incrementAndGet(); // contador seguro
            }
        }
    }
}
