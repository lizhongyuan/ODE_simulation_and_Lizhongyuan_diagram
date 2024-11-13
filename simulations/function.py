from typing import List

from simulations.structure import _2Tuple, _2TupleSS, _2TupleT, _2TupleTS
from simulations.structure import _2TupleS

# fMin1oS
def get_min_first_of_2tuple_S(p_2tuple_S: _2TupleS) -> object:
    min_first = None
    for item in p_2tuple_S:
        if min_first is None or min_first > item.first():
            min_first = item.first()
    return min_first


# fMax2oS
def get_max_second_of_2tuple_S(p_2tuple_S: _2TupleS) -> object:
    max_second = None
    for item in p_2tuple_S:
        if max_second is None or max_second < item.second():
            max_second = item.second()
    return max_second


# fCPo2tupleSS实现
# 2tupleSS内所有元素, 以pIdxT为顺序, 做笛卡尔积
def get_CP_of_2tuple_SS(p_2tupleSS: _2TupleSS, p_idxT: List[int]) -> _2TupleTS:

    sub_2tupleTS_list = get_CP_of_2tupleSS_recur(p_2tupleSS, p_idxT, 1)

    _2tupleTS_list = []
    for cur_2tupleT_list in sub_2tupleTS_list:
        cur_2tupleT = _2TupleT(cur_2tupleT_list)
        _2tupleTS_list.append(cur_2tupleT)

    _2tupleTS = _2TupleTS(_2tupleTS_list)

    return _2tupleTS


# 递归求2tupleSS内某些元素的笛卡尔积
def get_CP_of_2tupleSS_recur(p_2tupleSS: _2TupleSS,
                             p_idxT: List[int],
                             pivot: int) -> List[List[object]]:

    cur_idx = p_idxT[pivot - 1] - 1               # pivot所代表的2tupleS的索引
    cur_2tupleS = p_2tupleSS[cur_idx]

    _2tupleTS_list = []

    if pivot == len(p_idxT):
        for cur_2tuple in cur_2tupleS:
                _2tupleTS_list.append([cur_2tuple])
        return _2tupleTS_list

    post_2tupleTS_list = get_CP_of_2tupleSS_recur(p_2tupleSS, p_idxT, pivot + 1)

    for cur_2tuple in cur_2tupleS:
        for cur_post_2tupleT in post_2tupleTS_list:
            cur_2tupleT = [ cur_2tuple ] + cur_post_2tupleT
            _2tupleTS_list.append(cur_2tupleT)

    return _2tupleTS_list


# fBound2tuple函数实现
def get_bound_2tuple(p_2tupleT: _2TupleT) -> _2Tuple | None:
    """
    (定义28)获取长度有限的二元组的元组的边界二元组
    Args:
        p_2tupleT (_2TupleT):

    Returns:
        _2Tuple:
    """

    if p_2tupleT is None:
        return None

    min_first = p_2tupleT[1].first()
    max_second = p_2tupleT[1].second()

    for item in p_2tupleT.list():
        if min_first > item.first():
            min_first = item.first()
        if max_second < item.second():
            max_second = item.second()

    return _2Tuple([min_first, max_second])


# fBound2tupleS函数实现
def get_bound_2tuple_S(p_2tupleT_S: _2TupleTS) -> _2TupleS | None:

    if p_2tupleT_S is None:
        return None

    bound_2tuple_S_list = []
    bound_2tuple_map = set()
    for cur_2tupleT in p_2tupleT_S.list():
        cur_bound_2tuple = get_bound_2tuple(cur_2tupleT)
        if cur_bound_2tuple.instance() not in bound_2tuple_map:
            bound_2tuple_S_list.append(_2Tuple(cur_bound_2tuple.list()))
            bound_2tuple_map.add(cur_bound_2tuple.instance())

    return _2TupleS(bound_2tuple_S_list)


# fUnfeasibleAscMetaDI2tupleTS函数实现
def fUnfeasibleAscMetaDI2tupleTS():
    pass

def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
