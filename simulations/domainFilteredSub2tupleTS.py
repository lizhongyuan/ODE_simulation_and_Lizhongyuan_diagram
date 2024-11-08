from simulations.structure import TwoTupleT, TwoTupleTS, TwoTuple
from simulations.twoTupleT import get_min_1_of_2tuple_T, get_max_2_of_2tuple_T


# 定义24的判定函数, 判断_2tuple_T是否是_2tuple_TS在域[A, B]内部的子集(注意:还需要其他条件才能决定是否是域过滤子集)
def Pred_is_2tuple_T_in_Domain(_2tuple_TS: TwoTupleTS, _2tuple_T: TwoTupleT, A: object, B: object) -> bool:

    if not _2tuple_TS.has(_2tuple_T):
        return False

    for item in _2tuple_T:
        if item.first() < A or item.second() > B:
            return False

    return True

# 定义24, 求一个2tupleTS在域[A, B]的域过滤子集
def get_domain_filtered_sub_2tuple_TS(_2tuple_TS: TwoTupleTS, A: object, B: object) -> TwoTupleTS | None:
    _2tuple_TS_list = _2tuple_TS.list()
    _2tuple_T_list = []
    has_A_left = False
    has_B_right = False

    for _2tuple_T in _2tuple_TS_list:
        if not Pred_is_2tuple_T_in_Domain(_2tuple_TS, _2tuple_T, A, B):
            continue

        _2tuple_T_list.append(_2tuple_T)
        if not has_A_left and get_min_1_of_2tuple_T(_2tuple_T) == A:
            has_A_left = True
        if not has_B_right and get_max_2_of_2tuple_T(_2tuple_T) == B:
            has_B_right = True

    if has_A_left and has_B_right:
        return TwoTupleTS(_2tuple_T_list)

    return None
