#Importing the class Gameboard
from gameboard import Gameboard

##Making a main program that asks the user for number of rows and columns desired.
#Then the user can chose how many generations of Conway's Game of Life he or she
#wants to see
def main():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns "))
    board = Gameboard(rows, columns)
    print("The 0th generation looks like this: ")
    board.drawBoard()
    cont = input("Continue? (Yes: Type Enter - No: Type q): ")
    while cont=="":
        print("The ", board.fetchGenerationNumber(),"\'th generation looks like this: ")
        board.drawBoard()
        cont = input("Continue? (Yes: Type Enter - No: Type q): ")
main()
