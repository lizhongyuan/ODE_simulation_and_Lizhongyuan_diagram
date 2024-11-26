"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/14
"""
from typing import Tuple

from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.PDIE.pdieS import PDIES, get_feasible_DI_2tuple_TS2
from simulations.TwoTupleTS import get_largest_comm_cut_2tuple_S2
from simulations.completeAscOrderFilteredSub2tupleTS import get_complete_asc_order_filtered_2tuple_TS
from simulations.domainFilteredSub2tupleTS import get_domain_filtered_sub_2tuple_TS
from simulations.function import get_bound_2tuple_S
from simulations.PDIE.pdie import PDIE, PDIE_ERROR
from simulations.structure import _2Tuple, _2TupleTS, _2TupleS


def add(p_PDIE_S: PDIES, p_op_idx_T: Tuple[int,...], p_comm_cut_2tuple: _2Tuple) -> PDIE:
    print(f"PDIES 时序加法:\n")

    res_PDIE_expression = ""
    for i in range(len(p_op_idx_T)):
        res_PDIE_expression += p_PDIE_S[p_op_idx_T[i] - 1].getExpression()
        if i < len(p_op_idx_T) - 1:
            res_PDIE_expression += ' + '

    for atom_PDIE in p_PDIE_S:
        if atom_PDIE.isError():
            pdie_error = PDIE_ERROR()
            pdie_error.setExpression(res_PDIE_expression)
            return pdie_error

    # 1 取p_atom_PDIE_S的持续区间二元组集合的集合: DI_2tuple_SS
#    DI_2tuple_SS = p_atom_PDIE_S.get_DI_2tuple_SS()

#    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合\n{str(DI_2tuple_SS)}\n")

    # 2 使用p_idx_T作为笛卡尔积表达式的运算数顺序,
    # 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,
    # 得到一个二元组的元组的集合: _2tuple_TS_CP
#    _2tuple_TS_CP = get_CP_of_2tuple_SS(DI_2tuple_SS, p_op_idx_T)

#    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合\n{str(_2tuple_TS_CP)}\n")

    # 3 取_2tuple_TS_CP的合法子集

    wildcard_unfeasible_2tuple_TS: _2TupleTS = p_PDIE_S.get_wildcard_unfeasible_DI_2tuple_TS(p_op_idx_T)

    print(f"3 取笛卡尔积的合法子集")
    CP_of_DI_2tuple_SS: _2TupleTS = p_PDIE_S.get_CP_of_DI_2tuple_SS(p_op_idx_T)
    feasible_2tuple_TS: _2TupleTS = get_feasible_DI_2tuple_TS2(wildcard_unfeasible_2tuple_TS,
                                                               CP_of_DI_2tuple_SS)
    print(f"{str(feasible_2tuple_TS)}")

    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合")
    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合")
    print(f"3 取笛卡尔积的合法子集\n{str(feasible_2tuple_TS)}\n")

    # 4 取DI_2tuple_SS的最大公共切割二元组集合: largest_comm_cut_2tuple_S
    largest_comm_cut_2tuple_S: _2TupleS = get_largest_comm_cut_2tuple_S2(feasible_2tuple_TS)
    if largest_comm_cut_2tuple_S.empty():
        pdie_error = PDIE_ERROR()
        pdie_error.setExpression(res_PDIE_expression)
        return pdie_error

    print(f"4 取DI_2tuple_SS的最大公共切割二元组集合\n{str(largest_comm_cut_2tuple_S)}\n")

    # 5
    if p_comm_cut_2tuple not in largest_comm_cut_2tuple_S:
        pdie_error = PDIE_ERROR()
        pdie_error.setExpression(res_PDIE_expression)
        return pdie_error

    TS_start: any = p_comm_cut_2tuple.first()
    TS_end: any = p_comm_cut_2tuple.second()

    domain_filtered_sub_2tuple_TS: _2TupleTS = get_domain_filtered_sub_2tuple_TS(feasible_2tuple_TS, TS_start, TS_end)
    if domain_filtered_sub_2tuple_TS.empty():
        pdie_error = PDIE_ERROR()
        pdie_error.setExpression(res_PDIE_expression)
        return pdie_error

    print(f"5 使用p_comm_cut_2tuple对feasible_2tuple_TS进行过滤\n得到一个二元组的元组的集合\n{str(domain_filtered_sub_2tuple_TS)}\n")

    # 6 todo: 论文里完善
    DI_2tuple_S: _2TupleS = get_bound_2tuple_S(domain_filtered_sub_2tuple_TS)
    print(f"6 使用domain_filtered_sub_2tuple_TS计算出结果PDIE的DI_2tuple_S\n{str(DI_2tuple_S)}\n")

    # todo: 构造DIS和metaPDIES等等，返回对应PDIE
    res_PDIE = PDIE(expression=res_PDIE_expression,
                    is_error=False,
                    is_atom=False,
                    OP='+',
                    meta_PDIES=p_PDIE_S,
                    DI_2tuple_S=DI_2tuple_S)

    return res_PDIE


def multi(p_PDIE_S: PDIES, p_op_idx_T: Tuple[int,...], ) -> PDIE:
    print(f"PDIES 时序乘法:\n")

    res_PDIE_expression: str = ""
    for i in range(len(p_op_idx_T)):
        res_PDIE_expression += p_PDIE_S[p_op_idx_T[i] - 1].getExpression()
        if i < len(p_op_idx_T) - 1:
            res_PDIE_expression += ' * '

    for atom_PDIE in p_PDIE_S:
        if atom_PDIE.isError():
            pdie_error = PDIE_ERROR()
            pdie_error.setExpression(res_PDIE_expression)
            return pdie_error

    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合")
    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合")
    CP_of_DI_2tuple_SS: _2TupleTS = p_PDIE_S.get_CP_of_DI_2tuple_SS(p_op_idx_T)

    unfeasible_2tuple_TS: _2TupleTS = p_PDIE_S.get_wildcard_unfeasible_DI_2tuple_TS(p_op_idx_T)

    print(f"3 取笛卡尔积的合法子集")
    feasible_2tuple_TS: _2TupleTS = get_feasible_DI_2tuple_TS2(unfeasible_2tuple_TS, CP_of_DI_2tuple_SS)
    print(f"{str(feasible_2tuple_TS)}")

    complete_asc_order_filtered_2tuple_TS: _2TupleTS = get_complete_asc_order_filtered_2tuple_TS(feasible_2tuple_TS)
    if complete_asc_order_filtered_2tuple_TS.empty():
        pdie_error = PDIE_ERROR()
        pdie_error.setExpression(res_PDIE_expression)
        return pdie_error

    print(f"4 使用完全正序规则对feasible_2tuple_TS进行过滤\n得到一个二元组的元组的集合\n{str(complete_asc_order_filtered_2tuple_TS)}\n")

    # 6 todo: 论文里完善
    DI_2tuple_S: _2TupleS = get_bound_2tuple_S(complete_asc_order_filtered_2tuple_TS)
    print(f"5 使用complete_asc_order_filtered_2tuple_TS计算出结果PDIE的DI_2tuple_S\n{str(DI_2tuple_S)}\n")

    # todo: 构造DIS和metaPDIES等等，返回对应PDIE
    res_PDIE = PDIE(expression=res_PDIE_expression,
                    is_error=False,
                    is_atom=False,
                    OP='*',
                    meta_PDIES=p_PDIE_S,
                    DI_2tuple_S=DI_2tuple_S)

    return res_PDIE
