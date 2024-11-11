"""@package docstring
Documentation for this module.

More details.
"""

from simulations.structure import TwoTupleT


def get_min_1_of_2tuple_T(p_2tupleT: TwoTupleT) -> object:
    if p_2tupleT is None:
        return None

    min_first = p_2tupleT[0].first()
    for _2tuple in p_2tupleT:
        if min_first > _2tuple.first():
            min_first = _2tuple.first()
    return min_first


def get_max_2_of_2tuple_T(p_2tupleT: TwoTupleT) -> object:
    """
    获取一个TwoTupleT实例的所有集合元素的最大第2项

    Args:
        p_2tupleT : 一个TwoTupleT实例

    Returns:
        p_2tupleT的所有集合元素的最大第2项
    """

    if p_2tupleT is None:
        return None

    max_second = p_2tupleT[0].second()
    for _2tuple in p_2tupleT:
        if max_second < _2tuple.second():
            max_second = _2tuple.second()
    return max_second

# todo: 定义24