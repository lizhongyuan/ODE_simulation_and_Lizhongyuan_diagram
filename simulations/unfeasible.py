"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/15
"""
from typing import List, Any

from simulations.structure import _2TupleTS, _2TupleT, _2Tuple


def get_custom_ordered_wildcard_unfeasible_2tuple_TS(p_op_idx_T: tuple[Any,...],
                                                     p_wildcard_unfeasible_2tuple_TS: _2TupleTS,
                                                     p_wildcard_unfeasible_idx_T: tuple[Any,...]) -> _2TupleTS:
    """
    令
    p_wildcard_unfeasible_DI_2tuple_TS = { _2tuple_T_1, _2tuple_T_2, ..., _2tuple_T_n }
    p_wildcard_unfeasible_DI_idx_T = { i1, i2, ..., in }, 其元组代表了p_wildcard_unfeasible_DI_2tuple_TS每个集合元素的元组索引顺序
    p_op_idx_T = { idx_1, idx_2, ..., idx_n }
    获取p_op_idx_T作为元组顺序的通配的不合法DI二元组的元组的集合
    Args:
        p_op_idx_T: 一个索引元组
        p_wildcard_unfeasible_2tuple_TS: 通配的不合法DI二元组的元组的集合
        p_wildcard_unfeasible_idx_T: 通配的不合法DI二元组的元组的集合的索引元组

    Returns:
        (_2TupleTS): p_op_idx_T作为元组顺序的通配的不合法DI二元组的元组的集合
    """

    # ---------- 1 构造元组索引的转换词典 ----------

    idx_trans_dict: dict = {}
    for op_idx_pos in range(0, len(p_op_idx_T)):
        for DI_pos in range(0, len(p_wildcard_unfeasible_idx_T)):
            if p_wildcard_unfeasible_idx_T[DI_pos] == p_op_idx_T[op_idx_pos]:
                idx_trans_dict[DI_pos] = op_idx_pos

    # ---------- 2 构造p_op_idx_T作为元组顺序的通配的不合法DI二元组的元组的集合 ----------

    op_ordered_wildcard_unfeasible_DI_2tuple_TS: _2TupleTS = _2TupleTS([])
    for unfeasible_DI_2tuple_T in p_wildcard_unfeasible_2tuple_TS:

        # 2.1
        # 以表达式运算数的顺序, 将wildcard_unfeasible_DI_2tuple_T,
        # 转化为符合p_op_idx_T顺序的op_ordered_wildcard_unfeasible_DI_2tuple_T
        op_ordered_wildcard_unfeasible_DI_2tuple_list: List[_2Tuple] = []
        for DI_pos in range(0, len(p_wildcard_unfeasible_idx_T)):
            op_idx_pos: int = idx_trans_dict[DI_pos]
            wildcard_unfeasible_DI_2tuple: _2Tuple = unfeasible_DI_2tuple_T[op_idx_pos]
            op_ordered_wildcard_unfeasible_DI_2tuple_list.append(wildcard_unfeasible_DI_2tuple)

        op_ordered_unfeasible_DI_2tuple_T: _2TupleT = _2TupleT(op_ordered_wildcard_unfeasible_DI_2tuple_list)

        # 2.2
        # op_ordered_wildcard_unfeasible_DI_2tuple_T加入到op_ordered_wildcard_unfeasible_DI_2tuple_TS
        op_ordered_wildcard_unfeasible_DI_2tuple_TS.add(op_ordered_unfeasible_DI_2tuple_T)

    # ---------- 3 返回结果 ----------

    return op_ordered_wildcard_unfeasible_DI_2tuple_TS

