from simulations.function import fMin1oS, fMax2oS, get_CP_of_2tupleSS_recur, get_bound_2tuple
from simulations.function import get_CP_of_2tupleSS
from simulations.structure import TwoTuple, TwoTupleT, TwoTupleSS
from simulations.structure import TwoTupleS

if __name__ == '__main__':
    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([3, 4])
    _2tuple_T_1 = TwoTupleT([twoT1, twoT2])

    twoT3 = TwoTuple([1, 3])
    twoT4 = TwoTuple([2, 4])
    _2tuple_T_2 = TwoTupleT([twoT3, twoT4])

    twoT5 = TwoTuple([1, 2])
    twoT6 = TwoTuple([3, 4])
    twoT7 = TwoTuple([4, 5])
    _2tuple_T_3 = TwoTupleT([twoT5, twoT6, twoT7])

    bound_2tuple_1 = get_bound_2tuple(_2tuple_T_1)
    bound_2tuple_2 = get_bound_2tuple(_2tuple_T_2)
    bound_2tuple_3 = get_bound_2tuple(_2tuple_T_3)

    print(str(bound_2tuple_1))
    print(str(bound_2tuple_2))
    print(str(bound_2tuple_3))
