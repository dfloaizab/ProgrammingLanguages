public class SynchronizedCounter {
  
    //se indica que la variable puede ser afectada por varios hilos
    private volatile int c = 0;
  
    private Object lock1 = new Object();
  
    public void increment() {
            
        synchronized(lock1){
          c++;
        }
      
    }

    public synchronized void decrement() {
        c--;
    }

    public synchronized int value() {
        return c;
    }
}
