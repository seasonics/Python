import sys
import getopt
import minimax
import numpy as np
import random

def main(argv):
    # parse command line options
    opts, args = getopt.getopt(argv, "m:h:",)
    for opt, arg in opts:
        if opt in ("-m"):
            f1 = arg
    
    f = open (f1, 'r')
    #finds size of game
    gamesize = minimax.size(f)
    #parses the winpaths
    wPaths = minimax.winPaths(f)
    #populates a list of childen
    varlist = minimax.createVarList(gamesize)
    #creates the board
    minimax.Board = minimax.createBoard(gamesize)
    print(minimax.Board)
    vl = list(varlist)
    #Chooses first move from random int
    x= random.randint(0, gamesize)
    minimax.Board[x] = 'o'
    print (minimax.Board)
    #removes childen from move taken
    vl = minimax.changeVarList(minimax.Board,varlist)
    gamesize = gamesize-1
    #opponents move
    print ("Pick a space from:")
    var = int(raw_input(vl))
    minimax.Board[var] = 'x'
    print(minimax.Board)
    print ('\n')
    gamesize = gamesize-1
    vl = minimax.changeVarList(minimax.Board,varlist)

    #loops game
    while(1):
        minimax.tscore = -1000000000000000
        counter = 1
        minimax.MinMax(minimax.Board,-1000000000, 10000000000, gamesize,vl,wPaths,gamesize,counter)

        print ('\n')
        print (minimax.Board)
        if minimax.win(minimax.Board,wPaths) == 1:
            break
        vl =minimax.changeVarList(minimax.Board,varlist)
        gamesize = gamesize-1
        print ("Pick a space from:")
        var = int(raw_input(vl))
        print (var)
        minimax.Board[var] = 'x'
        print(minimax.Board)
        if minimax.win(minimax.Board,wPaths) == 1:
            break
        print ('\n')
        gamesize = gamesize-1
        vl = minimax.changeVarList(minimax.Board,varlist)

if __name__ == "__main__":
    main(sys.argv[1:])
