"""
@file test_add_1.py
@brief Brief description of the file.
@author Your Name
@date 2025/1/27
"""


from simulations.OP.pdieOP import complete_sequential_addition
from simulations.PDIE.pdie import AtomPDIE
from simulations.PDIE.pdieS import PDIES
from simulations.structure import _2TupleS, _2Tuple, _2TupleTS, _2TupleT


def test_complete_sequential_addition_1():

    # ---------- 1 Init some PDIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1',
                           p_DI_2tuple_S=DI_2tuple_S_1)

    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2',
                           p_DI_2tuple_S=DI_2tuple_S_2)

    # ---------- 2 Init a PDIES instance ----------

    PDIE_S = PDIES([ atom_PDIE_1, atom_PDIE_2 ])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to the PDIES instance ----------

    # 3.1 init a UnfeasibleDI2TupleTS instance
    unfeasible_DI_2tuple_TS_2 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ]),
        _2TupleT([ _2_tuple_1, _2_tuple_5 ]),
        _2TupleT([ _2_tuple_2, _2_tuple_4 ]),
    ])
    # 3.2 Assign to the member value of PDIE_S
    PDIE_S.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_2,
                                                  p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 5])
    # 4.2 Execute
    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果PDIE如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_2():

    # ---------- 1 Init some PDIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1',
                           p_DI_2tuple_S=DI_2tuple_S_1)

    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2',
                           p_DI_2tuple_S=DI_2tuple_S_2)

    DI_2tuple_S_3 = _2TupleS([ _2_tuple_1, _2_tuple_5 ])
    atom_PDIE_3 = AtomPDIE(p_expression='atomPDIE3',
                           p_DI_2tuple_S=DI_2tuple_S_3)

    # ---------- 2 Init a PDIES instance ----------

    PDIE_S_1 = PDIES([ atom_PDIE_1, atom_PDIE_2 ])
    PDIE_S_2 = PDIES([ atom_PDIE_1, atom_PDIE_2, atom_PDIE_3 ])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to the PDIES instance ----------

    # 3.1 init a UnfeasibleDI2TupleTS instance
    unfeasible_DI_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    # 3.2 Assign to the member value of PDIE_S
    PDIE_S_1.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_1,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple_A = _2Tuple([1, 4])
    # 4.2 Execute
    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S_1,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple_A)

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_3():

    # ---------- 1 Init some PDIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1',
                           p_DI_2tuple_S=DI_2tuple_S_1)

    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2',
                           p_DI_2tuple_S=DI_2tuple_S_2)

    # ---------- 2 Init a PDIES instance ----------

    PDIE_S = PDIES([ atom_PDIE_1, atom_PDIE_2 ])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to the PDIES instance ----------

    # 3.1 init a UnfeasibleDI2TupleTS instance
    wildcard_unfeasible_DI_2tuple_TS = _2TupleTS([
        _2TupleT([ _2_tuple_1, '*', ]),
        _2TupleT([ _2_tuple_2, '*', ]),
        _2TupleT([ '*', _2_tuple_6, ]),

    ])
    # 3.2 Assign to the member value of PDIE_S
    PDIE_S.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=wildcard_unfeasible_DI_2tuple_TS,
                                                  p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 5])
    # 4.2 Execute
    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_4():

    # ---------- 1 Init some PDIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1',
                           p_DI_2tuple_S=DI_2tuple_S_1)

    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2',
                           p_DI_2tuple_S=DI_2tuple_S_2)

    # ---------- 2 Init a PDIES instance ----------

    PDIE_S = PDIES([ atom_PDIE_1, atom_PDIE_2 ])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to the PDIES instance ----------

    # 3.1 init a UnfeasibleDI2TupleTS instance
    empty_unfeasible_DI_2tuple_TS = _2TupleTS([])
    # 3.2 Assign to the member value of PDIE_S
    PDIE_S.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=empty_unfeasible_DI_2tuple_TS,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 4])
    # 4.2 Execute
    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_5():

    # ---------- 1 Init some PDIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1',
                           p_DI_2tuple_S=DI_2tuple_S_1)

    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2',
                           p_DI_2tuple_S=DI_2tuple_S_2)

    DI_2tuple_S_3 = _2TupleS([ _2_tuple_1, _2_tuple_5 ])
    atom_PDIE_3 = AtomPDIE(p_expression='atomPDIE3',
                           p_DI_2tuple_S=DI_2tuple_S_3)

    # ---------- 2 Init a PDIES instance ----------

    PDIE_S_2 = PDIES([ atom_PDIE_1, atom_PDIE_2, atom_PDIE_3 ])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to the PDIES instance ----------

    # 3.1 init a UnfeasibleDI2TupleTS instance
    unfeasible_DI_2tuple_TS_123 = _2TupleTS([
        _2TupleT(['*', '*', '*']),
    ])
    # 3.2 Assign to the member value of PDIE_S
    PDIE_S_2.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_123,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2, atom_PDIE_3))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 4])
    # 4.2 Execute
    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S_2,
                                            p_op_idx_T=(1, 2, 3),
                                            p_domain_filter_2tuple=domain_filter_2tuple)

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_6():

    # ---------- 1 Init some PDIE instances ----------

    _2_tuple_1 = _2Tuple([1, 2])
    _2_tuple_2 = _2Tuple([3, 4])
    _2_tuple_3 = _2Tuple([4, 5])
    _2_tuple_4 = _2Tuple([1, 3])
    _2_tuple_5 = _2Tuple([2, 4])
    _2_tuple_6 = _2Tuple([3, 5])

    DI_2tuple_S_1 = _2TupleS([_2_tuple_1, _2_tuple_2, _2_tuple_3])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1',
                           p_DI_2tuple_S=DI_2tuple_S_1)

    DI_2tuple_S_2 = _2TupleS([_2_tuple_4, _2_tuple_5, _2_tuple_6])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2',
                           p_DI_2tuple_S=DI_2tuple_S_2)

    DI_2tuple_S_3 = _2TupleS([_2_tuple_1, _2_tuple_5])
    atom_PDIE_3 = AtomPDIE(p_expression='atomPDIE3',
                           p_DI_2tuple_S=DI_2tuple_S_3)

    # ---------- 2 Init a PDIES instance ----------

    PDIE_S = PDIES([atom_PDIE_1, atom_PDIE_2, atom_PDIE_3])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to the PDIES instance ----------

    # 3.1 init a UnfeasibleDI2TupleTS instance
    empty_unfeasible_DI_2tuple_TS = _2TupleTS([])
    # 3.2 Assign to the member value of PDIE_S
    PDIE_S.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=empty_unfeasible_DI_2tuple_TS,
                                                  p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2, atom_PDIE_3))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 4])
    # 4.2 Execute
    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S,
                                            p_op_idx_T=(1, 3, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")