__author__ = 'yokoi-h'

from TicketMaker import TicketMaker as ti

if __name__ == "__main__":
    ti_ins = ti.getInstance()
    print ti_ins.getNextTicketNumber()
    print ti_ins.getNextTicketNumber()
    print ti_ins.getNextTicketNumber()