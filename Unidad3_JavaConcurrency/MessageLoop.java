




public class MessageLoop implements Runnable {

	@Override
	public void run() {
		// TODO Auto-generated method stub
		
		String messages[] = 
			{
				"Lenguajes de Programación",
				"2022B",
				"Diego Loaiza",
				"Universidad Santiago de Cali",
				"Corte 3",
				"Concurrencia",
				"Preparación para el final",
				"Buena suerte!"
			};
		
		 try
		 {
			 for(int i = 0; i< messages.length; i++)
			 {
				 System.out.println(Thread.currentThread().getName() +">>"+ messages[i]);
				 Thread.sleep(2000);
			 }
		 }
		 catch(InterruptedException ex)
		 {
			 System.out.print("Ejecución no ha terminado aún");
		 }

	}
	
	/**
	 * This example creates a thread and waits for it to finish
	 * @param args
	 * @throws InterruptedException
	 */
	public static void main(String args[]) throws InterruptedException
	{
		long maxTime =  1000*30; //max waiting time
		
		Thread t = new Thread(new MessageLoop());
		
		//get start time:
		long startTime = System.currentTimeMillis();		
		t.start();		
		long elapsedTime = 0L;
		
		//Espera a que el hilo t termine su ejecución...
		while(t.isAlive()) //examina si el hilo aún está en ejecución
		{
			t.join(1000); //espera al hilo t, 1 segundo
			elapsedTime = System.currentTimeMillis() - startTime;
			if(elapsedTime > maxTime && t.isAlive())
			{
				System.out.println("Tired of waiting...");
				t.interrupt(); //main thread stops thread t for timeout
			}
		//
		}
		System.out.println("Finalized Job.");
	}
	
	

}
