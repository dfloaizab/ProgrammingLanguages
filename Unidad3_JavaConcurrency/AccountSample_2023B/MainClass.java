
public class MainClass extends Thread{
	
	//método que se ejecuta por cada instancia del hilo
	public void run()
	{
		System.out.println("Ejecutando hilo"+Thread.currentThread().getId());
	}
	
	
	public static void main(String[] args)
	{
		Account myAccount = new Account(250000);
		
		//1. crear 2 hilos para las dos operaciones 
		// CONCURRENTES sobre la cuenta:
		Thread hiloRetiro = new Thread( ()-> myAccount.withdraw(200000)  );
		//Thread hiloDeposito = new Thread ( () -> myAccount.deposit(50000));
		
		//Crear un arreglo de hilos que invocan el mismo método:
		Thread[] hilosRetiro = new Thread[8];
		
		for(int i = 0; i < hilosRetiro.length; i++)
		{
			hilosRetiro[i] = new Thread(  () -> myAccount.withdraw(100000)   );
			hilosRetiro[i].start();
		}
		
		//2 Iniciar los hilos:
		//hiloRetiro.start();
		//hiloDeposito.start();
		
		//3. Unir los hilos a este hilo principal (main)
		//e imprimir el id de cada hilo:
		try {
			
			//hiloDeposito.join();
			//hiloRetiro.join();
			
			//inicializar el arreglo de hilos de retiro:
			for(Thread t: hilosRetiro)
			{
				t.join();
				System.out.println("Hilo con id: "+t.getId());
			}				
			
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		//de aquí en adelante, se espera que ambos hilos terminen
		//gracias a que llamé la función join en cada uno de ellos		
		System.out.println("Balance final:"+myAccount.getBalance());		
		
		//operaciones secuenciales en el hilo principal:		
		//myAccount.deposit(500000);
		//myAccount.withdraw(40000);
	}

}
