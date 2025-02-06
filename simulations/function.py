from typing import List, Tuple

from simulations.structure import _2Tuple, _2TupleT, _2TupleTS
from simulations.PDIE._2TupleS import _2TupleS
from simulations.PDIE._2TupleSS import _2TupleSS





def f_CP_of_2tuple_SS(p_2tuple_SS: _2TupleSS,
                      p_opr_idx_T: Tuple[int,...]) -> _2TupleTS:
    """
    (定义14)Let set p_2tuple_SS = { p_2tuple_S_1, p_2tuple_S_2, p_2tuple_S_3, ... , p_2tuple_S_n },
    and p_idx_T = [ p_idx_1, p_idx_2, p_idx_3, ..., p_idx_n ].
    get cartesian product with expression p_2tuple_S_(p_idx_1) * p_2tuple_S_(p_idx_2) * p_2tuple_S_(p_idx_3) * ... * p_2tuple_S_(p_idx_n)
    Args:
        p_2tuple_SS (_2TupleSS): A set whose elements are sets of 2-tuples
        p_opr_idx_T (Tuple[int,...]): A tuple representing the index order of operands

    Returns:
        (_2TupleTS): cartesian product
    """

    _2tuple_list_list = get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS, p_opr_idx_T, 1)

    _2tuple_T_list = []
    for _2tuple_list in _2tuple_list_list:
        _2tuple_T = _2TupleT(_2tuple_list)
        _2tuple_T_list.append(_2tuple_T)

    _2tuple_TS: _2TupleTS = _2TupleTS(_2tuple_T_list)

    return _2tuple_TS


def get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS: _2TupleSS,
                                             p_opr_idx_T: Tuple[int,...],
                                             p_starting_pivot: int) -> List[List[_2Tuple]]:
    """
    获取一个2TupleSS instance的所有members从某个索引号开始的以某种索引顺序进行的笛卡尔积(索引号从1开始计数)
    Args:
        p_2tuple_SS (_2TupleSS): A set whose elements are sets of 2-tuples
        p_opr_idx_T (Tuple[any,...]): A tuple representing the index order of operands
        p_starting_pivot (int): p_opr_idx_T第一个进行笛卡尔积运算的元素的索引号

    Returns (List[List[_2Tuple]]):
        笛卡尔积结果的List[List[_2Tuple]]形式表示
    """

    # 获取p_starting_pivot在p_2tuple_SS对应的的元素cur_2tuple_S
    cur_starting_idx: int = p_opr_idx_T[p_starting_pivot - 1] - 1
    cur_2tuple_S: _2TupleS = p_2tuple_SS[cur_starting_idx]

    # 初始化本次递归的结果为[]
    cur_2tuple_list_list: List[List[_2Tuple]] = []

    # 本次递归是最后一趟的情况, 使用cur_2tuple_S构造结果, 然后返回
    if p_starting_pivot == len(p_opr_idx_T):
        for _2tuple in cur_2tuple_S:
                cur_2tuple_list_list.append([ _2tuple ])
        return cur_2tuple_list_list

    # 获取后一趟递归的结果post_2tuple_list_list
    post_2tuple_list_list: List[List[_2Tuple]] = \
        get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS=p_2tuple_SS,
                                                 p_opr_idx_T=p_opr_idx_T,
                                                 p_starting_pivot=p_starting_pivot + 1)

    # 使用post_2tuple_list_list和cur_2tuple_S构造结果
    for _2tuple in cur_2tuple_S:
        for post_2tuple_list in post_2tuple_list_list:
            _2tuple_list: List[_2Tuple] = [ _2tuple ] + post_2tuple_list
            cur_2tuple_list_list.append(_2tuple_list)

    return cur_2tuple_list_list


def get_bound_2tuple(p_2tupleT: _2TupleT) -> _2Tuple | None:
    """
    (定义28)获取长度有限的二元组的元组的边界二元组
    Args:
        p_2tupleT (_2TupleT):

    Returns:
        (_2Tuple):
    """

    if p_2tupleT is None:
        return None

    min_first = p_2tupleT[0].first()
    max_second = p_2tupleT[0].second()

    for item in p_2tupleT.list():
        if min_first > item.first():
            min_first = item.first()
        if max_second < item.second():
            max_second = item.second()

    return _2Tuple([min_first, max_second])


def get_bound_2tuple_S(p_2tupleT_S: _2TupleTS) -> _2TupleS | None:
    """
    获取二元组的元组的集合p_2tupleT_S的边界二元组集合
    Args:
        p_2tupleT_S (_2TupleTS): 二元组的元组的集合

    Returns:
        (_2TupleS) p_2tupleT_S的边界二元组集合
    """

    if p_2tupleT_S is None:
        return None

    bound_2tuple_S_list = []
    bound_2tuple_map = set()
    for cur_2tupleT in p_2tupleT_S.list():
        cur_bound_2tuple = get_bound_2tuple(cur_2tupleT)
        if cur_bound_2tuple.instance() not in bound_2tuple_map:
            bound_2tuple_S_list.append(_2Tuple(cur_bound_2tuple.list()))
            bound_2tuple_map.add(cur_bound_2tuple.instance())

    return _2TupleS(bound_2tuple_S_list)
