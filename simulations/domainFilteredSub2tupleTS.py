from typing import Any

from simulations.PDIE._2TupleT import _2TupleT, f_min_1_of_2tuple_T, f_max_2_of_2tuple_T
from simulations.PDIE._2TupleTS import _2TupleTS
#from simulations.twoTupleT import f_min_1_of_2tuple_T, f_max_2_of_2tuple_T


# 定义24的判定函数, 判断_2tuple_T是否是_2tuple_TS在域[A, B]内部的子集(注意:还需要其他条件才能决定是否是域过滤子集)
def Pred_is_2tuple_T_in_Domain(p_2tuple_TS: _2TupleTS, p_2tuple_T: _2TupleT, p_left: Any, p_right: Any) -> bool:

    if not p_2tuple_TS.has(p_2tuple_T):
        return False

    for item in p_2tuple_T:
        if item.first() < p_left or item.second() > p_right:
            return False

    return True


# todo: 移动到加法
# 定义24, 求一个2tupleTS在域[A, B]的域过滤子集
def get_domain_filtered_sub_2tuple_TS(p_2tuple_TS: _2TupleTS, p_left: Any, p_right: Any) -> _2TupleTS:
    """
    求一个2tupleTS在域[A, B]的域过滤子集(定义24)
    :param p_2tuple_TS: 一个二元组的元组的集合
    :param p_left: 过滤域的左边界
    :param p_right: 过滤域的右边界
    :return:
    """

    sub_2tuple_TS = _2TupleTS([])
    has_A_left = False
    has_B_right = False

    for _2tuple_T in p_2tuple_TS:
        if not Pred_is_2tuple_T_in_Domain(p_2tuple_TS, _2tuple_T, p_left, p_right):
            continue

        sub_2tuple_TS.add(_2tuple_T)

        if not has_A_left and f_min_1_of_2tuple_T(_2tuple_T) == p_left:
            has_A_left = True
        if not has_B_right and f_max_2_of_2tuple_T(_2tuple_T) == p_right:
            has_B_right = True

    if has_A_left and has_B_right:
        return sub_2tuple_TS

    return _2TupleTS([])
