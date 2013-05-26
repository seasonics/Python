from __future__ import print_function
import numpy as np
import random

#finds size from first line
def size (f):
    for line in f:
        return int(line)
    
#parse winning paths
def winPaths(f):
    winningPaths = []
    for line in f:
        path = set()
        plist = line.split()
        for x in plist:
            path.add(int(x))
        winningPaths.append(path)
    return winningPaths

#creates the children list
def createVarList(length):
    seq = range(length)
    return seq

#creates initial game board of all zeros
def createBoard(length):
    brd = []
    i = 0
    while i<length:
        brd.append(0)
        i = i+1
    return brd
        

def isEven(number):
        return number % 2 == 0
    
#checks if the path is in the winninglist
def scorep (path, wplist):
    for x in wplist:
        if ((x & path) == x):
            return 1
    return 0

#removes children from children list
def changeVarList(brd, vlist):
    count = 0
    vlistc = list(vlist)
    for x in brd:
        if x != 0:
            vlistc.remove(count)
        count = count+1

    return vlistc

def MinMax (brd,alpha,beta, depth, varlist, wPaths,gamesize,counter):
    global tscore
    global Board
    #chooses which player it is
    if isEven (counter):
        icon = 'x'
    else:
        icon = 'o'
        
    #checks if terminal node or depth 0
    score = set()
    score1 = set()
    count = 1
    for x in brd:
        if x ==('o'):
             score.add(count)
        if x ==('x'):
             score1.add(count)
        count = count + 1
    if scorep(score,wPaths) == 1:
            return 1
    if scorep(score1,wPaths) == 1:
            return -1
    if depth <= 0:
        return 0
    #implements alpha-beta pruning and minimax
    #for computer play
    if icon ==  'o':
        for x in varlist:
            brd2 = list(brd)
            brd2[x] = icon
            car2 = list(varlist)
            car2.remove(x)       
            alpha = max(alpha, MinMax(brd2,alpha,beta, depth-1, car2, wPaths,gamesize,counter = counter +1))
            if beta <= alpha:
                break
            if depth  == gamesize:
                if alpha >= tscore:
                    tscore = alpha
                    Board = list(brd2)
                alpha = -1000000000000
        return alpha
    #implements alpha-beta pruning and minimax
    #for human player
    if icon == 'x':
         for x in varlist:
            brd2 = list(brd)
            brd2[x] = icon
            car2 = list(varlist)
            car2.remove(x)  
            beta = min(beta, MinMax(brd2,alpha,beta, depth-1, car2, wPaths,gamesize,counter = counter +1))
            if beta <= alpha:
                break
         return beta

#checks win
def win (brd, wPaths):
    score = set()
    score1 = set()
    count = 1
    for x in brd:
        if x ==('o'):
             score.add(count)
        if x ==('x'):
             score1.add(count)
        count = count + 1
    if scorep(score,wPaths) == 1:
            print ("computer wins")
            return 1
    if scorep(score1,wPaths) == 1:
            print ("player wins")
            return 1
    return 0

