__author__ = 'yokoi-h'

import time
import eventlet

eventlet.monkey_patch()

from eventlet import patcher
orig_time = patcher.original('time')

def greenthread1():
    print('spawn greenthread1')
    while True:
        print('before sleep Green Thread: 1')
        time.sleep(0.1)
        print('after sleep Green Thread: 1')

def greenthread2():
    print('spawn greenthread2')
    while True:
        print('-----------------------------before sleep Green Thread: 2')
        time.sleep(5)
        print('-----------------------------after sleep Green Thread: 2')

if __name__ == '__main__':
    t1 = eventlet.spawn(greenthread1)
    t2 = eventlet.spawn(greenthread2)
    print(t1)
    t1.wait()
    # while True:
    #     print('Native Thread: 1')
    #     orig_time.sleep(1)

