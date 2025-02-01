# cut2tupleS
# 
#
from typing import List, Any

from simulations.structure import _2Tuple
from simulations.PDIE._2TupleS import _2TupleS
from simulations.PDIE._2TupleSS import _2TupleSS
from collections import OrderedDict


# todo: add test
def Pred_in_cut_2tuple_S(p_2tuple_S: _2TupleS, p_2tuple: _2Tuple, p_A: object, p_B: object) -> bool:
    """
    (定义19)Predicate, 一个二元组是否是某二元组集合的元素, 并且在某指定切割域内
    Args:
        p_2tuple_S (_2TupleS):
        p_2tuple (_2Tuple):
        p_A:
        p_B:

    Returns:
        bool:
    """

    for _2tuple in p_2tuple_S:
        if _2tuple == p_2tuple and _2tuple.first() >= p_A and _2tuple.second() <= p_B:
            return True

    return False


def Pred_is_cut_2tuple(p_2tupleS: _2TupleS, p_2tuple: _2Tuple) -> bool:
    """
    定义19的扩展实现
    Args:
        p_2tupleS:
        p_2tuple:

    Returns:

    """
    left_match = False
    right_match = False

    for _2tuple in p_2tupleS:
        # 切割域左右边间正好等于当前二元组的第1项和第2项, 则必是切割二元组
        if _2tuple.first() == p_2tuple.first() and _2tuple.second() == p_2tuple.second():
            return True
        # 切割域的左边界等于当前二元组的首项, 右边界大于当前二元组的末项
        if _2tuple.first() == p_2tuple.first() and _2tuple.second() < p_2tuple.second():
            if right_match:
                return True
            left_match = True
        # 切割域的右边界等于当前二元组的2项, 右边界大于当前二元组的末项
        if _2tuple.second() == p_2tuple.second() and _2tuple.first() > p_2tuple.first():
            if left_match:
                return True
            right_match = True

    return False


def get_cut_2tuple_S_by_domain(p_2tuple_S: _2TupleS,
                               p_A: object,
                               p_B: object) -> _2TupleS:
    """
    (定义19)获取二元组集合在某切割域的切割集合
    Args:
        p_2tuple_S (_2TupleS):
        p_A (object):
        p_B (object):

    Returns:
        _2TupleS:
    """

    if not Pred_is_cut_2tuple(p_2tuple_S, _2Tuple([p_A, p_B])):
        return _2TupleS([])

    cut_2tuple_S = _2TupleS([])

    for _2tuple in p_2tuple_S:
        if _2tuple.first() >= p_A and _2tuple.second() <= p_B:
            cut_2tuple_S.add(_2tuple)

    return cut_2tuple_S


def get_largest_comm_cut_2tuple_S_from_2tuple_SS(p_2tuple_SS: _2TupleSS) -> _2TupleS:
    """
    (定义21)获取二元组集合的集合的最大的公共切割二元组集合
    Args:
        p_2tuple_SS (_2TupleSS):

    Returns:
        _2TupleS:
    """

    ### ---------- 1 获取所有的第一项和第二项 ----------

    first_item_list: List[Any] = []
    second_item_list: List[Any] = []

    for _2tuple_S in p_2tuple_SS:
        for _2tuple in _2tuple_S:
            first_item_list.append(_2tuple.first())
            second_item_list.append(_2tuple.second())

    first_item_list = list(OrderedDict.fromkeys(first_item_list))
    second_item_list = list(OrderedDict.fromkeys(second_item_list))

    largest_comm_cut_2tuple_S: _2TupleS = _2TupleS([])

    ### ---------- 2 所有的第一项和第二项, 构造二元组, 检查是否是切割二元组, 并添加到列表 ----------
    for first in first_item_list:
        for second in second_item_list:

            # 2.1 跳过不合法的二元组
            if first >= second:
                continue

            _2tuple = _2Tuple([first, second])

            # 2.2 跳过重复的二元组
            if _2tuple in largest_comm_cut_2tuple_S:
                continue

            # 2.3 检查_2tuple是否是p_2tuple_SS每个元素的切割二元组, 如果是则加入到集合largest_comm_cut_2tuple_S
            is_comm_cut_2tuple: bool = True
            for _2tuple_S in p_2tuple_SS:
                if not Pred_is_cut_2tuple(_2tuple_S, _2tuple):
                    is_comm_cut_2tuple = False
                    break

            if is_comm_cut_2tuple:
                largest_comm_cut_2tuple_S.add(_2tuple)

    return largest_comm_cut_2tuple_S


def get_max_comm_cut_2tuple(p_2tuple_SS: _2TupleSS) -> _2Tuple | None:
    """
    (定义22)获取二元组集合的集合的最大公共切割二元组
    Args:
        p_2tuple_SS (_2TupleSS):

    Returns:
        _2Tuple | None:
    """

    largest_comm_cut_2tuple_S = get_largest_comm_cut_2tuple_S_from_2tuple_SS(p_2tuple_SS)

    if largest_comm_cut_2tuple_S.empty():
        return None

    min_1st = largest_comm_cut_2tuple_S[0].first()
    max_2nd = largest_comm_cut_2tuple_S[0].second()

    for comm_cut_2tuple in largest_comm_cut_2tuple_S:
        if min_1st > comm_cut_2tuple.first():
            min_1st = comm_cut_2tuple.first()
        if max_2nd < comm_cut_2tuple.second():
            max_2nd = comm_cut_2tuple.second()

    max_comm_cut_2tuple = _2Tuple([min_1st, max_2nd])

    return max_comm_cut_2tuple


