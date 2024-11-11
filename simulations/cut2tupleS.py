# cut2tupleS
# 
#

from simulations.structure import TwoTuple, TwoTupleSS, TwoTupleT, TwoTupleTS
from simulations.structure import TwoTupleS
from collections import OrderedDict

##
# is_cut_2tuple函数实现, 判断二元组_2tuple是否是p_2tupleS的一个切割二元组
def Pred_is_cut_2tuple(p_2tupleS: TwoTupleS, p_2tuple: TwoTuple) -> bool:
    left_match = False
    right_match = False

    for _2tuple in p_2tupleS:
        if _2tuple.first() == p_2tuple.first() and _2tuple.second() == p_2tuple.second():
            return True
        if _2tuple.first() == p_2tuple.first() and _2tuple.second() < p_2tuple.second():
            left_match = True
            if right_match:
                return True
        if _2tuple.second() == p_2tuple.second() and _2tuple.first() > p_2tuple.first():
            right_match = True
            if left_match:
                return True

    return False


# fCut2tupleSByDomain函数实现, 求二元组集合在某切割域的切割集合
def get_cut_2tuple_S_by_domain(p_2tuple_S: TwoTupleS,
                               p_A: object,
                               p_B: object) -> TwoTupleS | None:
    if not Pred_is_cut_2tuple(p_2tuple_S, TwoTuple([p_A, p_B])):
        return TwoTupleS([])

    _2tuple_S = TwoTupleS([])

    for _2tuple in p_2tuple_S:
        first = _2tuple.first()
        second = _2tuple.second()

        if first >= p_A and second <= p_B:
            _2tuple_S.add(_2tuple)

    if _2tuple_S.empty():
        return _2tuple_S

    left_match = False
    right_match = False

    for _2tuple in _2tuple_S:
        if _2tuple.first() == p_A and _2tuple.second() <= p_B:
            left_match = True
            if right_match:
                break
        if _2tuple.second() == p_B and _2tuple.first() >= p_A:
            right_match = True
            if left_match:
                break

    if left_match == False or right_match == False:
        return TwoTupleS([])

    return _2tuple_S


# fLargestCommCut2tupleS函数实现, 求p_2tuple_SS的最大的公共切割二元组的集合
def get_largest_comm_cut_2tuple_S(p_2tuple_SS: TwoTupleSS) -> TwoTupleS:

    ### ---------- 1 获取所有的第一项和第二项 ----------

    first_list = []
    second_list = []

    for _2tuple_S in p_2tuple_SS:
        for _2tuple in _2tuple_S:
            first_list.append(_2tuple.first())
            second_list.append(_2tuple.second())

    first_list = list(OrderedDict.fromkeys(first_list))
    second_list = list(OrderedDict.fromkeys(second_list))

    largest_comm_cut_2tuple_S = TwoTupleS([])

    ### ---------- 2 所有的第一项和第二项, 构造二元组, 检查是否是切割二元组, 并添加到列表 ----------
    for first in first_list:
        for second in second_list:

            # 2.1 跳过不合法的二元组
            if first >= second:
                continue

            # 2.2 跳过重复的二元组
            _2tuple = TwoTuple([first, second])
            if _2tuple in largest_comm_cut_2tuple_S:
                continue

            # 2.3 检查是否是p_2tuple_SS每个元素的切割二元组, 如果是则插入列表
            is_comm_cut_2tuple = True
            for _2tuple_S in p_2tuple_SS:
                if not Pred_is_cut_2tuple(_2tuple_S, _2tuple):
                    is_comm_cut_2tuple = False
                    break

            if is_comm_cut_2tuple:
                largest_comm_cut_2tuple_S.add(_2tuple)

    return largest_comm_cut_2tuple_S


### fMaxCommCutTwoT 求最大公共切割二元组
def get_max_comm_cut_2tuple(p_2tuple_SS: TwoTupleSS) -> TwoTuple | None:
    largest_comm_cut_2tuple_S = get_largest_comm_cut_2tuple_S(p_2tuple_SS)

    if largest_comm_cut_2tuple_S.empty():
        return None

    min_1st = largest_comm_cut_2tuple_S[0].first()
    max_2nd = largest_comm_cut_2tuple_S[0].second()

    for cur_comm_cut_2tuple in largest_comm_cut_2tuple_S:
        if min_1st > cur_comm_cut_2tuple.first():
            min_1st = cur_comm_cut_2tuple.first()
        if max_2nd < cur_comm_cut_2tuple.second():
            max_2nd = cur_comm_cut_2tuple.second()

    max_comm_cut_2tuple = TwoTuple([min_1st, max_2nd])

    return max_comm_cut_2tuple


