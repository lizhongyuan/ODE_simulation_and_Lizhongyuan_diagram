"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/15
"""

from typing import List
from simulations.structure import _2TupleTS, _2TupleT


def get_feasible_2tuple_TS(p_entire_DI_2tuple_TS: _2TupleTS,
                           p_unfeasible_DI_2tuple_TS: _2TupleTS,
                           p_op_idx_T: tuple,
                           p_unfeasible_idx_T: tuple) -> _2TupleTS:
    """
    获取合法的持续区间元组的集合
    Args:
        p_entire_DI_2tuple_TS (_2TupleTS): 完整的持续区间元组的集合
        p_unfeasible_DI_2tuple_TS (_2TupleTS): 非法的持续区间元组的集合
        p_op_idx_T (tuple[int]): p_entire_DI_2tuple_TS对应的索引元组
        p_unfeasible_idx_T (tuple[int]): p_unfeasible_DI_2tuple_TS对应的索引元组

    Returns:
        _2TupleTS: 合法的持续区间元组的集合
    """

    sorted_op_idx_T = tuple(sorted(p_op_idx_T))
    sorted_unfeasible_idx_T = tuple(sorted(p_unfeasible_idx_T))

    if sorted_op_idx_T != sorted_unfeasible_idx_T:
        raise ValueError("p_op_idx_T and p_unfeasible_idx_T must have same items !")

    # todo:
    idx_trans_dict = {}
    for op_idx in range(0, len(p_op_idx_T)):
        for idx in range(0, len(p_unfeasible_idx_T)):
            if p_unfeasible_idx_T[idx] == p_op_idx_T[op_idx]:
                idx_trans_dict[idx] = op_idx

    print(str(idx_trans_dict))

    op_order_unfeasible_DI_2tuple_TS = _2TupleTS([])
    for unfeasible_DI_2tuple_T in p_unfeasible_DI_2tuple_TS:
        op_order_unfeasible_DI_2tuple_list = []
        for idx in range(0, len(p_unfeasible_idx_T)):
            op_order_unfeasible_DI_2tuple_list.append(unfeasible_DI_2tuple_T[idx_trans_dict[idx]])
        op_order_unfeasible_DI_2tuple_TS.add(_2TupleT(op_order_unfeasible_DI_2tuple_list))

    print(op_order_unfeasible_DI_2tuple_TS)
    #
    # pass


# todo: 验证

op_idx_T = (2, 1, 3)
# unfeasible_idx_T = (2, 1, 4)
unfeasible_idx_T = (1, 2, 3)

entire_DI_2tuple_TS = _2TupleTS([])
unfeasible_DI_2tuple_TS = _2TupleTS([])

get_feasible_2tuple_TS(entire_DI_2tuple_TS, unfeasible_DI_2tuple_TS, op_idx_T, unfeasible_idx_T)
