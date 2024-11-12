from simulations.structure import _2TupleT, _2TupleTS, _2Tuple
from simulations.twoTupleT import get_min_1st_of_2tuple_T, get_max_2nd_of_2tuple_T


# 定义24的判定函数, 判断_2tuple_T是否是_2tuple_TS在域[A, B]内部的子集(注意:还需要其他条件才能决定是否是域过滤子集)
def Pred_is_2tuple_T_in_Domain(_2tuple_TS: _2TupleTS, _2tuple_T: _2TupleT, A: object, B: object) -> bool:

    if not _2tuple_TS.has(_2tuple_T):
        return False

    for item in _2tuple_T:
        if item.first() < A or item.second() > B:
            return False

    return True


# 定义24, 求一个2tupleTS在域[A, B]的域过滤子集
def get_domain_filtered_sub_2tuple_TS(_2tuple_TS: _2TupleTS, A: object, B: object) -> _2TupleTS | None:
    """
    求一个2tupleTS在域[A, B]的域过滤子集(定义24)
    :param _2tuple_TS: 一个二元组的元组的集合
    :param A: 过滤域的左边界
    :param B: 过滤域的右边界
    :return:
    """

    sub_2tuple_TS = _2TupleTS([])
    has_A_left = False
    has_B_right = False

    for _2tuple_T in _2tuple_TS:
        if not Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T, A, B):
            continue

        sub_2tuple_TS.add(_2tuple_T)

        if not has_A_left and get_min_1st_of_2tuple_T(_2tuple_T) == A:
            has_A_left = True
        if not has_B_right and get_max_2nd_of_2tuple_T(_2tuple_T) == B:
            has_B_right = True

    if has_A_left and has_B_right:
        return sub_2tuple_TS

    return _2TupleTS([])



def Pred_is_domain_filter_2tuple_T(p_2tuple_TS: _2TupleTS, p_2tuple: _2Tuple) -> bool:
    """
    (定义25)Predicate, 判定p_2tuple是否是p_2tuple_TS的域过滤二元组
    Args:
        p_2tuple_TS (_2TupleTS): 一个二元组集合
        p_2tuple (_2Tuple): 一个二元组

    Returns:
        bool: 判定结果
    """

    left = p_2tuple.first()
    right = p_2tuple.second()

    if get_domain_filtered_sub_2tuple_TS(p_2tuple_TS, left, right):
        return True

    return False

# todo: 定义25, 家里电脑

