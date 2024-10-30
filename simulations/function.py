from typing import List

from simulations.structure import TwoTuple, TwoTupleSS, TwoTupleT, TwoTupleTS
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


# 2tupleSS内所有元素, 以pIdxT为顺序, 做笛卡尔积
def fCPo2tupleSS(p2tupleSS: TwoTupleSS, pIdxT: List[int]):
    resList = _fCPo2tupleSSRecur(p2tupleSS, pIdxT, 1)

    setList = []
    for item in resList:
        cur2tupleT = TwoTupleT(item)
        setList.append(cur2tupleT)

    twoTupleTS = TwoTupleTS(setList)

    return twoTupleTS


def _fCPo2tupleSSRecur(p2tupleSS: TwoTupleSS, pIdxT: List[int], start: int) -> List[List[object]]:
    curList = p2tupleSS.List()[start - 1].List()

    resList = []

    if start == len(pIdxT):
        for item in curList:
            resList.append([item])

        return resList

    postList = _fCPo2tupleSSRecur(p2tupleSS, pIdxT, start + 1)

    for item in curList:
        for postItem in postList:
            curResItem = [item] + postItem
            resList.append(curResItem)

    return resList


def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
