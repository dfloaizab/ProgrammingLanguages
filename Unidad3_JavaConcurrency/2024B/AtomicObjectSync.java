import java.util.concurrent.atomic.AtomicInteger;

public class AtomicObjectSync {

    private AtomicInteger contador = new AtomicInteger(0);

    public void increment() {
        this.contador.incrementAndGet();
    }
    public void decrement() {
        this.contador.decrementAndGet();
    }
    public int getCounter()
    {
        return this.contador.get();
    }
    public static void main(String[] args) {

        //se crear una instancia de la clase con el recurso compartido al que se le ha defini
        //definido un acceso atómico
        AtomicObjectSync atomicCounter = new AtomicObjectSync();

        //se crean hilos que van a acceder de forma concurrente al contador:
        Thread th1 = new Thread(atomicCounter::increment);
        Thread th2 = new Thread(atomicCounter::decrement);

        //se inician los hilos:
        th1.start();
        th2.start();

        //se obliga al hilo main a que espere a los hilos:
        try
        {
            th1.join();
            th2.join();
        }
        catch(InterruptedException ex)
        {
            System.out.println(ex.getMessage());
        }
        System.out.println("Valor del contador: "+atomicCounter.getCounter());
    }
}
