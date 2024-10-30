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


# fCPo2tupleSS实现
# 2tupleSS内所有元素, 以pIdxT为顺序, 做笛卡尔积
def get_cp_of_2tupleSS(p_2tupleSS: TwoTupleSS, p_idxT: List[int]):
    sub_2tupleTS_list = get_cp_of_2tupleSS_recur(p_2tupleSS, p_idxT, 1)

    _2tupleTS_list = []
    for cur_2tupleT_list in sub_2tupleTS_list:
        cur_2tupleT = TwoTupleT(cur_2tupleT_list)
        _2tupleTS_list.append(cur_2tupleT)

    _2tupleTS = TwoTupleTS(_2tupleTS_list)

    return _2tupleTS


def get_cp_of_2tupleSS_recur(p_2tupleSS: TwoTupleSS, p_idxT: List[int], pivot: int) -> List[List[object]]:
    cur_idx = p_idxT[pivot - 1] - 1               # pivot所代表的索引
    cur_2tupleS = p_2tupleSS.List()[cur_idx]

    _2tupleTS_list = []

    if pivot == len(p_idxT):
        for cur_2tuple in cur_2tupleS.List():
            _2tupleTS_list.append([cur_2tuple])
        return _2tupleTS_list

    post_2tupleTS_list = get_cp_of_2tupleSS_recur(p_2tupleSS, p_idxT, pivot + 1)

    for cur_2tuple in cur_2tupleS.List():
        for cur_post_2tupleT in post_2tupleTS_list:
            cur_2tupleT = [ cur_2tuple ] + cur_post_2tupleT
            _2tupleTS_list.append(cur_2tupleT)

    return _2tupleTS_list


def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
