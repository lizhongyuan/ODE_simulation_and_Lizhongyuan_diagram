"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/12
"""
from typing import List

from simulations.cut2tupleS import get_largest_comm_cut_2tuple_S_from_2tuple_SS
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


def get_largest_comm_cut_2tuple_S_from_2tuple_TS(p_2tuple_TS: _2TupleTS) -> _2TupleS:

    if p_2tuple_TS.cardinality() == 0:
        return _2TupleS([])

    elem_2tuple_T_len: int = len(p_2tuple_TS[0])

    # 检查正确性
    for i in range(elem_2tuple_T_len):
        if len(p_2tuple_TS[i]) != elem_2tuple_T_len:
            raise ValueError("Wrong p_2tuple_TS !")

    _2tuple_list_list: List[List[_2Tuple]] = []
    for i in range(elem_2tuple_T_len):
        _2tuple_list_list.append([])

    # for i in range(p_2tuple_TS.cardinality()):
    #     _2tuple_T = p_2tuple_TS[i]
    #     for j in range(elem_2tuple_T_len):
    #         _2tuple_list_list[j].append(_2tuple_T[j])
    for _2tuple_T in p_2tuple_TS:
        for i in range(elem_2tuple_T_len):
            _2tuple_list_list[i].append(_2tuple_T[i])

    _2tuple_S_list: List[_2TupleS] = []
    for _2tuple_list in _2tuple_list_list:
        _2tuple_S_list.append(_2TupleS(_2tuple_list))
    _2tuple_SS: _2TupleSS = _2TupleSS(_2tuple_S_list)

    largest_comm_cut_2tuple_S: _2TupleS = get_largest_comm_cut_2tuple_S_from_2tuple_SS(_2tuple_SS)

    return largest_comm_cut_2tuple_S


