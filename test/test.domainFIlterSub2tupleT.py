from simulations.domainFilteredSub2tupleTS import Pred_is_2tuple_T_in_Domain
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

    _2tuple_TS = TwoTupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])

    _2tuple_T_4 = TwoTupleT([_2tuple_1, _2tuple_3])
    res = Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T_4, 1, 4)
    print(res)
    res = Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T_1, 1, 4)
    print(res)
    res = Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T_1, 1, 4.5)
    print(res)
