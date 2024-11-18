from simulations.function import get_bound_2tuple, get_bound_2tuple_S
from simulations.structure import _2Tuple, _2TupleT, _2TupleTS

if __name__ == '__main__':
    _2tuple_1 = _2Tuple([1, 2])
    _2tuple_2 = _2Tuple([3, 4])
    _2tuple_T_1 = _2TupleT([_2tuple_1, _2tuple_2])

    _2tuple_3 = _2Tuple([1, 3])
    _2tuple_4 = _2Tuple([2, 4])
    _2tuple_T_2 = _2TupleT([_2tuple_3, _2tuple_4])

    _2tuple_5 = _2Tuple([1, 2])
    _2tuple_6 = _2Tuple([3, 4])
    _2tuple_7 = _2Tuple([4, 5])
    _2tuple_T_3 = _2TupleT([_2tuple_5, _2tuple_6, _2tuple_7])

    bound_2tuple_1 = get_bound_2tuple(_2tuple_T_1)
    bound_2tuple_2 = get_bound_2tuple(_2tuple_T_2)
    bound_2tuple_3 = get_bound_2tuple(_2tuple_T_3)

    print(str(bound_2tuple_1))
    print(str(bound_2tuple_2))
    print(str(bound_2tuple_3))

    _2tuple_TS = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])

    bound_2tuple_S = get_bound_2tuple_S(_2tuple_TS)
    print(str(bound_2tuple_S))