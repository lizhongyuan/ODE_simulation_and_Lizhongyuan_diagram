"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/12
"""
from numpy.ma.core import empty

from simulations.operations import atom_add
from simulations.pdie import PDIES, PDIE, AtomPDIE, AtomPDIES
from simulations.structure import _2TupleS, _2Tuple, _2TupleTS

if __name__ == '__main__':

    empty_PDIES = PDIES([])

    _2_tuple_1 = _2Tuple([1, 2])
    _2_tuple_2 = _2Tuple([3, 4])
    _2_tuple_3 = _2Tuple([4, 5])
    DI_2tuple_S_1 = _2TupleS([_2_tuple_1, _2_tuple_2, _2_tuple_3])
    atom_PDIE_1 = AtomPDIE(DI_2tuple_S=DI_2tuple_S_1)

    print(str(atom_PDIE_1))

    _2_tuple_4 = _2Tuple([1, 3])
    _2_tuple_5 = _2Tuple([2, 4])
    _2_tuple_6 = _2Tuple([3, 5])
    DI_2tuple_S_2 = _2TupleS([_2_tuple_4, _2_tuple_5, _2_tuple_6])
    atom_PDIE_2 = AtomPDIE(DI_2tuple_S=DI_2tuple_S_2)

    print(str(atom_PDIE_2))
    # def atom_add(atom_PDIE_S: AtomPDIES, idx_T: List[int]) -> PDIES | None:

    atom_PDIE_S_1 = AtomPDIES([atom_PDIE_1, atom_PDIE_2])

    comm_cut_2tuple_A = _2Tuple([1, 4])

    unfeasible_DI_2tuple_TS_dict = {
        "idx_T_asc": [1, 2],
        "_2tuple_TS": _2TupleTS([])
    }

    res = atom_add(p_atom_PDIE_S=atom_PDIE_S_1,
                   p_idx_T=[1, 2],
                   p_comm_cut_2tuple=comm_cut_2tuple_A,
                   p_unfeasible_DI_2tuple_TS_dict=unfeasible_DI_2tuple_TS_dict)
    print(str(res))