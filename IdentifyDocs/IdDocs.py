import math
import string
from stemming.porter import stem
hamilton = ['hamilton1.txt','hamilton2.txt','hamilton3.txt','hamilton4.txt','hamilton5.txt',
             'hamilton6.txt','hamilton7.txt','hamilton8.txt','hamilton9.txt','hamilton10.txt',
             'hamilton11.txt','hamilton12.txt','hamilton13.txt','hamilton14.txt','hamilton15.txt']
madison= ['madison1.txt','madison2.txt','madison3.txt','madison4.txt','madison5.txt',
             'madison6.txt','madison7.txt','madison8.txt','madison9.txt','madison10.txt',
             'madison11.txt','madison12.txt','madison13.txt','madison14.txt','madison15.txt']
unknown = ['unknown1.txt','unknown2.txt','unknown3.txt','unknown4.txt','unknown5.txt',
           'unknown6.txt','unknown7.txt','unknown8.txt','unknown9.txt','unknown10.txt',
           'unknown11.txt',]

stopwords = ["the", "be", "to", "of",]

def docToDic (f, dic):
    f = open(f, 'r')
    splitList = []
    for line in f:
        splitList = line.split()
        for out in splitList:
            if out.lower() not in stopwords:
                var = out
                if var in dic:
                    dic[var] = dic[var] + 1
                else:
                    dic[var] = 1
    return dic
                
def MLE(dicn, dicp, pcount):
    pcount = float(pcount)
    val = sum(dicn.itervalues())
    for key in dicn:
        dicp[key] = (dicn[key] + pcount)/ ((len (dicn)*pcount) + val)
    return dicp


def MNB(ham,hval, mad,mval, unk, pcount):
    hamval = float(1)
    madval = float(1)
    pcount = float(pcount)
    for val in unk:
        if val in mad:
            madval = madval + (unk[val]*math.log(mad[val]))
            if val in ham:
                hamval = hamval + (unk[val]*math.log(ham[val]))
            else:
                hamval = hamval + (unk[val]* math.log((pcount/ ((len (ham)*pcount) + hval))))
        else:
            if val in ham:
                hamval = hamval + (unk[val]*math.log(ham[val]))
            else:
                 hamval = hamval + (unk[val]* math.log((pcount/ ((len (ham)*pcount) + hval))))
            madval = madval + (unk[val]* math.log((pcount/ ((len (mad)*pcount) + mval))))
    print hamval
    print madval
    return hamval > madval

def process (ham, mad):
    tcount = 0
    pcount = 3
    while pcount<4:
        count = 0
        i = 0
        maddicn = {}
        maddicp = {}
        for x in mad:
            maddicn = docToDic(x, maddicn)
        maddicp = MLE(maddicn, maddicp, pcount)
        while i<15:
            hamdicn = {}
            hamdicp = {}
            j = 0
            for x in ham:
               if j == i:
                   j
               else:
                   hamdicn = docToDic(x, hamdicn)
               j = j+1

            hamdicp = MLE(hamdicn, hamdicp, pcount)
            val = sum(hamdicn.itervalues())
            val2 = sum(maddicn.itervalues())
            hamNT = {}
            hamNT = docToDic(ham[i], hamNT)
            if MNB(hamdicp,val, maddicp,val2, hamNT,pcount ):
                count
            else:
                count = count+1
            i=i+1

        i = 0
        hamdicn = {}
        hamdicp = {}
        for x in ham:
            hamdicn = docToDic(x, hamdicn)
        hamdicp = MLE(hamdicn, hamdicp,pcount)
        while i<15:
            maddicn = {}
            maddicp = {}
            j = 0
            for x in mad:
               if j == i:
                   j
               else:
                   maddicn = docToDic(x, maddicn)
               j = j+1

            maddicp = MLE(maddicn, maddicp, pcount)
            val = sum(hamdicn.itervalues())
            val2 = sum(maddicn.itervalues())
            madNT = {}
            madNT = docToDic(mad[i], madNT)
            if MNB(hamdicp,val, maddicp,val2, madNT,pcount ):
                count = count+1
            i=i+1
        print count
        tcount = tcount + count
        pcount = pcount +1
    print tcount
    


def runUnknown (ham, mad, unknown):
    maddicn = {}
    maddicp = {}
    hamdicn = {}
    hamdicp = {}
    pcount = float(3)
    for x in mad:
        maddicn = docToDic(x, maddicn)
    maddicp = MLE(maddicn, maddicp, pcount)
    for x in ham:
        hamdicn = docToDic(x, hamdicn)
    hamdicp = MLE(hamdicn, hamdicp,pcount)
    val = sum(hamdicn.itervalues())
    val2 = sum(maddicn.itervalues())
    for x in unknown:
        unNT = {}
        unNT = docToDic(x, unNT)
        if MNB(hamdicp,val, maddicp,val2, unNT,pcount ):
            print "hamilton"
        else:
            print "madison"
    

runUnknown(hamilton, madison, unknown)
    
