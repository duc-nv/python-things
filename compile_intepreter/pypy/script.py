import time


start = time.perf_counter()
total = 0
n = 10000
for i in range(n):
    for j in range(n):
        total += i + j
print('Result ', total)
print('Time taken: ', time.perf_counter() - start)