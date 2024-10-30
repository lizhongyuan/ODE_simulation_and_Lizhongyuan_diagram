from typing import List

from simulations.structure import TwoTuple, TwoTupleSS
from simulations.structure import TwoTupleS

def fMin1oS(p2tupleS: TwoTupleS) -> object:
    minFirst = None
    for item in p2tupleS.List():
        if minFirst is None or minFirst > item.First():
            minFirst = item.First()
    return minFirst


def fMax2oS(p2tupleS: TwoTupleS) -> object:
    maxSecond = None
    for item in p2tupleS.List():
        if maxSecond is None or maxSecond < item.Second():
            maxSecond = item.Second()
    return maxSecond

def fCPo2tupleSS(p2tupleSS: TwoTupleSS, pIdxT: List[int]):
    pass
    # todo

def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
