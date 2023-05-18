
public class MainThread {
	
	
	/**
	 * main thread
	 * @param args
	 */
	public static void main(String args[])
	{	
		
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
				System.out.println(mensaje);	
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
					
		}		
		
		
	}

}
