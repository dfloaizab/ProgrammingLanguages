
/**
 * Esta clase representa el recurso compartido:
 * @author loaiza
 *
 */
public class Counter {
	
	private int value=0;
	
	public void increment()
	{
		value++;
	}
	
	public void decrement()
	{
		value--;
	}
	
	public int getValue()
	{
		return this.value;
	}

}
