"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/14
"""

from typing import Tuple

from simulations.PDIE.pdieS import PDIES, get_feasible_DI_2tuple_TS, f_feasible_DI_2tuple_TS
from simulations.TwoTupleTS import get_largest_comm_cut_2tuple_S_from_2tuple_TS
from simulations.completeAscOrderFilteredSub2tupleTS import get_complete_asc_order_filtered_2tuple_TS
from simulations.domainFilteredSub2tupleTS import get_domain_filtered_sub_2tuple_TS
from simulations.function import get_bound_2tuple_S
from simulations.PDIE.pdie import PDIE, PDIE_ERROR
from simulations.structure import _2Tuple, _2TupleTS, _2TupleS, _2TupleSS


def add(p_PDIE_S: PDIES, p_op_idx_T: Tuple[int,...], p_comm_cut_2tuple: _2Tuple) -> PDIE:
    print(f"PDIES 时序加法:\n")

    res_PDIE_expression = ""
    meta_PDIE_list: list[PDIE] = []

    for i in range(len(p_op_idx_T)):
        meta_PDIE_list.append(p_PDIE_S[p_op_idx_T[i] - 1])
        res_PDIE_expression += p_PDIE_S[p_op_idx_T[i] - 1].getExpression()
        if i < len(p_op_idx_T) - 1:
            res_PDIE_expression += ' + '

    for atom_PDIE in p_PDIE_S:
        if atom_PDIE.isError():
            return PDIE_ERROR(res_PDIE_expression)

    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合")
    DI_2tuple_SS: _2TupleSS = p_PDIE_S.get_DI_2tuple_SS()
    print(f"{str(DI_2tuple_SS)}\n")

    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合custom_ordered_CP_of_DI_2tuple_SS")
    custom_ordered_CP_of_DI_2tuple_SS: _2TupleTS = p_PDIE_S.get_custom_ordered_CP_of_DI_2tuple_SS(DI_2tuple_SS, p_op_idx_T)
    print(f"{str(custom_ordered_CP_of_DI_2tuple_SS)}\n")


    print(f"3 取笛卡尔积custom_ordered_CP_of_DI_2tuple_SS的合法子集custom_ordered_feasible_DI_2tuple_TS")
    custom_ordered_wildcard_unfeasible_2tuple_TS: _2TupleTS = p_PDIE_S.get_custom_ordered_wildcard_unfeasible_DI_2tuple_TS(p_op_idx_T)
    custom_ordered_feasible_DI_2tuple_TS: _2TupleTS = get_feasible_DI_2tuple_TS(custom_ordered_CP_of_DI_2tuple_SS,
                                                                                custom_ordered_wildcard_unfeasible_2tuple_TS)

    feasible_DI_2tuple_TS = f_feasible_DI_2tuple_TS(PDIE_S_1, (1, 2))

    print(f"{str(custom_ordered_feasible_DI_2tuple_TS)}\n")

    print(f"4 取custom_ordered_feasible_DI_2tuple_TS的最大公共切割二元组集合largest_comm_cut_2tuple_S, 验证过滤域是否合法")
    largest_comm_cut_2tuple_S: _2TupleS = get_largest_comm_cut_2tuple_S_from_2tuple_TS(custom_ordered_feasible_DI_2tuple_TS)
    if largest_comm_cut_2tuple_S.empty():
        return PDIE_ERROR(res_PDIE_expression)

    print(f"{str(largest_comm_cut_2tuple_S)}\n")

    if p_comm_cut_2tuple not in largest_comm_cut_2tuple_S:
        return PDIE_ERROR(res_PDIE_expression)

    print(f"5 使用p_comm_cut_2tuple对custom_ordered_feasible_DI_2tuple_TS进行过滤\n得到一个二元组的元组的集合domain_filtered_sub_DI_2tuple_TS")

    TS_start: any = p_comm_cut_2tuple.first()
    TS_end: any = p_comm_cut_2tuple.second()

    domain_filtered_sub_DI_2tuple_TS: _2TupleTS = get_domain_filtered_sub_2tuple_TS(custom_ordered_feasible_DI_2tuple_TS, TS_start, TS_end)
    if domain_filtered_sub_DI_2tuple_TS.empty():
        return PDIE_ERROR(res_PDIE_expression)

    print(f"{str(domain_filtered_sub_DI_2tuple_TS)}\n")

    # 6 todo: 论文里完善
    print(f"6 使用domain_filtered_sub_DI_2tuple_TS计算出结果PDIE的DI_2tuple_S")
    DI_2tuple_S: _2TupleS = get_bound_2tuple_S(domain_filtered_sub_DI_2tuple_TS)
    print(f"{str(DI_2tuple_S)}\n")

    # todo: 构造DIS和metaPDIES等等，返回对应PDIE, 还是需要每个参与运算的PDIE的DI
    res_PDIE = PDIE(p_expression=res_PDIE_expression,
                    p_is_error=False,
                    p_is_atom=False,
                    p_OP='+',
                    p_meta_PDIE_T=tuple(meta_PDIE_list),
                    p_meta_DI_2tuple_TS=domain_filtered_sub_DI_2tuple_TS,
                    p_DI_2tuple_S=DI_2tuple_S)

    return res_PDIE


def multi(p_PDIE_S: PDIES, p_op_idx_T: Tuple[int,...], ) -> PDIE:
    print(f"PDIES 时序乘法:\n")

    res_PDIE_expression: str = ""
    meta_PDIE_list: list[PDIE] = []

    for i in range(len(p_op_idx_T)):
        meta_PDIE_list.append(p_PDIE_S[p_op_idx_T[i] - 1])
        res_PDIE_expression += p_PDIE_S[p_op_idx_T[i] - 1].getExpression()
        if i < len(p_op_idx_T) - 1:
            res_PDIE_expression += ' * '

    for atom_PDIE in p_PDIE_S:
        if atom_PDIE.isError():
            return PDIE_ERROR(res_PDIE_expression)

    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合DI_2tuple_SS")
    DI_2tuple_SS: _2TupleSS = p_PDIE_S.get_DI_2tuple_SS()
    print(f"{str(DI_2tuple_SS)}\n")

    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合custom_ordered_CP_of_DI_2tuple_SS")
    custom_ordered_CP_of_DI_2tuple_SS: _2TupleTS = p_PDIE_S.get_custom_ordered_CP_of_DI_2tuple_SS(DI_2tuple_SS, p_op_idx_T)
    print(f"{str(custom_ordered_CP_of_DI_2tuple_SS)}\n")

    print(f"3 取笛卡尔积custom_ordered_CP_of_DI_2tuple_SS的合法子集custom_ordered_feasible_DI_2tuple_TS")
    custom_ordered_wildcard_unfeasible_DI_2tuple_TS: _2TupleTS = p_PDIE_S.get_custom_ordered_wildcard_unfeasible_DI_2tuple_TS(p_op_idx_T)
    custom_ordered_feasible_DI_2tuple_TS: _2TupleTS = get_feasible_DI_2tuple_TS(custom_ordered_CP_of_DI_2tuple_SS,
                                                                                custom_ordered_wildcard_unfeasible_DI_2tuple_TS)
    print(f"{str(custom_ordered_feasible_DI_2tuple_TS)}\n")

    print(f"4 使用完全正序规则对custom_ordered_feasible_DI_2tuple_TS进行过滤\n得到一个二元组的元组的集合complete_asc_order_filtered_DI_2tuple_TS")
    complete_asc_order_filtered_DI_2tuple_TS: _2TupleTS = get_complete_asc_order_filtered_2tuple_TS(custom_ordered_feasible_DI_2tuple_TS)
    if complete_asc_order_filtered_DI_2tuple_TS.empty():
        return PDIE_ERROR(res_PDIE_expression)

    print(f"{str(complete_asc_order_filtered_DI_2tuple_TS)}\n")

    # 6 todo: 论文里完善
    print(f"5 使用complete_asc_order_filtered_2tuple_TS计算出结果PDIE的DI_2tuple_S")
    DI_2tuple_S: _2TupleS = get_bound_2tuple_S(complete_asc_order_filtered_DI_2tuple_TS)
    print(f"{str(custom_ordered_feasible_DI_2tuple_TS)}\n")

    # todo: 构造DIS和metaPDIES等等，返回对应PDIE
    res_PDIE = PDIE(p_expression=res_PDIE_expression,
                    p_is_error=False,
                    p_is_atom=False,
                    p_OP='*',
                    p_meta_PDIE_T=tuple(meta_PDIE_list),
                    p_meta_DI_2tuple_TS=complete_asc_order_filtered_DI_2tuple_TS,
                    p_DI_2tuple_S=DI_2tuple_S)

    return res_PDIE
