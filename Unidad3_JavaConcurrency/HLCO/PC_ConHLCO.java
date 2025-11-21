import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * LENGUAJES DE PROGRAMACIÓN 2025B
 * PROGRAMACIÓN CONCURRENTE CON HILOS
 */
public class PC_HLCO {

    private static final int MAX_SIZE = 10;            // capacidad de la cola
    private static final int ITEMS_TO_PRODUCE = 30;    // total de items
    private static final int PRODUCERS = 2;
    private static final int CONSUMERS = 2;

    // Cola bloqueante de tamaño fijo
    private final BlockingQueue<Integer> queue =
            new ArrayBlockingQueue<>(MAX_SIZE);

    private final AtomicInteger processed = new AtomicInteger(); // contador seguro

    // Permite detectar cuando ya se procesaron todos los items
    private final CountDownLatch latch = new CountDownLatch(ITEMS_TO_PRODUCE);

    public static void main(String[] args) throws InterruptedException {
        new PC_HLCO().run();
    }

    public void run() throws InterruptedException {

        // Pool de threads para productores y consumidores
        ExecutorService executor =
                Executors.newFixedThreadPool(PRODUCERS + CONSUMERS);

        // ------------------- PRODUCTORES -------------------
        for (int i = 0; i < PRODUCERS; i++) {
            executor.submit(() -> { // se ejecuta en un thread del pool
                for (int j = 0; j < ITEMS_TO_PRODUCE / PRODUCERS; j++) {
                    try {
                        int n = (int) (Math.random() * 100);

                        // put() bloquea automáticamente si la cola está llena
                        queue.put(n);

                        System.out.println(Thread.currentThread().getName() +
                                " produjo " + n);

                    } catch (InterruptedException e) {}
                }
            });
        }

        // ------------------- CONSUMIDORES -------------------
        for (int i = 0; i < CONSUMERS; i++) {
            executor.submit(() -> {
                try {
                    // Mientras falten items por procesar
                    while (latch.getCount() > 0) {

                        // take() bloquea si la cola está vacía
                        Integer val = queue.take();

                        System.out.println(Thread.currentThread().getName() +
                                " consumió " + val);

                        processed.incrementAndGet();
                        latch.countDown(); // avisamos que un item fue procesado
                    }
                } catch (InterruptedException e) {}
            });
        }

        // Espera hasta que se hayan procesado TODOS los items
        latch.await();

        // Apaga el pool de threads
        executor.shutdown();

        System.out.println("Procesados: " + processed.get());
    }
}
