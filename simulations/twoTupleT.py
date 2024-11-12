"""@package docstring
Documentation for this module.

More details.
"""

from simulations.structure import _2TupleT


def get_min_1st_of_2tuple_T(p_2tupleT: _2TupleT) -> object:
    if p_2tupleT is None:
        return None

    min_1st = p_2tupleT[0].first()
    for _2tuple in p_2tupleT:
        if min_1st > _2tuple.first():
            min_1st = _2tuple.first()
    return min_1st


def get_max_2nd_of_2tuple_T(p_2tupleT: _2TupleT) -> object:
    """
    获取一个TwoTupleT实例的所有集合元素的最大第2项

    Args:
        p_2tupleT : 一个TwoTupleT实例

    Returns:
        p_2tupleT的所有集合元素的最大第2项
    """

    if p_2tupleT is None:
        return None

    max_2nd = p_2tupleT[0].second()
    for _2tuple in p_2tupleT:
        if max_2nd < _2tuple.second():
            max_2nd = _2tuple.second()
    return max_2nd

# todo: 定义24