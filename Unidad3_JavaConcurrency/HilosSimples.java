public class HilosSimples {	
	
	static void hiloMensaje(String mensaje)
	{
		String nombreHilo = Thread.currentThread().getName();
		System.out.println("Hilo:"+nombreHilo+",Mensaje:"+mensaje);
	}		
	
	//clase estática para el segundo hilo del programa:
	private static class CicloMensajes implements Runnable
	{
		@Override
		public void run() {
			//cola de mensajes:
			String messages[] = {
					"Este",
					"es",
					"el",
					"curso",
					"de",
					"lenguajes",
					"de",
					"programación"
			};
			
			for(String mensaje: messages)
			{
				try {
					Thread.sleep(2000);
					hiloMensaje(mensaje);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					hiloMensaje("No he terminado!");
				}					
			}			
		}		
	}	
	/**
	 * Hilo principal del programa:
	 * @param args
	 * @throws InterruptedException 
	 */
	public static void main(String args[]) throws InterruptedException
	{
		long tiempoEspera = 1000*14;//1000*60*60; //tiempo de espera de una hora
		hiloMensaje("Arranca el hilo principal, se va a iniciar el hilo de mensajes");
		long tiempoInicio = System.currentTimeMillis();
		Thread miHilo = new Thread(new CicloMensajes());
		miHilo.start();
		hiloMensaje("Hilo iniciado, esperando que termine...");
		while(miHilo.isAlive())
		{
			hiloMensaje("Esperando que termine...");
			miHilo.join(1000);
			long tiempoActual, tiempoTranscurrido;
			tiempoActual = System.currentTimeMillis();
			tiempoTranscurrido = tiempoActual - tiempoInicio;
			if(tiempoTranscurrido > tiempoEspera && miHilo.isAlive())
			{
				hiloMensaje("Sigo esperando que termine!");
				miHilo.interrupt();
				miHilo.join();
			}			
		}
		hiloMensaje("Por fin ");		
	}
}
