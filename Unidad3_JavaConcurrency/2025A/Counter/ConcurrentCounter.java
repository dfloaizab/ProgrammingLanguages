
public class ConcurrentCounter {
	
	
	//recurso compartido:
	public static void main(String[] args)
	{
		Counter myCounter = new Counter();
		
		Thread hilo1 = new Thread(  () -> {
			//este hilo va a llamar la función incrementar de Counter, 10 veces:
			for(int i=0; i < 10; i++)
			{
				myCounter.increment();
				System.out.println("Hilo actual:"+Thread.currentThread().getId()+". Valor del contador:"+myCounter.getValue());
			}			
			
		});
		
		Thread hilo2 = new Thread(  () -> {
			for(int i=0; i < 10; i++)
			{
				myCounter.decrement();
				System.out.println("Hilo actual:"+Thread.currentThread().getId()+". Valor del contador:"+myCounter.getValue());
			}
		} 
		);
		
		//inicia la ejecución de los hilos:
		hilo1.start();
		hilo2.start();
		
		//este hilo principal va a esperar que hilo2 e hilo2 terminen su ejecución:
		try {
			hilo1.join();
			hilo2.join();
		}
		catch(InterruptedException ex)
		{
			
		}
		
		//imprimir valor final del contador:
		System.out.println("\nValor final del contador:"+myCounter.getValue());
		
		
	}

}
