public class ContadorSecuencial
{


    static int counter = 0;

    public static void main(String[] args)
    {
        final int SIM_THREADS = 4;
        final int ITERATIONS = 10000;


        System.out.println("Inicio (secuencial). Esperando resultado... ");


        for(int t = 0; t < SIM_THREADS; t++)
        {
            for(int i = 0; i < ITERATIONS; i++)
            {
                counter++; //ESTA OPERACIÓN ES ATÓMICA EN ESTE CONTEXTO SECUENCIAL
            }
        }

        //Mostrar en console:
        System.out.printf("Hilos ejecutados: %d, Iteraciones por cada hilo: %d, Valor final de counter: %d",SIM_THREADS,ITERATIONS,counter);

    }


}
