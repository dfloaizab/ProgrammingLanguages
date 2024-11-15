public class VolatileCounter {

    private volatile int counter = 0;

    public void increment() {
        counter++;
    }
    public void decrement() {
        counter--;
    }

    public int getCounter() {
        return counter;
    }

    public static void main(String[] args) {
        VolatileCounter vc = new VolatileCounter();

        Thread th1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 10; i++) {
                    vc.increment();
                }
            }
        });

        Thread th2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i < 10; i++) {
                    vc.increment();
                }
            }
        });

        th1.start();
        th2.start();

        try
        {
            th1.join();
            th2.join();
        }
        catch  (InterruptedException e)
        {
            System.out.println(e);
        }
        System.out.println("Valor final del contador" + vc.getCounter());
    }

}
