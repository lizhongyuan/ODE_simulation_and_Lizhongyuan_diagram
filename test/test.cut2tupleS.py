from simulations.function import get_bound_2tuple, get_bound_2tuple_S, get_cut_2tuple_S_by_domain, is_cut_2tuple
from simulations.structure import TwoTuple, TwoTupleT, TwoTupleTS, TwoTupleS


if __name__ == '__main__':

    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([3, 4])
    twoT3 = TwoTuple([1, 3])
    twoT4 = TwoTuple([2, 4])

    _2tuple_S = TwoTupleS([twoT1, twoT2, twoT3, twoT4])


    ##
    # 1 测试is_cut_2tuple
    print("---------- 1 Test is_cut_2tuple ----------")

    res1 = is_cut_2tuple(_2tuple_S, twoT3)
    print(f"res1: {res1}")

    test_2tuple = TwoTuple([1, 2.5])
    res2 = is_cut_2tuple(_2tuple_S, test_2tuple)
    print(f"res2: {res2}")

    test_2tuple_2 = TwoTuple([1, 3])
    res3 = is_cut_2tuple(_2tuple_S, test_2tuple_2)
    print(f"res3: {res3}")

    print("---------- 2 Test get_cut_2tuple_S_by_domain ----------")
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
