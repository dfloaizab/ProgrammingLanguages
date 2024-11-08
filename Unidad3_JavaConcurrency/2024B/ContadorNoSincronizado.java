public class ContadorNoSincronizado {

    //recurso compartido:
    private int contador;

    //operaciones de acceso al recurso compartido:
    private synchronized void incrementar() {
        contador++;
    }

    private void decrementar() {
        contador--;
    }

    public int getContador() {
        return contador;
    }

    public static void main(String[] args) {

        ContadorNoSincronizado c = new ContadorNoSincronizado();

        Runnable tarea = () ->
        {
            for(int i = 0; i < 1000; i++) {
                c.incrementar();
                System.out.println("Ejecutando hilo con id= "+Thread.currentThread().threadId()+" ,valor del contador="+c.contador);
            }
        };

        //crear hilos que invoquen a la función de forma concurrente:
        Thread hilo1 = new Thread(tarea);
        Thread hilo2 = new Thread(tarea);

        hilo1.start();
        hilo2.start();

        //indicar al hilo main que espere a que hilo1 e hilo2 terminen su ejecución:

        try {
            hilo1.join();
            hilo2.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        System.out.println("valor final del contador:" + c.getContador());

    }

}
