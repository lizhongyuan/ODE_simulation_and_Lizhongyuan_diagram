from typing import Any

from simulations.PDIE._2TupleT import _2TupleT, f_min_1_of_2tuple_T, f_max_2_of_2tuple_T
from simulations.PDIE._2TupleTS import _2TupleTS
#from simulations.twoTupleT import f_min_1_of_2tuple_T, f_max_2_of_2tuple_T


# 定义24的判定函数, 判断_2tuple_T是否是_2tuple_TS在域[A, B]内部的子集(注意:还需要其他条件才能决定是否是域过滤子集)
def Pred_is_2tuple_T_in_Domain(p_2tuple_TS: _2TupleTS,
                               p_2tuple_T: _2TupleT,
                               p_left: object,
                               p_right: object) -> bool:


    if not p_2tuple_TS.has(p_2tuple_T):
        return False

    for item in p_2tuple_T:
        if item.first() < p_left or item.second() > p_right:
            return False

    return True


# todo: 移动到加法
def f_domain_filtered_sub_2tuple_TS(p_2tuple_TS: _2TupleTS,
                                    p_left: object,
                                    p_right: object) -> _2TupleTS:
    """
    (定义18)Get the domain filtered subset of a 2TupleTS instance in a domain

    Args:
        p_2tuple_TS (_2TupleTS): A 2TupleTS instance
        p_left (object): The left border of a domain
        p_right (object): The right border of a domain

    Returns:
        (_2TupleTS): The domain filtered subset
    """

    sub_2tuple_TS = _2TupleTS([])
    exists_1st_equal_to_left = False
    exists_2nd_equal_to_right = False

    for _2tuple_T in p_2tuple_TS:
        if not Pred_is_2tuple_T_in_Domain(p_2tuple_TS, _2tuple_T, p_left, p_right):
            continue

        sub_2tuple_TS.add(_2tuple_T)

        if not exists_1st_equal_to_left and f_min_1_of_2tuple_T(_2tuple_T) == p_left:
            exists_1st_equal_to_left = True
        if not exists_2nd_equal_to_right and f_max_2_of_2tuple_T(_2tuple_T) == p_right:
            exists_2nd_equal_to_right = True

    if exists_1st_equal_to_left and exists_2nd_equal_to_right:
        return sub_2tuple_TS

    return _2TupleTS([])
