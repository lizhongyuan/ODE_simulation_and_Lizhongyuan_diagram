from simulations.domainFilteredSub2tupleTS import Pred_is_2tuple_T_in_Domain, get_domain_filtered_sub_2tuple_TS
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

    _2tuple_TS = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])

    _2tuple_T_4 = _2TupleT([_2tuple_1, _2tuple_3])
    res = Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T_4, 1, 4)
    print(res)
    res = Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T_1, 1, 4)
    print(res)
    res = Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T_1, 1, 4.5)
    print(res)

    domain_filtered_sub_2tuple_TS_2 = get_domain_filtered_sub_2tuple_TS(_2tuple_TS, 1, 4)
    print(domain_filtered_sub_2tuple_TS_2)

    domain_filtered_sub_2tuple_TS_3 = get_domain_filtered_sub_2tuple_TS(_2tuple_TS, 1, 4.5)
    print(domain_filtered_sub_2tuple_TS_3)
