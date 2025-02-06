from simulations.PDIE._2Tuple import _2Tuple
from simulations.PDIE._2TupleT import _2TupleT
from simulations.twoTupleT import get_min_1st_of_2tuple_T, get_max_2nd_of_2tuple_T

if __name__ == '__main__':

    _2tuple_1 = _2Tuple([1, 2])
    _2tuple_2 = _2Tuple([3, 4])
    _2tuple_3 = _2Tuple([1, 3])
    _2tuple_4 = _2Tuple([2, 4])


    _2tuple_T_1 = _2TupleT([_2tuple_1, _2tuple_2])
    _2tuple_T_2 = _2TupleT([_2tuple_3, _2tuple_4])

    min_1st_of_1 = get_min_1st_of_2tuple_T(_2tuple_T_1)
    max_2nd_of_1 = get_max_2nd_of_2tuple_T(_2tuple_T_1)
    min_1st_of_2 = get_min_1st_of_2tuple_T(_2tuple_T_2)
    max_2nd_of_2 = get_max_2nd_of_2tuple_T(_2tuple_T_2)

    print(f'min_1st_of_1: {min_1st_of_1}')
    print(f'max_2nd_of_1: {max_2nd_of_1}')
    print(f'min_1st_of_2: {min_1st_of_2}')
    print(f'max_2nd_of_2: {max_2nd_of_2}')

    wildcard_2tuple_T = _2TupleT([_2tuple_1, '*'])
    print(_2tuple_T_1.wildcard_match(wildcard_2tuple_T))
    print(_2tuple_T_2.wildcard_match(wildcard_2tuple_T))
