import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import time

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  # etc..
  ]

#################### Serial #########################
results = []
t = time.time()
for url in urls:
  result = urllib2.urlopen(url)
  results.append(result)
serial_time = time.time() - t
############### Parallel: 2 threads ###################
pool = ThreadPool(2)
t = time.time()
results = pool.map(urllib2.urlopen, urls)
par2_time = time.time() - t
pool.close()
pool.join()
############### Parallel: 4 threads ###################
pool = ThreadPool(4)
t = time.time()
results = pool.map(urllib2.urlopen, urls)
par4_time = time.time() - t
pool.close()
pool.join()
############### Parallel: 8 threads ###################
pool = ThreadPool(8)
t = time.time()
results = pool.map(urllib2.urlopen, urls)
par8_time = time.time() - t
pool.close()
pool.join()

print('\n------------ Performance check --------------')
print('       serial time used  : ', serial_time, ' s')
print('    2 threads time used  : ', par2_time, ' s')
print('    4 threads time used  : ', par4_time, ' s')
print('    8 threads time used  : ', par8_time, ' s')