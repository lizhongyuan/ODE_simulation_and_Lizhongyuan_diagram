"""
@file test_multi.py
@brief Test complete sequential multiplication.
@author Zhongyuan.Li
@date 2025/1/28
"""


from simulations.OP.pdieOP import complete_sequential_multiplication
from simulations.PDIE.pdie import AtomPDIE
from simulations.PDIE.pdieS import PDIES
from simulations.structure import _2TupleS, _2Tuple, _2TupleTS, _2TupleT


def test_complete_sequential_multiplication_1():

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

    # ---------- 4 Multi ----------

    PDIE_res = complete_sequential_multiplication(p_PDIE_S=PDIE_S,
                                                  p_opd_idx_T=(1, 2))

    # ---------- 5 Show the result ----------

    if PDIE_res.isError():
        print(f"完全时序乘法结果为PDIE_error")
    else:
        print(f"完全时序乘法执行成功, 结果PDIE如下")
        print(f"{str(PDIE_res)}\n")