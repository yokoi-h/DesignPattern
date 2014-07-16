__author__ = 'yokoi-h'

import sys

from TextBuilder import TextBuilder
from HTMLBuilder import HTMLBuilder
from NumberedItemBuilder import NumberedItemBuilder
from Director import Director

if __name__ == "__main__":
    opt = sys.argv[1]

    if opt == "plain":
        builder = TextBuilder()
        director = Director(builder)
        director.construct()
        result = builder.getResult()
        print result
    else:
        if opt == "html":
            builder = HTMLBuilder()
            director = Director(builder)
            director.construct()
            result = builder.getResult()
            print result,"was created."

        if opt == "number":
            builder = NumberedItemBuilder()
            director = Director(builder)
            director.construct()
            result = builder.getResult()
            print result,"was created."