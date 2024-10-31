from simulations.function import get_bound_2tuple, get_bound_2tuple_S, get_cut_2tuple_S_by_domain
from simulations.structure import TwoTuple, TwoTupleT, TwoTupleTS, TwoTupleS

if __name__ == '__main__':

    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([3, 4])
    twoT3 = TwoTuple([1, 3])
    twoT4 = TwoTuple([2, 4])

    _2tuple_S = TwoTupleS([twoT1, twoT2, twoT3, twoT4])

    cut_2tuple_S_1 = get_cut_2tuple_S_by_domain(_2tuple_S, 1, 1.5)
    print(str(cut_2tuple_S_1))

    cut_2tuple_S_2 = get_cut_2tuple_S_by_domain(_2tuple_S, 1, 2)
    print(str(cut_2tuple_S_2))

    cut_2tuple_S_3 = get_cut_2tuple_S_by_domain(_2tuple_S, 1, 3)
    print(str(cut_2tuple_S_3))

    cut_2tuple_S_4 = get_cut_2tuple_S_by_domain(_2tuple_S, 2, 4)
    print(str(cut_2tuple_S_4))

    cut_2tuple_S_5 = get_cut_2tuple_S_by_domain(_2tuple_S, 1, 4)
    print(str(cut_2tuple_S_5))

    cut_2tuple_S_6 = get_cut_2tuple_S_by_domain(_2tuple_S, 0.5, 4)
    print(str(cut_2tuple_S_6))
