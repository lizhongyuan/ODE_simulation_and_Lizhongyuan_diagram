"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/12
"""
from numpy.ma.core import empty

from simulations.pdie import PDIES, PDIE, AtomPDIE
from simulations.structure import _2TupleS, _2Tuple

if __name__ == '__main__':

    empty_PDIES = PDIES([])

    _2_tuple_1 = _2Tuple([1, 2])
    _2_tuple_2 = _2Tuple([4, 5])
    DI_2tuple_S_1 = _2TupleS([_2_tuple_1, _2_tuple_2])
    atom_PDIE_1 = AtomPDIE(DI_2tuple_S=DI_2tuple_S_1)

    print(str(atom_PDIE_1))

    _2_tuple_3 = _2Tuple([1, 3])
    _2_tuple_4 = _2Tuple([2, 4])
    _2_tuple_5 = _2Tuple([3, 5])
    DI_2tuple_S_2 = _2TupleS([_2_tuple_3, _2_tuple_4, _2_tuple_5])
    atom_PDIE_2 = AtomPDIE(DI_2tuple_S=DI_2tuple_S_2)

    print(str(atom_PDIE_2))
