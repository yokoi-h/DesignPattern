__author__ = 'yokoi-h'

class Triple(object):

    __ins = []

    def __new__(cls, *args, **kwargs):
        if len(cls.__ins) == 0:
            ins = super(Triple, cls).__new__(cls,  *args, **kwargs)
            cls.__ins.append(ins)
            ins = super(Triple, cls).__new__(cls,  *args, **kwargs)
            cls.__ins.append(ins)
            ins = super(Triple, cls).__new__(cls,  *args, **kwargs)
            cls.__ins.append(ins)
        return cls.__ins

    @classmethod
    def getInstance(cls, index):
        return cls.__ins[index]

Triple()
