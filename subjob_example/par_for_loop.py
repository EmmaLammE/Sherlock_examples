import numpy as np
from concurrent import futures
from multiprocessing.dummy import Pool as ThreadPool
import time
# from numpy import random

# x = random.randint(100)

def some_function_call(inputs):
    out = np.sqrt(inputs)+inputs**(0.53)+0.198*inputs
    return out


total_err = 0.0
N = int(1e7)
inputs = np.random.randint(100, size=(N))
# print(inputs)
err = np.zeros((N))
totoal_err = 0.0

#################### Serial #########################
t = time.time()
for i in range(N):
    err[i] = some_function_call(inputs[i])
    total_err += err[i]
serial_time = time.time() - t

############### Parallel: 2 threads ###################
total_err_par2 = 0.0
pool = ThreadPool(2)
t = time.time()
for err in pool.map(some_function_call,inputs):
    total_err_par2 += err
par2_time = time.time() - t
pool.close()
pool.join()

############### Parallel: 4 threads ###################
total_err_par4 = 0.0
pool = ThreadPool(4)
t = time.time()
for err in pool.map(some_function_call,inputs):
    total_err_par4 += err
par4_time = time.time() - t
pool.close()
pool.join()

############### Parallel: 8 threads ###################
total_err_par8 = 0.0
pool = ThreadPool(8)
t = time.time()
for err in pool.map(some_function_call,inputs):
    total_err_par8 += err
par8_time = time.time() - t
pool.close()
pool.join()


print('\n------------ Correctness check --------------')
print('       serial total error  : ', total_err)
print('    2 threads total error  : ', total_err_par2)
print('    4 threads total error  : ', total_err_par4)
print('    8 threads total error  : ', total_err_par8)

print('\n------------ Performance check --------------')
print('       serial time used  : ', serial_time, ' s')
print('    2 threads time used  : ', par2_time, ' s')
print('    4 threads time used  : ', par4_time, ' s')
print('    8 threads time used  : ', par8_time, ' s')
