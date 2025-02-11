"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2025/1/23
"""

from typing import Tuple

from simulations.PDIE.feasible import f_feasible_DI_2tuple_TS
from simulations.PDIE.partial_duration_interval_event_set import PDIES
from simulations.PDIE.partial_duration_interval_event import AtomPDIE
from simulations.PDIE._2Tuple import _2Tuple
from simulations.PDIE._2Tuple_T import _2TupleT
from simulations.PDIE._2Tuple_TS import _2TupleTS
from simulations.PDIE._2Tuple_S import _2TupleS


def test_f_feasible_DI_2tuple_TS() -> None:

    print('test_f_feasible_DI_2tuple_TS')

#    empty_PDIES = PDIES([])

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(p_expression='atomPDIE1', p_DI_2tuple_S=DI_2tuple_S_1)

    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])
    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(p_expression='atomPDIE2', p_DI_2tuple_S=DI_2tuple_S_2)

    PDIE_S_1 = PDIES([ atom_PDIE_1, atom_PDIE_2 ])
    unfeasible_DI_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    # unfeasible_DI_2tuple_TS_1 = _2TupleTS([
    #     _2TupleT([ '*', '*' ])
    # ])

    PDIE_S_1.set_wildcard_unfeasible_DI_2tuple_info(p_wildcard_unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_1,
                                                    p_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))

#    print(PDIE_S_1)
    feasible_DI_2tuple_TS = f_feasible_DI_2tuple_TS(PDIE_S_1, (1, 2))

    print(feasible_DI_2tuple_TS)
