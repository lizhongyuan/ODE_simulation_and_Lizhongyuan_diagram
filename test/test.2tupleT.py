from simulations.structure import TwoTuple, TwoTupleT
from simulations.twoTupleT import get_min_1_of_2tuple_T, get_max_2_of_2tuple_T

if __name__ == '__main__':

    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([3, 4])
    twoT3 = TwoTuple([1, 3])
    twoT4 = TwoTuple([2, 4])


    _2tuple_T_1 = TwoTupleT([twoT1, twoT2])
    _2tuple_T_2 = TwoTupleT([twoT3, twoT4])

    min_1_of_1 = get_min_1_of_2tuple_T(_2tuple_T_1)
    max_2_of_1 = get_max_2_of_2tuple_T(_2tuple_T_1)
    min_1_of_2 = get_min_1_of_2tuple_T(_2tuple_T_2)
    max_2_of_2 = get_max_2_of_2tuple_T(_2tuple_T_2)

    print(get_max_2_of_2tuple_T.__doc__)

    print(f'min_1_of_1: {min_1_of_1}')
    print(f'max_2_of_1: {max_2_of_1}')
    print(f'min_1_of_2: {min_1_of_2}')
    print(f'max_2_of_2: {max_2_of_2}')