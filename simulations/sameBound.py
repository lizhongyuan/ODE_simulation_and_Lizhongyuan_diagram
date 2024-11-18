"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/18
"""
from simulations.function import get_bound_2tuple
from simulations.structure import _2TupleTS, _2TupleTSS


def is_same_bound_2tuple_TS(_2tuple_TS: _2TupleTS) -> bool:
    """
    (定义34) 检查_2tuple_TS是否是同边界二元组的元组的集合(论文未出现)
    Args:
        _2tuple_TS (_2TupleTS): 一个二元组的元组的集合

    Returns:
        bool: 是or否
    """

    if _2tuple_TS.cardinality() < 1:
        return False

    bound_2tuple = get_bound_2tuple(_2tuple_TS[0])
    for _2tuple_T in _2tuple_TS:
        if bound_2tuple != get_bound_2tuple(_2tuple_T):
            return False

    return True


# (The set composed of _2TupleTS(sets whose elements are tuples of 2-tuple)s with distinct bound 2-tuples)
# (Get the set composed of sets of tuples of 2-tuple with distinct bound 2-tuples from a set composed of tuples of 2-tuple)
def get_distinct_same_bound_2tuple_TSS(p_2tuple_TS: _2TupleTS) -> _2TupleTSS:
    """
    (定义35) 获取二元组的元组的集合的多种相同边界的二元组的元组的集合的集合
    Args:
        p_2tuple_TS (_2TupleTS): 一个二元组的元组的集合(a set composed of tuples of 2-tuple)

    Returns:
        (_2TupleTSS):
    """

    bound_2tuple_TS_dict = {}
    for _2tuple_T in p_2tuple_TS:
        bound_2tuple = get_bound_2tuple(_2tuple_T)
        bound_2tuple_str = str(bound_2tuple)

        if not bound_2tuple_TS_dict.get(bound_2tuple_str):
            bound_2tuple_TS_dict[bound_2tuple_str] = []

        bound_2tuple_TS_dict[bound_2tuple_str].append(_2tuple_T)

    distinct_same_bound_2tuple_TS_list = []
    for key in bound_2tuple_TS_dict.keys():
        same_bound_2tuple_TS = _2TupleTS(bound_2tuple_TS_dict[key])
        distinct_same_bound_2tuple_TS_list.append(same_bound_2tuple_TS)

    return _2TupleTSS(distinct_same_bound_2tuple_TS_list)