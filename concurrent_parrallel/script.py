import os
import threading
import multiprocessing
import time


def execution_time(func):
    def inner(*arg, **kwargs):
        tik = time.perf_counter()
        return_values = func(*arg, **kwargs)
        time_taken = time.perf_counter() - tik
        print(func.__name__, '. Time taken: ', time_taken)
        return return_values
    return inner


def count_down(counts):
    while counts > 0:
        counts -= 1


@execution_time
def normal(counts):
    count_down(counts)


@execution_time
def multithreads(counts, n_threads):
    counts_per_thread = counts // n_threads
    threads = []
    for _ in range(n_threads):
        threads.append(threading.Thread(target=count_down, args=(counts_per_thread, )))
    for t in threads:
        t.start()
    for t in threads:
        t.join()


@execution_time
def multiprocesses(counts, n_processes):
    counts_per_process = counts // n_processes
    processes = []
    for _ in range(n_processes):
        processes.append(multiprocessing.Process(target=count_down, args=(counts_per_process, )))
    for p in processes:
        p.start()
    for p in processes:
        p.join()


COUNTS = 100_000_000
normal(COUNTS)
for n_threads in [5, 10, 20]:
    print('n_threads: ', n_threads, "=============")
    multithreads(COUNTS, n_threads)
for n_processes in [1, 2, 3, 4, 5, 7, 8, 10, 20, 100]:
    print('n_processes: ', n_processes)
    multiprocesses(COUNTS, n_processes)
