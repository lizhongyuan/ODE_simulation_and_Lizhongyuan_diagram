# cut2tupleS
# 
#

from simulations.structure import TwoTuple, TwoTupleSS, TwoTupleT, TwoTupleTS
from simulations.structure import TwoTupleS
from collections import OrderedDict

##
# is_cut_2tuple函数实现, 判断二元组_2tuple是否是p_2tupleS的一个切割二元组
def Pred_is_cut_2tuple(p_2tupleS: TwoTupleS, p_2tuple: TwoTuple) -> bool:
    first_elem_match = False
    second_elem_match = False

    for _2tuple in p_2tupleS:
        if _2tuple.first() == p_2tuple.first() and _2tuple.second() <= p_2tuple.second():
            if _2tuple.second() == p_2tuple.second():
                return True
            if second_elem_match:
                return True
            first_elem_match = True
        if _2tuple.second() == p_2tuple.second() and _2tuple.first() >= p_2tuple.first():
            if _2tuple.first() == p_2tuple.first():
                return True
            if first_elem_match:
                return True
            second_elem_match = True

    return False


# fCut2tupleSByDomain函数实现, 求二元组集合在某切割域的切割集合
def get_cut_2tuple_S_by_domain(p_2tuple_S: TwoTupleS,
                               p_A: object,
                               p_B: object) -> TwoTupleS | None:
    if not Pred_is_cut_2tuple(p_2tuple_S, TwoTuple([p_A, p_B])):
        return TwoTupleS([])

    cut_2tuple_S = TwoTupleS([])

    for item in p_2tuple_S:
        cur_first = item.first()
        cur_second = item.second()

        if cur_first >= p_A and cur_second <= p_B:
            cut_2tuple_S.add(item)

    if cut_2tuple_S.empty():
        return cut_2tuple_S

    first_elem_match = False
    second_elem_match = False

    for item in cut_2tuple_S:
        if item.first() == p_A and item.second() <= p_B:
            first_elem_match = True
            if second_elem_match:
                break
        if item.second() == p_B and item.first() >= p_A:
            second_elem_match = True
            if first_elem_match:
                break

    if first_elem_match == False or second_elem_match == False:
        return TwoTupleS([])

    return cut_2tuple_S


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

#    largest_comm_cut_2tuple_S_list = []
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
def get_max_comm_cut_2tuple(p_2tuple_SS: TwoTupleSS):
    largest_comm_cut_2tuple_S = get_largest_comm_cut_2tuple_S(p_2tuple_SS)

    if largest_comm_cut_2tuple_S.empty():
        return None

    min_first = largest_comm_cut_2tuple_S[0].first()
    max_second = largest_comm_cut_2tuple_S[0].second()

    for cur_comm_cut_2tuple in largest_comm_cut_2tuple_S:
        if min_first > cur_comm_cut_2tuple.first():
            min_first = cur_comm_cut_2tuple.first()
        if max_second < cur_comm_cut_2tuple.second():
            max_second = cur_comm_cut_2tuple.second()

    max_comm_cut_2tuple = TwoTuple([min_first, max_second])

    return max_comm_cut_2tuple
