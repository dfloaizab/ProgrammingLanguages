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
	//hilo principal: método main:
	public static void main(String args[])
	{
		
	}
}
