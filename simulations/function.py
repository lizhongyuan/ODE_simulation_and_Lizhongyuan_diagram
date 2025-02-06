from typing import List, Tuple

from simulations.PDIE._2Tuple import _2Tuple
from simulations.PDIE import _2TupleT, _2TupleS, _2TupleTS
from simulations.PDIE._2TupleS import _2TupleS




# todo: 移动到pdieOP
def get_bound_2tuple(p_2tupleT: _2TupleT) -> _2Tuple | None:
    """
    (定义28)获取长度有限的二元组的元组的边界二元组
    Args:
        p_2tupleT (_2TupleT):

    Returns:
        (_2Tuple):
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
