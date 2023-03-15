import numpy as np
from numpy.linalg import norm 
# from concurrent import futures
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import time

def some_function_call(a,b,x):
    y = a*x + b + x**2 - 2*b*x + np.sqrt(x) - a
    return y


total_err = 0.0
N = int(1e5)
x = np.random.randint(100, size=(N))
y = np.zeros((N))
a = 1.0
b = 0.1

#################### Serial #########################
t = time.time()
for i in range(N):
    y[i] = some_function_call(a,b,x[i])
serial_time = time.time() - t
############### Parallel: 2 threads ###################
pool = ThreadPool(2)
t = time.time()
func = partial(some_function_call, a, b)
y2 = pool.map(func, x)
par2_time = time.time() - t
pool.close()
pool.join()
############### Parallel: 4 threads ###################
pool = ThreadPool(4)
t = time.time()
func = partial(some_function_call, a, b)
y4 = pool.map(func, x)
par4_time = time.time() - t
pool.close()
pool.join()
############### Parallel: 8 threads ###################
pool = ThreadPool(8)
t = time.time()
func = partial(some_function_call, a, b)
y8 = pool.map(func, x)
par8_time = time.time() - t
pool.close()
pool.join()


print('\n------------ Correctness check --------------')
print('       serial total error  : ', norm(y,2))
print('    2 threads total error  : ', norm(y2,2))
print('    4 threads total error  : ', norm(y4,2))
print('    8 threads total error  : ', norm(y8,2))

print('\n------------ Performance check --------------')
print('       serial time used  : ', serial_time, ' s')
print('    2 threads time used  : ', par2_time, ' s')
print('    4 threads time used  : ', par4_time, ' s')
print('    8 threads time used  : ', par8_time, ' s')
