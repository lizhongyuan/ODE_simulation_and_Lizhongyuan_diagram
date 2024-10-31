from simulations.function import get_bound_2tuple, get_bound_2tuple_S
from simulations.structure import TwoTuple, TwoTupleT, TwoTupleTS

if __name__ == '__main__':
    _2tuple_1 = TwoTuple([1, 2])
    _2tuple_2 = TwoTuple([3, 4])
    _2tuple_T_1 = TwoTupleT([_2tuple_1, _2tuple_2])

    _2tuple_3 = TwoTuple([1, 3])
    _2tuple_4 = TwoTuple([2, 4])
    _2tuple_T_2 = TwoTupleT([_2tuple_3, _2tuple_4])

    _2tuple_5 = TwoTuple([1, 2])
    _2tuple_6 = TwoTuple([3, 4])
    _2tuple_7 = TwoTuple([4, 5])
    _2tuple_T_3 = TwoTupleT([_2tuple_5, _2tuple_6, _2tuple_7])

    bound_2tuple_1 = get_bound_2tuple(_2tuple_T_1)
    bound_2tuple_2 = get_bound_2tuple(_2tuple_T_2)
    bound_2tuple_3 = get_bound_2tuple(_2tuple_T_3)

    print(str(bound_2tuple_1))
    print(str(bound_2tuple_2))
    print(str(bound_2tuple_3))

    _2tuple_TS = TwoTupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])

    bound_2tuple_S = get_bound_2tuple_S(_2tuple_TS)
    print(str(bound_2tuple_S))