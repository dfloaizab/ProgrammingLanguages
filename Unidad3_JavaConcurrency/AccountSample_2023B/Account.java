
public class Account {
	
	private float balance;
	
	
	public Account(float initialBalance)
	{
		this.balance = initialBalance;
	}
	
	/**
	 * retiro
	 * @param amount
	 */
	public void withdraw(float amount)
	{
		//validar balance >= valor a retirar
		balance -= amount;
	}
	
	/**
	 * depósito
	 * @param amount
	 */
	public void deposit(float amount)
	{
		balance += amount;
	}

}
