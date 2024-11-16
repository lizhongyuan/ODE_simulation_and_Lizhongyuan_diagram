"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/15
"""

from simulations.structure import _2TupleTS, _2TupleT


def get_feasible_DI_2tuple_TS(p_entire_DI_2tuple_TS: _2TupleTS,
                              p_unfeasible_DI_2tuple_TS: _2TupleTS,
                              p_op_idx_T: tuple,
                              p_unfeasible_DI_idx_T: tuple) -> _2TupleTS:
    """
    获取合法的持续区间元组的集合
    Args:
        p_entire_DI_2tuple_TS (_2TupleTS): 完整的持续区间元组的集合
        p_unfeasible_DI_2tuple_TS (_2TupleTS): 非法的持续区间元组的集合
        p_op_idx_T (tuple[int]): p_entire_DI_2tuple_TS对应的索引元组
        p_unfeasible_DI_idx_T (tuple[int]): p_unfeasible_DI_2tuple_TS对应的索引元组

    Returns:
        _2TupleTS: 合法的持续区间元组的集合
    """

    # 1 ---------- 检查p_op_idx_T和p_unfeasible_idx_T是否合法 ----------

    if tuple(sorted(p_op_idx_T)) != tuple(sorted(p_unfeasible_DI_idx_T)):
        raise ValueError("p_op_idx_T and p_unfeasible_DI_idx_T must have same items !")

    # 2 ---------- 构造以p_op_idx_T为索引顺序的不可能区间二元组的元组的集合 ----------

    # 2.1 构造索引转换字典(p_unfeasible_DI_idx_T每个元素在元组中的位置 ---> 它在p_op_idx_T的位置)
    idx_trans_dict = {}
    for op_pos in range(0, len(p_op_idx_T)):
        for unfeasible_DI_pos in range(0, len(p_unfeasible_DI_idx_T)):
            if p_unfeasible_DI_idx_T[unfeasible_DI_pos] == p_op_idx_T[op_pos]:
                idx_trans_dict[unfeasible_DI_pos] = op_pos

    print(str(idx_trans_dict))

    # 2.2 使用索引转换字典, 构造以p_op_idx_T为索引顺序的不可能区间二元组的元组的集合
    op_ordered_unfeasible_DI_2tuple_TS = _2TupleTS([])
    for unfeasible_DI_2tuple_T in p_unfeasible_DI_2tuple_TS:

        # 2.2.1
        # 以表达式运算数的顺序, 将当前不可能持续区间二元组unfeasible_DI_2tuple_T,
        # 转化为符合表达式运算顺序的不可能持续区间二元组op_ordered_unfeasible_DI_2tuple_T
        op_ordered_unfeasible_DI_2tuple_list = []
        for cur_pos in range(0, len(p_unfeasible_DI_idx_T)):
            op_pos = idx_trans_dict[cur_pos]
            unfeasible_DI_2tuple = unfeasible_DI_2tuple_T[op_pos]
            op_ordered_unfeasible_DI_2tuple_list.append(unfeasible_DI_2tuple)
        op_ordered_unfeasible_DI_2tuple_T = _2TupleT(op_ordered_unfeasible_DI_2tuple_list)

        # 2.2.2
        # 符合表达式运算顺序的不可能持续区间二元组, 加入到op_ordered_unfeasible_DI_2tuple_TS
        op_ordered_unfeasible_DI_2tuple_TS.add(op_ordered_unfeasible_DI_2tuple_T)

    # 3 构造合法的二元组的元组的集合
    feasible_DI_2tuple_TS = _2TupleTS([])
    for _2tuple_T in p_entire_DI_2tuple_TS:
        # 如果在op_ordered_unfeasible_DI_2tuple_TS, 则_2tuple_T非法, continue
        if _2tuple_T in op_ordered_unfeasible_DI_2tuple_TS:
            continue
        feasible_DI_2tuple_TS.add(_2tuple_T)

    # 4 返回结果

    return feasible_DI_2tuple_TS


#
# op_idx_T = (2, 1, 3)
# # unfeasible_idx_T = (2, 1, 4)
# unfeasible_idx_T = (1, 2, 3)
#
# entire_DI_2tuple_TS = _2TupleTS([])
# unfeasible_DI_2tuple_TS = _2TupleTS([])
#
# get_feasible_DI_2tuple_TS(entire_DI_2tuple_TS, unfeasible_DI_2tuple_TS, op_idx_T, unfeasible_idx_T)
