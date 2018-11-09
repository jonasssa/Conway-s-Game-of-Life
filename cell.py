#Creates the class Cell. This class makes it possible to manipulate the
#state of a cell to either dead or alive.
class Cell:

    ##The constructor takes no parameters, but initiates the status of a cell as
    #dead
    def __init__(self):
        self._status = "dead"

    #This method is used to give a cell the status of dead
    def setDead(self):
        self._status = "dead"

    #This method is used to give a cell the status of alive
    def setAlive(self):
        self._status = "alive"

    ##This method takes no parameters, but checks whether a cell is alive or
    #dead
    def isAlive(self):
        if self._status == "alive":
            retur = True
        else:
            retur = False
        return retur

    ##This method checks a cell for status. If it is dead, it returns "." and
    #if it is alive, it returns "O"
    def fetchStatusSign(self):
        if self.isAlive():
            sign = "O"
        else:
            sign = "."
        return sign
