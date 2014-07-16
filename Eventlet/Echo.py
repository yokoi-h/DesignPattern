__author__ = 'yokoi-h'

import eventlet

def echo_handler(sock, addr):
    fd = sock.makefile()
    while True:
        print "before readline"
        line = fd.readline()
        print "after readline"
        print line
        if not line:
            break

        fd.write(line)
        fd.flush()

if __name__ == '__main__':
    server_sock = eventlet.listen(('localhost', 3001))
    eventlet.serve(server_sock, echo_handler)
