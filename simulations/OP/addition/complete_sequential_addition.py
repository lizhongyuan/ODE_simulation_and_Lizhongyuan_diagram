"""
@file complete_sequential_addition.py
@brief Brief description of the file.
@author Your Name
@date 2025/2/8
"""

from typing import Tuple

from simulations.OP.helper import check_idx_tuple_border, has_duplicates, print_finish_line
from simulations.PDIE._2Tuple import _2Tuple
from simulations.PDIE._2TupleS import _2TupleS
from simulations.PDIE._2TupleTS import _2TupleTS
from simulations.PDIE.feasible import f_feasible_DI_2tuple_TS
from simulations.PDIE.partial_duration_interval_event import PDIE, PDIE_ERROR
from simulations.PDIE.partial_duration_interval_event_set import PDIES
from simulations.domainFilteredSub2tupleTS import f_domain_filtered_sub_2tuple_TS
from simulations.function import get_bound_2tuple_S


def complete_sequential_addition(p_PDIE_S: PDIES,
                                 p_opd_idx_T: Tuple[int,...],
                                 p_domain_filter_2tuple: _2Tuple) -> PDIE:
    """
    Complete sequential addition
    Args:
        p_PDIE_S (PDIES): A PDIES instance
        p_opd_idx_T(Tuple[int,...]): Index order of operands
        p_domain_filter_2tuple(_2Tuple): A domain filter 2Tuple instance

    Returns:
        PDIE: The result of complete sequential addition
    """

    print(f"####################################################################")
    print(f"##################  Complete sequential addition  ##################")
    print(f"####################################################################\n")

    print(f"1 Check parameters and handle.\n")

    if len(p_PDIE_S) != len(p_opd_idx_T):
        raise ValueError("The length of p_PDIE_S must be equal to the length of p_opd_idx_T.")

    if not check_idx_tuple_border(p_opd_idx_T, len(p_opd_idx_T)):
        raise ValueError("p_opd_idx_T error.")

    if has_duplicates(p_opd_idx_T):
        print(f"There are duplicate elements, get PDIE_error")
        PDIE_result: PDIE = PDIE_ERROR()
        print(f"{str(PDIE_result)}\n")
        print_finish_line()
        return PDIE_result

    for cur_PDIE in p_PDIE_S:
        if cur_PDIE.is_error():
            print(f"There are PDIE_errors in p_PDIE_S, get PDIE_error")
            PDIE_result: PDIE = PDIE_ERROR()
            print(f"{str(PDIE_result)}\n")
            print_finish_line()
            return PDIE_result

    print(f"2 Take the valid subset of the Cartesian product of all members of \nthe DI2TupleSS instance of p_PDIE_S in the order of the indices\n specified by p_opd_idx_T.\n")

    feasible_DI_2tuple_TS: _2TupleTS = f_feasible_DI_2tuple_TS(p_PDIE_S, p_opd_idx_T)
    if feasible_DI_2tuple_TS.empty():
        print(f"feasible_DI_2tuple_TS is empty, get PDIE_error")
        PDIE_result: PDIE = PDIE_ERROR()
        print(f"{str(PDIE_result)}\n")
        print_finish_line()
        return PDIE_result

    print(f"feasible_DI_2tuple_TS: {str(feasible_DI_2tuple_TS)}\n")

    print(f"3 Filter feasible_DI_2tuple_TS using p_domain_filter_2tuple to obtain \n a set of tuples of 2-tuples named domain_filtered_sub_DI_2tuple_TS.\n")

    TS_start: any = p_domain_filter_2tuple.first()
    TS_end: any = p_domain_filter_2tuple.second()

    domain_filtered_sub_DI_2tuple_TS: _2TupleTS = \
        f_domain_filtered_sub_2tuple_TS(feasible_DI_2tuple_TS,
                                        TS_start,
                                        TS_end)
    if domain_filtered_sub_DI_2tuple_TS.empty():
        print(f"domain_filtered_sub_DI_2tuple_TS is empty, get PDIE_error")
        PDIE_result: PDIE = PDIE_ERROR()
        print(f"{str(PDIE_result)}\n")
        print_finish_line()
        return PDIE_result

    print(f"domain_filtered_sub_DI_2tuple_TS: {str(domain_filtered_sub_DI_2tuple_TS)}\n")

    print(f"4 Use domain_filtered_sub_DI_2tuple_TS to calculate the set of duration \n interval 2-tuples of PDIE_result.\n")

    DI_2tuple_S: _2TupleS = get_bound_2tuple_S(domain_filtered_sub_DI_2tuple_TS)

    print(f"DI_2tuple_S: {str(DI_2tuple_S)}\n")

    print(f"5 Build PDIE_result.\n")

    meta_PDIE_list: list[PDIE] = []

    PDIE_result_expression: str = ""

    for i in range(len(p_opd_idx_T)):
        meta_PDIE_list.append(p_PDIE_S[p_opd_idx_T[i] - 1])
        PDIE_result_expression += p_PDIE_S[p_opd_idx_T[i] - 1].getExpression()
        if i < len(p_opd_idx_T) - 1:
            PDIE_result_expression += ' + '

    PDIE_result: PDIE = PDIE(p_expression=PDIE_result_expression,
                             p_is_error=False,
                             p_is_atom=False,
                             p_OP='+',
                             p_meta_PDIE_T=tuple(meta_PDIE_list),
                             p_meta_DI_2tuple_TS=domain_filtered_sub_DI_2tuple_TS,
                             p_DI_2tuple_S=DI_2tuple_S)
    print(f"PDIE_result: {str(PDIE_result)}\n")

    print_finish_line()

    return PDIE_result

