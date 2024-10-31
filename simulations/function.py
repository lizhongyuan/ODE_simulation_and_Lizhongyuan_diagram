from typing import List

from simulations.structure import TwoTuple, TwoTupleSS, TwoTupleT, TwoTupleTS
from simulations.structure import TwoTupleS

# fMin1oS
def get_min_first_of_2tuple_S(p_2tuple_S: TwoTupleS) -> object:
    min_first = None
    for item in p_2tuple_S:
        if min_first is None or min_first > item.first():
            min_first = item.first()
    return min_first


# fMax2oS
def get_max_second_of_2tuple_S(p_2tuple_S: TwoTupleS) -> object:
    max_second = None
    for item in p_2tuple_S:
        if max_second is None or max_second < item.second():
            max_second = item.second()
    return max_second


# fCPo2tupleSS实现
# 2tupleSS内所有元素, 以pIdxT为顺序, 做笛卡尔积
def get_CP_of_2tuple_SS(p_2tupleSS: TwoTupleSS, p_idxT: List[int]) -> TwoTupleTS:

    sub_2tupleTS_list = get_CP_of_2tupleSS_recur(p_2tupleSS, p_idxT, 1)

    _2tupleTS_list = []
    for cur_2tupleT_list in sub_2tupleTS_list:
        cur_2tupleT = TwoTupleT(cur_2tupleT_list)
        _2tupleTS_list.append(cur_2tupleT)

    _2tupleTS = TwoTupleTS(_2tupleTS_list)

    return _2tupleTS


# 递归求2tupleSS内某些元素的笛卡尔积
def get_CP_of_2tupleSS_recur(p_2tupleSS: TwoTupleSS,
                             p_idxT: List[int],
                             pivot: int) -> List[List[object]]:

    cur_idx = p_idxT[pivot - 1] - 1               # pivot所代表的2tupleS的索引
    cur_2tupleS = p_2tupleSS[cur_idx]

    _2tupleTS_list = []

    if pivot == len(p_idxT):
        for cur_2tuple in cur_2tupleS:
                _2tupleTS_list.append([cur_2tuple])
        return _2tupleTS_list

    post_2tupleTS_list = get_CP_of_2tupleSS_recur(p_2tupleSS, p_idxT, pivot + 1)

    for cur_2tuple in cur_2tupleS:
        for cur_post_2tupleT in post_2tupleTS_list:
            cur_2tupleT = [ cur_2tuple ] + cur_post_2tupleT
            _2tupleTS_list.append(cur_2tupleT)

    return _2tupleTS_list


def is_cut_2tuple(p_2tupleS: TwoTupleS, _2tuple: TwoTuple) -> bool:
    first_elem_match = False
    second_elem_match = False

    for item in p_2tupleS:
        if item.first() == _2tuple.first():
            first_elem_match = True
            if second_elem_match:
                break
        if item.second() == _2tuple.second():
            second_elem_match = True
            if first_elem_match:
                break

    if first_elem_match == False or second_elem_match == False:
        return False

    return True


# fCut2tupleSByDomain函数实现, 求二元组集合在某切割域的切割集合
def get_cut_2tuple_S_by_domain(p_2tuple_S: TwoTupleS,
                               p_A: object,
                               p_B: object) -> TwoTupleS | None:
    cut_2tuple_S_list = []

#    for item in p_2tuple_S.list():
    for item in p_2tuple_S:
        cur_first = item.first()
        cur_second = item.second()

        if cur_first >= p_A and cur_second <= p_B:
            cut_2tuple_S_list.append(item)

    if len(cut_2tuple_S_list) == 0:
        return None

    first_elem_match = False
    second_elem_match = False

    for item in cut_2tuple_S_list:
        if item.first() == p_A:
            first_elem_match = True
            if second_elem_match:
                break
        if item.second() == p_B:
            second_elem_match = True
            if first_elem_match:
                break

    if first_elem_match == False or second_elem_match == False:
        return None

    cut_2tuple_S = TwoTupleS(cut_2tuple_S_list)

    return cut_2tuple_S


# fLargestCommCut2tupleS函数实现, 求p_2tuple_SS的最大的公共切割二元组集合
def get_largest_comm_cut_2tuple_S(p_2tuple_SS: TwoTupleSS) -> TwoTupleS:
    # todo
    pass


# fBound2tuple函数实现
def get_bound_2tuple(p_2tupleT: TwoTupleT) -> TwoTuple | None:

    if p_2tupleT is None:
        return None

    min_first = p_2tupleT[1].first()
    max_second = p_2tupleT[1].second()

    for item in p_2tupleT.list():
        if min_first > item.first():
            min_first = item.first()
        if max_second < item.second():
            max_second = item.second()

    return TwoTuple([min_first, max_second])


# fBound2tupleS函数实现
def get_bound_2tuple_S(p_2tupleT_S: TwoTupleTS) -> TwoTupleS | None:

    if p_2tupleT_S is None:
        return None

    bound_2tuple_S_list = []
    bound_2tuple_map = set()
    for cur_2tupleT in p_2tupleT_S.list():
        cur_bound_2tuple = get_bound_2tuple(cur_2tupleT)
        if cur_bound_2tuple.instance() not in bound_2tuple_map:
            bound_2tuple_S_list.append(TwoTuple(cur_bound_2tuple.list()))
            bound_2tuple_map.add(cur_bound_2tuple.instance())

    return TwoTupleS(bound_2tuple_S_list)


# fUnfeasibleAscMetaDI2tupleTS函数实现
def fUnfeasibleAscMetaDI2tupleTS():
    pass

def fCut2tupleSbyDomain(p2tupleS, pA, pB):
    pass
    # todo
