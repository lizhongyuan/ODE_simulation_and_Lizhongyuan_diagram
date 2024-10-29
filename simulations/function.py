from simulations.structure import TwoT
from simulations.structure import TwoTplS

def fMin1oS(twoTplS):
    minFirst = None
    for item in twoTplS.List():
        if minFirst is None or minFirst > item.First():
            minFirst = item.First()
    return minFirst


def fMax2oS(twoTplS):
    maxSecond = None
    for item in twoTplS.List():
        if maxSecond is None or maxSecond < item.Second():
            maxSecond = item.Second()
    return maxSecond

def fCPo2tupleSS(p2tupleSS, pIdxT):
    pass
    # todo

def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
