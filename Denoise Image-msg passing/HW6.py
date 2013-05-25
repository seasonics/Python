import numpy as np

class node:
    def __init__(self, y ):
        self.y = float(y)
        self.msgs = []

def yArray (fl):
    f = open(fl, 'r')
    nlist = []
    sline = []
    i = 0
    for line in f:
        nlist.append([])
        sline = line.split()
        for x in sline:
            nlist[i].append(int(x))
        i = i+1
    return nlist


def createAndInit (n, ar):
    arr = [[0 for x in xrange(n)] for x in xrange(n)]
    i = 0
    j = 0
    while i < n:
        j = 0 
        while j<n:
            arr[i][j] = node(ar[i][j])
            j = j+1
        i = i+1
    return arr



def neighboors (nde, nlist):
    nodeList =[]
    i = 0
    for val in nlist:
        if nde in val:
            x=i
            y= val.index(nde)

        i=i+1
    if x+1< 100:
        nodeList.append(nlist[x+1][y])
    if x-1>=0:
        nodeList.append(nlist[x-1][y])
    if y+1< 100:
         nodeList.append(nlist[x][y+1])
    if y-1>=0:
        nodeList.append(nlist[x][y-1])
    return nodeList

def ownNode (nde, nlist):
    nodeList =[]
    i = 0
    for val in arr:
        if nde in val:
            x=i
            y= val.index(nde)

    nodeList.append(nlist[x][y])
    return nodeList

def firstMsg (nlist,n):
    i = 0
    j = 0
    nblist =[]
    for listx in nlist:
        for x in listx:
            x.msgs.append([])
    while i<n:
        print "here"
        j = 0
        while j<n:
          nblist = neighboors (nlist[i][j], nlist)
          for x in nblist:
              x.msgs[0].append([{nlist[i][j]:1},{nlist[i][j]:1}])
          j = j+1
        i = i+1

    return nlist

def passMsg (nlist, n, theta, itr):
    k=1
    theta = theta
    #start the iterations
    while k<itr:
        
        i=0
        j=0
        #mssg from y node
        for listx in nlist:
            for x in listx:
                x.msgs.append([])
                if x.y == 0:
                    x.msgs[k].append([{"y":1+theta}, {"y":1-theta}])
                else:
                    x.msgs[k].append([{"y":1-theta}, {"y":1+theta}])
        #send mssg to nb
        while i<n:
            j = 0
            print "phere"
            while j<n:
                nblist =[]
                nblist = neighboors (nlist[i][j], nlist)
                for x in nblist:
                    
                    #get zero val
                    nbdlist = []
                    nbdlist = list(nblist)
                    nbdlist.remove(x)
                    nbdlist.append("y")
                    val = float(1)
                    clist = [row[0] for row in nlist[i][j].msgs[k-1]]
                    for a in nbdlist:
                        for b in clist:
                            if a in b:
                                val = val * b[a]
                    firstVal = (1+theta) * val
                    val = float(1)
                    clist = [row[1] for row in nlist[i][j].msgs[k-1]]
                    for a in nbdlist:
                        for b in clist:
                            if a in b:
                                val = val * b[a]
                    secondVal =(1-theta) * val
                    zeroVal = firstVal + secondVal
                    #get first val
                    val = float(1)
                    clist = [row[0] for row in nlist[i][j].msgs[k-1]]
                    for a in nbdlist:
                        for b in clist:
                            if a in b:
                                val = val * b[a]
                    firstVal = (1-theta) * val
                    val = float(1)
                    clist = [row[1] for row in nlist[i][j].msgs[k-1]]
                    for a in nbdlist:
                        for b in clist:
                            if a in b:
                                val = val * b[a]
                    secondVal =(1+theta) * val
                    oneVal = firstVal + secondVal
                    x.msgs[k].append([{nlist[i][j]:(zeroVal/(zeroVal+oneVal))}, {nlist[i][j]:(oneVal/(zeroVal+oneVal))}])
                    
                j = j+1
            i = i+1
        k=k+1
    return nlist

def runAndPrint (fl):
    yarr = yArray (fl)
    arr = createAndInit(100,yarr )
    arr = firstMsg(arr, 100)
    arr = passMsg(arr, 100, .3, 3)
    f = open ('output.txt', 'w')
    i = 0
    j = 0
    while i<100:
        j = 0
        while j <100:
            zeros = [row[0] for row in arr[i][j].msgs[-1]]
            ones = [row[1] for row in arr[i][j].msgs[-1]]
            zerovals = []
            onevals = []
            z = float(1)
            o = float(1)
            for x in zeros:
                zerovals.append(x.values())
            for x in ones:
                onevals.append(x.values())
            for x in zerovals:
                z = z*x[0]
            for x in onevals:
                o = o*x[0]
            if o>z:
                f.write("1 ")
            else:
                f.write("0 ")
            j = j+1
        f.write("\n")
        i = i+1
    f.close()
        
runAndPrint('circle.1.txt')

                                           
                                    



        
    
    
    

