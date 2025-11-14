public class ContadorConHilos {


    static int counter = 0;

    public static void main(String[] args)
    {
        final int SIM_THREADS = 4;
        final int ITERATIONS = 1000;

        System.out.println("Inicio (secuencial). Esperando resultado... ");

        Thread[] threads = new Thread[SIM_THREADS];

        for(int t = 0; t < SIM_THREADS; t++)
        {
             final int id = t;

             //2 parámetros: función a ejecutar
             threads[t] = new Thread(  
                () -> 
                {
                    for(int i = 0; i < ITERATIONS; i++)
                    {
                        counter++;
                        try {
                            Thread.sleep(1);
                        } catch (InterruptedException ex) {
                        }
                    }                    
                }, //función lambda a ejecutar por cada hilo

                "Thread id:"+t+1
             );
             System.out.printf("\ncreado hilo %s: estado %s ",threads[t].getName(), threads[t].getState());
        }


        for(int t = 0; t < SIM_THREADS; t++)
        {
            threads[t].start();
             System.out.printf("\ncreado hilo %s: estado %s, isAlive:%b ",threads[t].getName(), threads[t].getState(), threads[t].isAlive());
        }

        //interrumpimos hilo principal:
        //entra en estado TIMED_WAITING:
        // try {
        //     Thread.sleep(50); //al interrumpirse, cede el uso de la CPU a los demás hilos.
        // } catch (InterruptedException e) {
        //     // TODO Auto-generated catch block
        //     e.printStackTrace();
        // }

         // Esperar que todos los hilos terminen
        for (int i = 0; i < SIM_THREADS; i++) {
            try {
                // join hace que el hilo actual espere hasta que el hilo i termine
                threads[i].join(); //SOMETER LA EJECUCIÓN Y FINALIZACIÓN DE CADA HILO AL HILO PRINCIPAL:
                // Después de join, el hilo i tendrá estado TERMINATED
                System.out.printf("\n%s ha terminado (isAlive=%b, estado=%s)%n",
                        threads[i].getName(), threads[i].isAlive(), threads[i].getState());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

         System.out.printf("\nFinal (concurrencia SIN sincronización). Valor esperado = %d. Valor real = %d%n",
                SIM_THREADS * ITERATIONS, counter);

    }
    
}
