
/**
 * MainClass can create and run multiple threads by implementing the Runnable interface
 * @author ASUS
 *
 */
public class MainClass implements Runnable {

	@Override
	/**
	 * Single thread code
	 */
	public void run() {
		// TODO Auto-generated method stub
		System.out.println("I'm running on a thread...");
		if(Thread.interrupted())
			return;
	}
	
	/**
	 * main thread code
	 * @param args
	 */
	public static void main(String args[])
	{
		Thread thread1 = new Thread(new MainClass());
		Thread thread2 = new  Thread(new MainClass());
		
		try {
		
		thread1.start();
		thread1.sleep(1000);
		
		//Interrupción del hilo principal por 5 segundos
			
		Thread.sleep(5000);
			
		thread2.start();
			
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}

}
