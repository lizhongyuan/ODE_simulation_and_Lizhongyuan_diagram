"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/12
"""
from simulations.cut2tupleS import get_largest_comm_cut_2tuple_S
from simulations.structure import _2TupleTS, _2Tuple, _2TupleS, _2TupleSS


def get_2tuple_from_2tuple_TS(p_2tuple_TS: _2TupleTS, p_idx: int, p_n: int) -> _2Tuple | None:
    """
    (定义28)从p_2tuple_TS获取索引号p_idx的元素的第n个二元组(p_idx和p_n都是从1开始计数)
    Args:
        p_2tuple_TS (_2TupleTS):
        p_idx (int):
        p_n (int):

    Returns:
        _2Tuple: 索引号p_idx的元素的第n个二元组, 如果不存在则返回None
    """

    if p_idx < 1 or p_idx > p_2tuple_TS.cardinality():
        return None

    if p_n < 1 or p_n > len(p_2tuple_TS[p_idx - 1]):
        return None

    return p_2tuple_TS[p_idx - 1][p_n - 1]


def get_largest_comm_cut_2tuple_S2(p_2tuple_TS: _2TupleTS) -> _2TupleS:

    if p_2tuple_TS.cardinality() == 0:
        return _2TupleS([])

    list_cnt = len(p_2tuple_TS[0])

    _2tuple_list_list = []
    for i in range(list_cnt):
        _2tuple_list_list.append([])

    # todo: 检查正确性

    # for _2tuple_T in p_2tuple_TS:
    #     for _2tuple in _2tuple_T:
    for i in range(p_2tuple_TS.cardinality()):
        _2tuple_T = p_2tuple_TS[i]
        for j in range(list_cnt):
            _2tuple_list_list[j].append(_2tuple_T[j])

    _2tuple_S_list = []
    for _2tuple_list in _2tuple_list_list:
        _2tuple_S_list.append(_2TupleS(_2tuple_list))

    _2tuple_SS = _2TupleSS(_2tuple_S_list)

    _2tuple_S = get_largest_comm_cut_2tuple_S(_2tuple_SS)

    return _2tuple_S
