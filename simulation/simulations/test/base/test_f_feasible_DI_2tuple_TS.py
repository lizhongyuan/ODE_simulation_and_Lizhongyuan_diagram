"""
@file test_f_feasible_DI_2tuple_TS.py
@brief: Test cases of function f_feasible_DI_2tuple_TS.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from simulations.OIE.feasible import f_feasible_DI_2tuple_TS
from simulations.OIE.optional_intervals_event_set import OIES
from simulations.OIE.optional_intervals_event import AtomOIE
from simulations.OIE._2Tuple import _2Tuple
from simulations.OIE._2Tuple_T import _2TupleT
from simulations.OIE._2Tuple_TS import _2TupleTS
from simulations.OIE._2Tuple_S import _2TupleS


def test_f_feasible_DI_2tuple_TS() -> None:

    print('test_f_feasible_DI_2tuple_TS')

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_OIE_1 = AtomOIE(p_expression='atomOIE1', p_DI_2tuple_S=DI_2tuple_S_1)

    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])
    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_OIE_2 = AtomOIE(p_expression='atomOIE2', p_DI_2tuple_S=DI_2tuple_S_2)

    OIE_S_1 = OIES([ atom_OIE_1, atom_OIE_2 ])
    unfeasible_DI_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    # unfeasible_DI_2tuple_TS_1 = _2TupleTS([
    #     _2TupleT([ '*', '*' ])
    # ])

    OIE_S_1.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_1,
                                                    p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    feasible_DI_2tuple_TS = f_feasible_DI_2tuple_TS(OIE_S_1, (1, 2))

    print(feasible_DI_2tuple_TS)
