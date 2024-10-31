from typing import List

from simulations.structure import TwoTuple, TwoTupleSS, TwoTupleT, TwoTupleTS
from simulations.structure import TwoTupleS

def fMin1oS(p2tupleS: TwoTupleS) -> object:
    minFirst = None
    for item in p2tupleS.list():
        if minFirst is None or minFirst > item.first():
            minFirst = item.first()
    return minFirst


def fMax2oS(p2tupleS: TwoTupleS) -> object:
    maxSecond = None
    for item in p2tupleS.list():
        if maxSecond is None or maxSecond < item.second():
            maxSecond = item.second()
    return maxSecond


# fCPo2tupleSS实现
# 2tupleSS内所有元素, 以pIdxT为顺序, 做笛卡尔积
def get_CP_of_2tupleSS(p_2tupleSS: TwoTupleSS, p_idxT: List[int]) -> TwoTupleTS:

    sub_2tupleTS_list = get_CP_of_2tupleSS_recur(p_2tupleSS, p_idxT, 1)

    _2tupleTS_list = []
    for cur_2tupleT_list in sub_2tupleTS_list:
        cur_2tupleT = TwoTupleT(cur_2tupleT_list)
        _2tupleTS_list.append(cur_2tupleT)

    _2tupleTS = TwoTupleTS(_2tupleTS_list)

    return _2tupleTS


# 递归求2tupleSS内某些元素的笛卡尔积
def get_CP_of_2tupleSS_recur(p_2tupleSS: TwoTupleSS, p_idxT: List[int], pivot: int) -> List[List[object]]:

    # cur_idx = p_idxT[pivot - 1] - 1               # pivot所代表的索引
    # cur_2tupleS = p_2tupleSS.list()[cur_idx]
    cur_idx = p_idxT[pivot - 1]               # pivot所代表的索引
    cur_2tupleS = p_2tupleSS[cur_idx]

    _2tupleTS_list = []

    if pivot == len(p_idxT):
        for cur_2tuple in cur_2tupleS.list():
                _2tupleTS_list.append([cur_2tuple])
        return _2tupleTS_list

    post_2tupleTS_list = get_CP_of_2tupleSS_recur(p_2tupleSS, p_idxT, pivot + 1)

    for cur_2tuple in cur_2tupleS.list():
        for cur_post_2tupleT in post_2tupleTS_list:
            cur_2tupleT = [ cur_2tuple ] + cur_post_2tupleT
            _2tupleTS_list.append(cur_2tupleT)

    return _2tupleTS_list


# fBound2tuple函数实现
def get_bound_2tuple(p_2tupleT: TwoTupleT) -> TwoTuple | None:

    if p_2tupleT is None:
        return None

    min_first = p_2tupleT[1].first()
    max_second = p_2tupleT[1].second()

    for item in p_2tupleT.list():
        if min_first > item.first():
            min_first = item.first()
        if max_second < item.second():
            max_second = item.second()

    return TwoTuple([min_first, max_second])


# fBound2tupleS函数实现
def get_bound_2tuple_S(p_2tupleT_S: TwoTupleTS) -> TwoTupleS | None:

    if p_2tupleT_S is None:
        return None

    bound_2tuple_S_list = []
    bound_2tuple_map = set()
    for cur_2tupleT in p_2tupleT_S.list():
        cur_bound_2tuple = get_bound_2tuple(cur_2tupleT)
        if cur_bound_2tuple.instance() not in bound_2tuple_map:
            bound_2tuple_S_list.append(TwoTuple(cur_bound_2tuple.list()))
            bound_2tuple_map.add(cur_bound_2tuple.instance())

    return TwoTupleS(bound_2tuple_S_list)

def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
