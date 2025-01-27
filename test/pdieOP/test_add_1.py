"""
@file test_add_1.py
@brief Brief description of the file.
@author Your Name
@date 2025/1/27
"""


from simulations.OP.pdieOP import complete_sequential_addition, multi
from simulations.PDIE.pdie import PDIE, AtomPDIE
from simulations.PDIE.pdieS import PDIES
from simulations.structure import _2TupleS, _2Tuple, _2TupleTS, _2TupleT


def test_complete_sequential_addition_1():

    # 1 init some PDIE instances
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

    # 3 init PDIES instance
    PDIE_S_1 = PDIES([ atom_PDIE_1, atom_PDIE_2 ])
    PDIE_S_2 = PDIES([ atom_PDIE_1, atom_PDIE_2, atom_PDIE_3 ])

    # 4 set UnfeasibleDI2TupleTS instance to PDIES instance
    # unfeasible_DI_2tuple_TS_1 = _2TupleTS([
    #     _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    # ])
    unfeasible_DI_2tuple_TS_2 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ]),
        _2TupleT([ _2_tuple_1, _2_tuple_5 ]),
        _2TupleT([ _2_tuple_2, _2_tuple_4 ]),
    ])
    # empty_unfeasible_DI_2tuple_TS = _2TupleTS([])
    # wildcard_unfeasible_DI_2tuple_TS = _2TupleTS([
    #     _2TupleT([ _2_tuple_3, '*', ]),
    # ])
    #
    # unfeasible_DI_2tuple_TS_123 = _2TupleTS([
    #     _2TupleT(['*', '*', '*']),
    # ])

    PDIE_S_1.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_2,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # 5 init a DomainFilter2Tuple instance
    # domain_filter_2tuple_A = _2Tuple([1, 4])
    domain_filter_2tuple_B = _2Tuple([1, 5])

    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S_1,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple_B)
    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果PDIE如下")
        print(f"{str(PDIE_res)}\n")

    # atom_PDIE_S_1.set_unfeasible_DI_2tuple_info(unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_1,
    #                                             unfeasible_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))
    # res = atom_add(p_atom_PDIE_S=atom_PDIE_S_1,
    #                p_op_idx_T=(1, 2),
    #                p_comm_cut_2tuple=_2Tuple([ 1, 4 ]))
    # print(str(res))

    # # todo: 让大伙验证一下这个
    # atom_PDIE_S_1.set_unfeasible_DI_2tuple_info(unfeasible_DI_2tuple_TS=wildcard_unfeasible_DI_2tuple_TS,
    #                                             unfeasible_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))
    # res = atom_add(p_atom_PDIE_S=atom_PDIE_S_1,
    #                p_op_idx_T=(1, 2),
    #                p_comm_cut_2tuple=_2Tuple([ 1, 4 ]))
    # print(str(res))

    # atom_PDIE_S_1.set_unfeasible_DI_2tuple_info(unfeasible_DI_2tuple_TS=empty_unfeasible_DI_2tuple_TS,
    #                                             unfeasible_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))
    # res = atom_add(p_atom_PDIE_S=atom_PDIE_S_1,
    #                p_op_idx_T=(1, 2),
    #                p_comm_cut_2tuple=_2Tuple([ 1, 4 ]),
    #                )
    # print(str(res))



    # PDIE_S_2.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_123,
    #                                                 p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2, atom_PDIE_3))
    # PDIE_res = add(p_PDIE_S=PDIE_S_2,
    #                p_op_idx_T=(1, 2, 3),
    #                p_comm_cut_2tuple=_2Tuple([ 1, 4 ]))
    # print(f"PDIE加法执行成功, 结果PDIE如下")
    # print(f"{str(PDIE_res)}\n")
    #
    # PDIE_res = add(p_PDIE_S=PDIE_S_2,
    #                p_op_idx_T=(1, 3, 2),
    #                p_comm_cut_2tuple=_2Tuple([1, 4]))
    # print(f"PDIE加法执行成功, 结果PDIE如下")
    # print(f"{str(PDIE_res)}\n")
    #
    # PDIE_S_1.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_1,
    #                                                 p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))
    # PDIE_res = multi(p_PDIE_S=PDIE_S_1,
    #                  p_op_idx_T=(1, 2))
    # print(f"PDIE乘法执行成功, 结果PDIE如下")
    # print(f"{str(PDIE_res)}\n")
    #
    # PDIE_res = multi(p_PDIE_S=PDIE_S_1,
    #                  p_op_idx_T=(2, 1))
    # print(f"PDIE乘法执行成功, 结果PDIE如下")
    # print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_2():

    # 1 init some PDIE instances
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

    # 2 init PDIES instance
    PDIE_S_1 = PDIES([ atom_PDIE_1, atom_PDIE_2 ])
    PDIE_S_2 = PDIES([ atom_PDIE_1, atom_PDIE_2, atom_PDIE_3 ])

    # 3 set UnfeasibleDI2TupleTS instance to PDIES instance
    unfeasible_DI_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])

    PDIE_S_1.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_1,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # 4 init a DomainFilter2Tuple instance
    domain_filter_2tuple_A = _2Tuple([1, 4])

    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S_1,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple_A)
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

    # ---------- 2 Init PDIES instance ----------

    PDIE_S = PDIES([ atom_PDIE_1, atom_PDIE_2 ])

    # ---------- 3 Set UnfeasibleDI2TupleTS instance to PDIES instance ----------

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

    # 4.1 init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 5])
    # 4.2 execute
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

    # 1 init some PDIE instances
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

    # 2 init PDIES instance
    PDIE_S = PDIES([ atom_PDIE_1, atom_PDIE_2 ])

    # 3 set UnfeasibleDI2TupleTS instance to PDIES instance
    empty_unfeasible_DI_2tuple_TS = _2TupleTS([])

    PDIE_S.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=empty_unfeasible_DI_2tuple_TS,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

    # 4 init a DomainFilter2Tuple instance
    domain_filter_2tuple_A = _2Tuple([1, 4])

    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S,
                                            p_op_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple_A)
    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_5():

    # 1 init some PDIE instances
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

    # 2 init PDIES instance
    PDIE_S_2 = PDIES([ atom_PDIE_1, atom_PDIE_2, atom_PDIE_3 ])

    # 3 set UnfeasibleDI2TupleTS instance to PDIES instance
    unfeasible_DI_2tuple_TS_123 = _2TupleTS([
        _2TupleT(['*', '*', '*']),
    ])

    PDIE_S_2.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_123,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2, atom_PDIE_3))

    # 4 init a DomainFilter2Tuple instance
    domain_filter_2tuple_A = _2Tuple([1, 4])

    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S_2,
                                            p_op_idx_T=(1, 2, 3),
                                            p_domain_filter_2tuple=domain_filter_2tuple_A)

    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")


def test_complete_sequential_addition_6():
    # 1 init some PDIE instances
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

    # 2 init PDIES instance
    PDIE_S_2 = PDIES([atom_PDIE_1, atom_PDIE_2, atom_PDIE_3])

    # 3 set UnfeasibleDI2TupleTS instance to PDIES instance
    empty_unfeasible_DI_2tuple_TS = _2TupleTS([])

    PDIE_S_2.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=empty_unfeasible_DI_2tuple_TS,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2, atom_PDIE_3))

    # 4 init a DomainFilter2Tuple instance
    domain_filter_2tuple_A = _2Tuple([1, 4])

    PDIE_res = complete_sequential_addition(p_PDIE_S=PDIE_S_2,
                                            p_op_idx_T=(1, 3, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple_A)
    if PDIE_res.isError():
        print(f"完全时序加法结果为PDIE_error")
    else:
        print(f"完全时序加法执行成功, 结果如下")
        print(f"{str(PDIE_res)}\n")