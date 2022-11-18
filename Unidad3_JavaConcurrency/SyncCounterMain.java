


public class SyncCounterMain implements Runnable {
	
	static SynchronizedCounter mySyncCounter;

	@Override
	public void run() {
		// TODO Auto-generated method stub
		
		System.out.println(Thread.currentThread().getName());
		
		mySyncCounter.increment();
		mySyncCounter.increment();
		mySyncCounter.increment();
		mySyncCounter.decrement();
		mySyncCounter.decrement();
		mySyncCounter.decrement();
		mySyncCounter.decrement();
		mySyncCounter.decrement();		
	}
		
	public static void main(String args[])
	{
		mySyncCounter = new SyncCounter();
		
		Thread t1 = new Thread(new SyncCounterMain());
		Thread t2 = new Thread(new SyncCounterMain());		
		
	}

}
