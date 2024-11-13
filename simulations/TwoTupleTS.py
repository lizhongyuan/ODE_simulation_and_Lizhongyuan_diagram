"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/12
"""


from simulations.structure import _2TupleTS, _2Tuple


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