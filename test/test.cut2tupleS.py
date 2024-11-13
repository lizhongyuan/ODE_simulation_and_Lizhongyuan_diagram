from simulations.cut2tupleS import (get_cut_2tuple_S_by_domain, Pred_is_cut_2tuple, get_largest_comm_cut_2tuple_S,
                                    get_max_comm_cut_2tuple)
from simulations.structure import _2Tuple, _2TupleT, _2TupleTS, _2TupleS, _2TupleSS

if __name__ == '__main__':

    _2tuple_1 = _2Tuple([1, 2])
    _2tuple_2 = _2Tuple([3, 4])
    _2tuple_3 = _2Tuple([1, 3])
    _2tuple_4 = _2Tuple([2, 4])

    _2tuple_S = _2TupleS([_2tuple_1, _2tuple_2, _2tuple_3, _2tuple_4])

    ##
    # 1 测试is_cut_2tuple, 非论文内容
    print("---------- 1 Test is_cut_2tuple, not in paper ----------")

    res1 = Pred_is_cut_2tuple(_2tuple_S, _2tuple_3)
    print(f"res1: {res1}")

    test_2tuple = _2Tuple([1, 2.5])
    res2 = Pred_is_cut_2tuple(_2tuple_S, test_2tuple)
    print(f"res2: {res2}")

    test_2tuple_2 = _2Tuple([2, 3])
    res3 = Pred_is_cut_2tuple(_2tuple_S, test_2tuple_2)
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

    print("---------- 3 Test get_largest_comm_cut_2tuple_S ----------")

    twoT5 = _2Tuple([1, 2])
    twoT6 = _2Tuple([3, 4])
    twoT7 = _2Tuple([4, 5])
    twoTplS1 = _2TupleS([_2tuple_1, _2tuple_2])
    twoTplS2 = _2TupleS([_2tuple_3, _2tuple_4, twoT6])
    twoTplS3 = _2TupleS([twoT5, twoT6, twoT7])

    twoTupleSS = _2TupleSS([twoTplS1, twoTplS2, twoTplS3])
    # 最大的公共切割二元组集合
    print(f"2tupleSS: {str(twoTupleSS)}")
    largest_comm_cut_2tuple_S = get_largest_comm_cut_2tuple_S(twoTupleSS)
    print(str(largest_comm_cut_2tuple_S))

    print("---------- 4 Test get_max_comm_cut_2tuple ----------")

    max_comm_cut_2tuple = get_max_comm_cut_2tuple(twoTupleSS)
    print(str(max_comm_cut_2tuple))
