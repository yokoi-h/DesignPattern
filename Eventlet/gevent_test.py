__author__ = 'yokoi-h'

import gevent

def func1():
    print('running func1')
    gevent.sleep(1)
    print('end func1')

def func2():
    print('running func2')
    gevent.sleep(2)
    print('end func2')

def func3():
    print('running func3')
    gevent.sleep(3)
    print('end func3')

if __name__ == '__main__':
    gevent.joinall([

        gevent.spawn(func1),
        gevent.spawn(func2),
        gevent.spawn(func3)

    ])

