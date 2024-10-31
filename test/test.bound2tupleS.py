from simulations.function import get_bound_2tuple, get_bound_2tuple_S
from simulations.structure import TwoTuple, TwoTupleT, TwoTupleTS

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

    _2tuple_TS = TwoTupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])

    bound_2tuple_S = get_bound_2tuple_S(_2tuple_TS)
    print(str(bound_2tuple_S))