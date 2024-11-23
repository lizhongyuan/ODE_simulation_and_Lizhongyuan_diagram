"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/12
"""

from simulations.OP.atomOP import atom_add
from simulations.PDIE.pdie import AtomPDIE
from simulations.PDIE.pdieS import PDIES, AtomPDIES
from simulations.structure import _2TupleS, _2Tuple, _2TupleTS, _2TupleT

if __name__ == '__main__':

    empty_PDIES = PDIES([])

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    DI_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_PDIE_1 = AtomPDIE(expression='atomPDIE1', DI_2tuple_S=DI_2tuple_S_1)

    print(str(atom_PDIE_1))
    print(str(atom_PDIE_1.get_factor_DI_distinct_same_bound_2tuple_TSS()))

    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])
    DI_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_PDIE_2 = AtomPDIE(expression='atomPDIE2', DI_2tuple_S=DI_2tuple_S_2)

    print(str(atom_PDIE_2))

    atom_PDIE_S_1 = AtomPDIES([ atom_PDIE_1, atom_PDIE_2 ])

    comm_cut_2tuple_A = _2Tuple([ 1, 4 ])
    comm_cut_2tuple_B = _2Tuple([ 1, 5 ])

    unfeasible_DI_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    unfeasible_DI_2tuple_TS_2 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ]),
        _2TupleT([ _2_tuple_1, _2_tuple_5 ]),
        _2TupleT([ _2_tuple_2, _2_tuple_4 ]),
    ])
    empty_unfeasible_DI_2tuple_TS = _2TupleTS([])
    wildcard_unfeasible_DI_2tuple_TS = _2TupleTS([
        _2TupleT([ _2_tuple_3, '*', ]),
    ])

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

    atom_PDIE_S_1.set_unfeasible_DI_2tuple_info(unfeasible_DI_2tuple_TS=unfeasible_DI_2tuple_TS_2,
                                                unfeasible_PDIE_tuple=(atom_PDIE_1, atom_PDIE_2))
    res = atom_add(p_atom_PDIE_S=atom_PDIE_S_1,
                   p_op_idx_T=(1, 2),
                   p_comm_cut_2tuple=_2Tuple([ 1, 5 ]))
    print(str(res))
