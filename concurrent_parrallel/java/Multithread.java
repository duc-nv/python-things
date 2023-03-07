
class MultithreadDemo extends Thread {
    private long count;

    public MultithreadDemo(long count) {
        this.count = count;
    }
    
    public void run () {
        try {
            // System.out.println("Thread: " + Thread.currentThread().getId());
            while (this.count > 0) {
                this.count -= 1;
            }
        } catch (Exception e) {
            System.out.println("Got exception " + e);
        }
    }

}

public class Multithread {
    public static void main(String[] args) {
        long count = 1000000000;
        for (int nThreads = 1; nThreads <= 20; nThreads++) {
            long countPerThread = count / nThreads;
            Thread[] threads = new MultithreadDemo[nThreads];
            long tik0, tik1;
            tik0 = System.currentTimeMillis();
            for (int i = 0; i < nThreads; i++) {
                threads[i] = new MultithreadDemo(countPerThread);
            }
            for (int i = 0; i < nThreads; i++) {
                threads[i].start();
            }
            for (int i = 0; i < nThreads; i++) {
                try {
                    threads[i].join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            tik1 = System.currentTimeMillis();
            System.out.println("nThreads " + nThreads + ", Time taken: " + (tik1 - tik0) + " ms");

        }
    }
}
