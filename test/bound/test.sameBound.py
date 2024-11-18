"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/18
"""

from simulations.function import get_bound_2tuple, get_bound_2tuple_S
from simulations.sameBound import is_same_bound_2tuple_TS, get_distinct_same_bound_2tuple_TSS
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
#    _2tuple_7 = _2Tuple([4, 5])
    _2tuple_T_3 = _2TupleT([_2tuple_4, _2tuple_5, _2tuple_6])

    # bound_2tuple_1 = get_bound_2tuple(_2tuple_T_1)
    # bound_2tuple_2 = get_bound_2tuple(_2tuple_T_2)
    # bound_2tuple_3 = get_bound_2tuple(_2tuple_T_3)

    _2tuple_7 = _2Tuple([4, 5])
    _2tuple_8 = _2Tuple([3, 5])
    _2tuple_T_4 = _2TupleT([_2tuple_1, _2tuple_2, _2tuple_7])
    _2tuple_T_5 = _2TupleT([_2tuple_3, _2tuple_4, _2tuple_8])

    _2tuple_TS_A = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])
    _2tuple_TS_B = _2TupleTS([_2tuple_T_4, _2tuple_T_5])

    bound_2tuple_S = is_same_bound_2tuple_TS(_2tuple_TS_A)
    print(bound_2tuple_S)
    bound_2tuple_S = is_same_bound_2tuple_TS(_2tuple_TS_B)
    print(bound_2tuple_S)

    _2tuple_TS_A = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])
    diverse_same_bound_2tuple_TSS_A = get_distinct_same_bound_2tuple_TSS(_2tuple_TS_A)
    print(str(diverse_same_bound_2tuple_TSS_A))

    _2tuple_TS_B = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3, _2tuple_T_4])
    diverse_same_bound_2tuple_TSS_B = get_distinct_same_bound_2tuple_TSS(_2tuple_TS_B)
    print(str(diverse_same_bound_2tuple_TSS_B))

    _2tuple_TS_C = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3, _2tuple_T_4, _2tuple_T_5])
    diverse_same_bound_2tuple_TSS_C = get_distinct_same_bound_2tuple_TSS(_2tuple_TS_C)
    print(str(diverse_same_bound_2tuple_TSS_C))
