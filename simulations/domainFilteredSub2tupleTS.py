from simulations.structure import TwoTupleT, TwoTupleTS, TwoTuple


# 定义24的判定函数, 判断_2tuple_T是否是_2tuple_TS在域[A, B]内部的子集(注意:还需要其他条件才能决定是否是域过滤子集)
def Pred_is_2tuple_T_in_Domain(_2tuple_TS: TwoTupleTS, _2tuple_T: TwoTupleT, A: object, B: object) -> bool:

    if not _2tuple_TS.has(_2tuple_T):
        return False

    for item in _2tuple_T:
        if item.first() < A or item.second() > B:
            return False

    return True
