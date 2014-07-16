__author__ = 'yokoi-h'

import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0,2))
    print('Task', pid, 'done')


def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous')
synchronous()

print('Asynchronous')
asynchronous()