from typing import List, Tuple

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
def get_custom_ordered_CP_of_2tuple_SS(p_2tuple_SS: _2TupleSS, p_idx_T: Tuple[int,...]) -> _2TupleTS:
    """
    (定义16)Let set p_2tuple_SS = { p_2tuple_S_1, p_2tuple_S_2, p_2tuple_S_3, ... , p_2tuple_S_n },
    and p_idx_T = [ p_idx_1, p_idx_2, p_idx_3, ..., p_idx_n ].
    get cartesian product with expression p_2tuple_S_(p_idx_1) * p_2tuple_S_(p_idx_2) * p_2tuple_S_(p_idx_3) * ... * p_2tuple_S_(p_idx_n)
    Args:
        p_2tuple_SS (_2TupleSS): A set whose elements are sets of 2-tuples
        p_idx_T (Tuple[int,...]): A tuple representing the index order of operands

    Returns:
        (_2TupleTS): cartesian product
    """

    _2tuple_list_list = get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS, p_idx_T, 1)

    _2tuple_T_list = []
    for _2tuple_list in _2tuple_list_list:
        _2tuple_T = _2TupleT(_2tuple_list)
        _2tuple_T_list.append(_2tuple_T)

    _2tuple_TS = _2TupleTS(_2tuple_T_list)

    return _2tuple_TS


# 递归求2tupleSS内某些元素的笛卡尔积, todo: 全面改造
def get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS: _2TupleSS,
                                             p_idx_T: Tuple[int,...],
                                             p_pivot: int) -> List[List[_2Tuple]]:

    cur_idx = p_idx_T[p_pivot - 1] - 1               # pivot所代表的2tupleS的索引
    cur_2tuple_S = p_2tuple_SS[cur_idx]

    _2tuple_list_list = []

    if p_pivot == len(p_idx_T):
        for _2tuple in cur_2tuple_S:
                _2tuple_list_list.append([ _2tuple ])
        return _2tuple_list_list

    post_2tupleT_list_list = get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS, p_idx_T, p_pivot + 1)

    for _2tuple in cur_2tuple_S:
        for post_2tuple_list in post_2tupleT_list_list:
            _2tuple_list = [ _2tuple ] + post_2tuple_list
            _2tuple_list_list.append(_2tuple_list)

    return _2tuple_list_list


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

    min_first = p_2tupleT[0].first()
    max_second = p_2tupleT[0].second()

    for item in p_2tupleT.list():
        if min_first > item.first():
            min_first = item.first()
        if max_second < item.second():
            max_second = item.second()

    return _2Tuple([min_first, max_second])


def get_bound_2tuple_S(p_2tupleT_S: _2TupleTS) -> _2TupleS | None:
    """
    获取二元组的元组的集合p_2tupleT_S的边界二元组集合
    Args:
        p_2tupleT_S (_2TupleTS): 二元组的元组的集合

    Returns:
        (_2TupleS) p_2tupleT_S的边界二元组集合
    """

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
