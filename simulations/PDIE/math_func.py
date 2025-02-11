"""
@brief: Brief description of the class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/2
"""

from simulations.PDIE._2Tuple_S import _2TupleS


def f_min_1_of_2tuple_S(p_2tuple_S: _2TupleS) -> object:
    """
    (定义6) Get the minimum first item of a 2TupleS instance.
    Args:
        p_2tuple_S (_2TupleSS): A 2TupleS instance

    Returns:
        (object): The minimum first item
    """
    min_first: object = None
    for item in p_2tuple_S:
        if min_first is None or min_first > item.first():
            min_first = item.first()
    return min_first


def f_max_2_of_2tuple_S(p_2tuple_S: _2TupleS) -> object:
    """
    (定义6)获取一个2TupleS instance的最大第2项
    Args:
        p_2tuple_S (_2TupleSS):

    Returns:
        (object):
    """

    max_second: object = None
    for item in p_2tuple_S:
        if max_second is None or max_second < item.second():
            max_second = item.second()
    return max_second