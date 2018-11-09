from random import randint
from cell import Cell

##The class Gameboard is made and is supposed to simulate the life and death
#of cells as it is in the model Conway's Game of Life
class Gameboard:

    ##The constructor takes inn a desired amount of rows and columns we want
    #in the grid (consisting of cells)
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        #Initiating the grid with dead cells inside
        self._grid = []
        for i in range(self._rows):
            empty_list = []
            for j in range(self._columns):
                empty_list.append(Cell())
            self._grid.append(empty_list)
        #Setting the generationNumber to 0 initially
        self._generationNumber = 0
        ##Calling the method self.generate in order to generate both dead and
        #live cells within the grid, randomly
        self.generate()

    ##The method drawBoard prints out the grid with status sign fetched from the
    #class Cell, using fetchStatusSign.
    #The dead cells are illustrated by "." and the live cells as "O"
    def drawBoard(self):
        print("")
        for i in range(self._rows):
            for j in range(self._columns):
                print(self._grid[i][j].fetchStatusSign(),end="")
            print("")
        print("")
        #Then we have to update the grid as we just completed one generation
        self.update()

    ##The method update takes no parameters, but goes through every cell in the
    #grid and either convert a dead cell to an alive one, a cell that is alive
    #to a dead one or leaves it as it. This update all depend on the number of
    #neighboring cells that are alive, and whether or not the cell in
    #question is alive or dead
    def update(self):
        dead_become_alive = []
        alive_become_dead = []
        number_alive_neighbors = 0
        for i in range(self._rows):
            for j in range(self._columns):
                nabo = self.findNeighbor(i,j)
                ##Checking dead cells for number of neighboring cells that are
                #alive
                if self._grid[i][j].isAlive()==False:
                    for k in nabo:
                        if k.isAlive():
                            number_alive_neighbors += 1
                    if number_alive_neighbors == 3:
                        dead_become_alive.append(self._grid[i][j])
                else:
                    for k in nabo:
                    ##Checking live cells for number of neighboring cells that
                    #are alive
                        if k.isAlive():
                            number_alive_neighbors += 1
                    if number_alive_neighbors > 3:
                        alive_become_dead.append(self._grid[i][j])
                    elif number_alive_neighbors < 2:
                        alive_become_dead.append(self._grid[i][j])
                number_alive_neighbors = 0
        ##Changing the status of dead cells that are to be converted into live
        #ones
        for elem in dead_become_alive:
            elem.setAlive()
        ##Changing the status of live cells that are to be converted into live
        #ones
        for elem in alive_become_dead:
            elem.setDead()
        #Updating the generation number by one
        self._generationNumber += 1

    #This method takes no parameters, but fetches the generationNumber
    def fetchGenerationNumber(self):
        return(self._generationNumber)

    ##This method generates a grid of cells into random values of either dead or
    #alive, where the probability for alive upon generation is set to 1/3
    def generate(self):
        for i in range(self._rows):
            for j in range(self._columns):
                if randint(0,2) == 1:
                    self._grid[i][j].setAlive()
        return(self._grid)

    ##This method takes in x and y which represent rows and columns, respectively.
    #These values are coordinates in the grid and creates a list of neighbors,
    #where each neighbor is represented as a cell object.
    def findNeighbor(self, x, y):
        list_neighbors = []
        if x+1 > len(self._grid[:][0]) or y+1 > len(self._grid[0][:]):
            print("Invalid coordinates for finding neighbors!")
        else:
            for i in range(self._rows):
                for j in range(self._columns):
                    if i == x and (j == y-1 or j == y+1):
                        list_neighbors.append(self._grid[i][j])
                    elif (i == x-1 or i == x+1) and j == y:
                        list_neighbors.append(self._grid[i][j])
                    elif (i==x+1 or i==x-1) and (j==y-1 or j==y+1):
                        list_neighbors.append(self._grid[i][j])
        return(list_neighbors)

    ##This method finds the number of cells that are alive in a grid
    def findAmountAlive(self):
        count = 0
        for i in range(self._rows):
            for j in range(self._columns):
                if self._grid[i][j].isAlive():
                    count += 1
        return count
