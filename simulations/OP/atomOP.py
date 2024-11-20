"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/14
"""
from typing import List, Tuple

from simulations.cut2tupleS import get_largest_comm_cut_2tuple_S
from simulations.domainFilteredSub2tupleTS import get_domain_filtered_sub_2tuple_TS
from simulations.function import get_CP_of_2tuple_SS, get_bound_2tuple_S
from simulations.pdie import PDIES, AtomPDIES, PDIE, PDIE_ERROR
from simulations.structure import _2Tuple, _2TupleTS
from simulations.unfeasible import get_feasible_DI_2tuple_TS


# todo:
def atom_add(p_atom_PDIE_S: AtomPDIES,
             p_op_idx_T: Tuple[int,...],
             p_comm_cut_2tuple: _2Tuple,
             p_unfeasible_DI_2tuple_TS_dict: dict) -> PDIE | None:
    print(f"AtomPDIES 时序加法:\n\n")

    for atom_PDIE in p_atom_PDIE_S:
        if atom_PDIE.isError():
            return PDIE_ERROR()

    # 1 取p_atom_PDIE_S的持续区间二元组集合的集合: DI_2tuple_SS
    DI_2tuple_SS = p_atom_PDIE_S.get_DI_2tuple_SS()

    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合\n{str(DI_2tuple_SS)}\n")

    # 2 使用p_idx_T作为笛卡尔积表达式的运算数顺序,
    # 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,
    # 得到一个二元组的元组的集合: _2tuple_TS_CP
    _2tuple_TS_CP = get_CP_of_2tuple_SS(DI_2tuple_SS, p_op_idx_T)

    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合\n{str(_2tuple_TS_CP)}\n")

    # 3 取_2tuple_TS_CP的合法子集

    unfeasible_PDIE_T = p_unfeasible_DI_2tuple_TS_dict['PDIE_tuple']
    idx_T_asc_list = []
    if unfeasible_PDIE_T is not None and unfeasible_PDIE_T != ():
        for pdie in unfeasible_PDIE_T:
            cur_idx = p_atom_PDIE_S.index(pdie)
            if cur_idx is None:
                raise ValueError(f"p_atom_PDIE_S 中没有元素{pdie}")
            if cur_idx in idx_T_asc_list:
                return PDIE_ERROR()

            idx_T_asc_list.append(cur_idx)

    feasible_2tuple_TS = get_feasible_DI_2tuple_TS(_2tuple_TS_CP,
                                                   p_unfeasible_DI_2tuple_TS_dict['_2tuple_TS'],
                                                   p_op_idx_T,
                                                   tuple(idx_T_asc_list))


    print(f"3 取_2tuple_TS_CP的合法子集\n{str(feasible_2tuple_TS)}\n")

    # 4 取DI_2tuple_SS的最大公共切割二元组集合: largest_comm_cut_2tuple_S
    largest_comm_cut_2tuple_S = get_largest_comm_cut_2tuple_S(DI_2tuple_SS)
    if largest_comm_cut_2tuple_S.empty():
        return PDIE_ERROR()

    print(f"4 取DI_2tuple_SS的最大公共切割二元组集合\n{str(largest_comm_cut_2tuple_S)}\n")

    # 5
    if p_comm_cut_2tuple not in largest_comm_cut_2tuple_S:
        return PDIE_ERROR()

    TS_start = p_comm_cut_2tuple.first()
    TS_end = p_comm_cut_2tuple.second()

    domain_filtered_sub_2tuple_TS = get_domain_filtered_sub_2tuple_TS(feasible_2tuple_TS, TS_start, TS_end)
    if domain_filtered_sub_2tuple_TS.empty():
        return PDIE_ERROR()

    print(f"5 {str(domain_filtered_sub_2tuple_TS)}")

    # 6 todo: 论文里完善
    DI_2tuple_S = get_bound_2tuple_S(domain_filtered_sub_2tuple_TS)

    # todo: 构造DIS和metaPDIES等等，返回对应PDIE

    res_PDIE_expression = ""
    for i in range(len(p_op_idx_T)):
        res_PDIE_expression += p_atom_PDIE_S[i].getExpression()
        if i < len(p_op_idx_T) - 1:
            res_PDIE_expression += ' + '

    res_PDIE = PDIE(expression=res_PDIE_expression,
                    is_error=False,
                    is_atom=False,
                    OP='+',
                    meta_PDIES=p_atom_PDIE_S,
                    DI_2tuple_S=DI_2tuple_S)

    return res_PDIE