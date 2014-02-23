__author__ = 'yokoi-h'

from FileIO import FileIO, FileProperties

if __name__ == "__main__":

    io = FileProperties()
    io.readFromFile("file.txt")
    io.setValue("year", "2004")
    io.setValue("month", "4")
    io.setValue("day", "21")
    io.writeToFile("newFile.txt")
