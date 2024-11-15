"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/14
"""
from typing import List

from simulations.cut2tupleS import get_largest_comm_cut_2tuple_S
from simulations.domainFilteredSub2tupleTS import get_domain_filtered_sub_2tuple_TS
from simulations.function import get_CP_of_2tuple_SS, get_bound_2tuple_S
from simulations.pdie import PDIES, AtomPDIES, PDIE
from simulations.structure import _2Tuple, _2TupleTS


# todo:
def atom_add(p_atom_PDIE_S: AtomPDIES,
             p_idx_T: List[int],
             p_comm_cut_2tuple: _2Tuple,
             p_unfeasible_DI_2tuple_TS_dict: dict) -> PDIE | None:
    print(f"AtomPDIES 时序加法:\n\n")

    # 1 取p_atom_PDIE_S的持续区间二元组集合的集合: DI_2tuple_SS
    DI_2tuple_SS = p_atom_PDIE_S.get_DI_2tuple_SS()

    print(f"1 取p_atom_PDIE_S的持续区间二元组集合的集合\n{str(DI_2tuple_SS)}\n")

    # 2 使用p_idx_T作为笛卡尔积表达式的运算数顺序,
    # 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,
    # 得到一个二元组的元组的集合: _2tuple_TS_CP
    _2tuple_TS_CP = get_CP_of_2tuple_SS(DI_2tuple_SS, p_idx_T)

    print(f"2 使用p_idx_T作为笛卡尔积表达式的运算数顺序, 取DI_2tuple_SS的所有集合元素, 以该顺序进行过笛卡尔积,\n得到一个二元组的元组的集合\n{str(_2tuple_TS_CP)}\n")

    # 3 取_2tuple_TS_CP的合法子集, (暂时认为都合法)todo, 增加索引顺序使用的调整
    feasible_2tuple_TS = _2TupleTS([])
    unfeasible_DI_2tuple_TS = p_unfeasible_DI_2tuple_TS_dict['_2tuple_TS']
    for _2tuple_T in _2tuple_TS_CP:
        if _2tuple_T not in unfeasible_DI_2tuple_TS:
            feasible_2tuple_TS.add(_2tuple_T)
    if feasible_2tuple_TS.empty():
        return None

    print(f"3 取_2tuple_TS_CP的合法子集\n{str(feasible_2tuple_TS)}\n")

    # 4 取DI_2tuple_SS的最大公共切割二元组集合: largest_comm_cut_2tuple_S
    largest_comm_cut_2tuple_S = get_largest_comm_cut_2tuple_S(DI_2tuple_SS)
    if largest_comm_cut_2tuple_S.empty():
        return None

    print(f"4 取DI_2tuple_SS的最大公共切割二元组集合\n{str(largest_comm_cut_2tuple_S)}\n")

    # 5
    if p_comm_cut_2tuple not in largest_comm_cut_2tuple_S:
        return None

    TS_start = p_comm_cut_2tuple.first()
    TS_end = p_comm_cut_2tuple.second()

    domain_filtered_sub_2tuple_TS = get_domain_filtered_sub_2tuple_TS(feasible_2tuple_TS, TS_start, TS_end)
    if domain_filtered_sub_2tuple_TS.empty():
        return None
    print(f"5 {str(domain_filtered_sub_2tuple_TS)}")

    # 6 todo: 论文里完善
    DI_2tuple_S = get_bound_2tuple_S(domain_filtered_sub_2tuple_TS)

    # todo: 构造DIS和metaPDIES等等，返回对应PDIE

    res_PDIE = PDIE(is_atom=False, meta_PDIES=p_atom_PDIE_S, DI_2tuple_S=DI_2tuple_S)

    return res_PDIE