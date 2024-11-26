"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/25
"""

from simulations.structure import _2TupleTS


def get_complete_asc_order_filtered_2tuple_TS(_2tuple_TS: _2TupleTS) -> _2TupleTS:

    if _2tuple_TS.empty():
        return _2tuple_TS

    if len(_2tuple_TS[0]) == 1:     # todo: 需要检查每一项都是len == 1吗?
        return _2tuple_TS

    sub_2tuple_TS = _2TupleTS([])

    for _2tuple_T in _2tuple_TS:
        is_complete_asc_order = True
        for i in range(len(_2tuple_T) - 1):
            if _2tuple_T[i].second() > _2tuple_T[i + 1].first():
                is_complete_asc_order = False
                break
        if is_complete_asc_order:
            sub_2tuple_TS.add(_2tuple_T)

    return sub_2tuple_TS
