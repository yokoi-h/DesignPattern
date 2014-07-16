__author__ = 'yokoi-h'

import eventlet

PORT = 3001
fds = []

def chat_handler(sock, addr):
    print('Participant joined chat')
    fd = sock.makefile()
    fds.append(fd)
    _loop_handler(fd)
    fds.remove(fd)
    print('Participant left chat')

def _loop_handler(fd):
    while True:
        line = fd.readline()
        print('Chat: %s' % (line.strip(),))
        if not line:
            break
        _broadcast_message(fd, line)

def _broadcast_message(pfd, msg):
    for fd in fds:
        if fd is pfd:
            continue
        fd.write(msg)
        fd.flush()

if __name__ == '__main__':
    print('Server starting up on port %d' % PORT)
    lister = eventlet.listen(('localhost', 3001))
    eventlet.serve(lister, chat_handler)
