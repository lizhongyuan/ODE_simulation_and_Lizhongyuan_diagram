"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/21
"""

from simulations.OP.atomOP import atom_add
from simulations.PDIE.pdie import AtomPDIE
from simulations.PDIE.pdieS import PDIES, AtomPDIES
from simulations.structure import _2TupleS, _2Tuple, _2TupleTS, _2TupleT

if __name__ == '__main__':

    empty_PDIES = PDIES([])

    _2_tuple_11 = _2Tuple([ 1, 2 ])
    _2_tuple_12 = _2Tuple([ 2, 4 ])
    _2_tuple_13 = _2Tuple([ 6, 7 ])
    DI_2tuple_S_1 = _2TupleS([ _2_tuple_11, _2_tuple_12, _2_tuple_13 ])
    atom_PDIE_1 = AtomPDIE(expression='atomPDIE1', DI_2tuple_S=DI_2tuple_S_1)
    print(str(atom_PDIE_1))

    _2_tuple_21 = _2Tuple([ 1, 3 ])
    _2_tuple_22 = _2Tuple([ 3, 4 ])
    _2_tuple_23 = _2Tuple([ 5, 7 ])
    DI_2tuple_S_2 = _2TupleS([ _2_tuple_21, _2_tuple_22, _2_tuple_23 ])
    atom_PDIE_2 = AtomPDIE(expression='atomPDIE2', DI_2tuple_S=DI_2tuple_S_2)
    print(str(atom_PDIE_2))

    _2_tuple_31 = _2Tuple([ 1, 3 ])
    _2_tuple_32 = _2Tuple([ 5, 7 ])
    DI_2tuple_S_3 = _2TupleS([ _2_tuple_31, _2_tuple_32, ])
    atom_PDIE_3 = AtomPDIE(expression='atomPDIE3', DI_2tuple_S=DI_2tuple_S_3)
    print(str(atom_PDIE_3))

    _2_tuple_41 = _2Tuple([ 1, 4 ])
    _2_tuple_42 = _2Tuple([ 4, 7 ])
    DI_2tuple_S_4 = _2TupleS([ _2_tuple_41, _2_tuple_42, ])
    atom_PDIE_4 = AtomPDIE(expression='atomPDIE4', DI_2tuple_S=DI_2tuple_S_4)
    print(str(atom_PDIE_4))

