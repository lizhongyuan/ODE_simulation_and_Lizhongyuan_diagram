# cut2tupleS
# 
#

from simulations.structure import TwoTuple, TwoTupleSS, TwoTupleT, TwoTupleTS
from simulations.structure import TwoTupleS
from collections import OrderedDict

##
# is_cut_2tuple函数实现, 判断二元组_2tuple是否是p_2tupleS的一个切割二元组
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

    ### ---------- 1 获取所有的第一项和第二项 ----------

    first_list = []
    second_list = []

    for cur_2tuple_S in p_2tuple_SS:
        for cur_2tuple in cur_2tuple_S:
            first_list.append(cur_2tuple.first())
            second_list.append(cur_2tuple.second())

    first_list = list(OrderedDict.fromkeys(first_list))
    second_list = list(OrderedDict.fromkeys(second_list))

    largest_comm_cut_2tuple_S_list = []

    ### ---------- 2 所有的第一项和第二项, 构造二元组, 检查是否是切割二元组, 并添加到列表 ----------
    for cur_first in first_list:
        for cur_second in second_list:

            # 2.1 跳过不合法的二元组
            if cur_first >= cur_second:
                continue

            # 2.2 跳过重复的二元组
            cur_2tuple = TwoTuple([cur_first, cur_second])
            if cur_2tuple in largest_comm_cut_2tuple_S_list:
                continue

            # 2.3 检查是否是p_2tuple_SS每个元素的切割二元组, 如果是则插入列表
            res = True
            for cur_2tuple_S in p_2tuple_SS:
                if not is_cut_2tuple(cur_2tuple_S, cur_2tuple):
                    res = False
                    break

            if res:
                largest_comm_cut_2tuple_S_list.append(cur_2tuple)

    largest_comm_cut_2tuple_S = TwoTupleS(largest_comm_cut_2tuple_S_list)

    return largest_comm_cut_2tuple_S


### fMaxCommCutTwoT 求最大公共切割二元组, todo: 检查论文是否有错
def get_max_comm_cut_2tuple(p_2tuple_SS: TwoTupleSS):
    pass