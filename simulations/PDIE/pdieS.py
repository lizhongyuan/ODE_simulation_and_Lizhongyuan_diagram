"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/20
"""
from locale import format_string
from typing import List, Tuple

from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.function import get_CP_of_2tuple_SS
from simulations.structure import MySet, _2TupleSS, _2TupleTS, _2TupleS
from simulations.unfeasible import get_feasible_DI_2tuple_TS, get_op_ordered_unfeasible_DI_2tuple_TS


def get_feasible_DI_2tuple_TS2(op_ordered_unfeasible_DI_2tuple_TS: _2TupleTS,
                               op_ordered_CP_of_2tuple_SS: _2TupleTS) -> _2TupleTS:
    # 3 ---------- 构造合法的二元组的元组的集合 ----------

    feasible_DI_2tuple_TS = _2TupleTS([])
    for _2tuple_T in op_ordered_CP_of_2tuple_SS:
        # 3.1 如果在op_ordered_unfeasible_DI_2tuple_TS, 则_2tuple_T非法, continue
        if _2tuple_T in op_ordered_unfeasible_DI_2tuple_TS:
            continue

        # 3.2 如果通配在op_ordered_unfeasible_DI_2tuple_TS, continue
        wildcard_matched = False
        for op_ordered_unfeasible_DI_2tuple_T in op_ordered_unfeasible_DI_2tuple_TS:
            if _2tuple_T.wildcard_match(op_ordered_unfeasible_DI_2tuple_T):
                wildcard_matched = True
                break
        if wildcard_matched:
            continue

        # 3.3 合法, 加入到feasible_DI_2tuple_TS
        feasible_DI_2tuple_TS.add(_2tuple_T)

    # 4 ---------- 返回结果 ----------

    return feasible_DI_2tuple_TS


class PDIES(MySet):
    """
    PDIE Set
    """

    def __init__(self, setList: list):
        super().__init__(setList)
        self._unfeasible_PDIE_tuple = None
        self._unfeasible_DI_2tuple_TS = None

    def __str__(self):

        dict_str = self._get_dict_str()

        format_str = \
            (f"{{\n" +
             f"\tdict: {dict_str},\n" +
             # f"\tis_error: {self._is_error},\n" +
             # f"\tis_atom: {self._is_atom},\n" +
             # #             f"\tmeta_PDIE: {str(self._meta_PDIE)},\n" +
             # f"\tDI_2tuple_S: {str(self._DI_2tuple_S)}\n" +
             # f"\tfactor_DI_2tuple_TS: {str(self._factor_DI_2tuple_TS)}\n" +
             # f"\tdistinct_same_bound_2tuple_TSS: {str(self.get_factor_DI_distinct_same_bound_2tuple_TSS())}\n" +
             f"}}"
             )
        return format_str

    def _get_dict_str(self) -> str:
        dict_str = f"{{ "
        for i in range(len(self._dict.keys())):
            key = list(self._dict.keys())[i]
            dict_str += f"{key}: {self._dict[key].getExpression()}"
            if i != len(self._dict.keys()) - 1:
                dict_str += ", "
        dict_str += f" }}"

        return dict_str

    def show_dict(self) -> None:
        print(self._get_dict_str())

    def get_dict_key(self, p_PDIE: AbstractPDIE) -> str | None:
        for key in list(self._dict.keys()):
            if self._dict[key] == p_PDIE:
                return key
        return None

    def get_DI_2tuple_SS(self) -> _2TupleSS:
        """
        获取自身的持续区间二元组的集合的集合(Get the "set composed of duration interval 2-tuple sets" of itself)
        Returns:
            (_2TupleSS): 持续区间二元组的集合的集合(set composed of duration interval 2-tuple sets)
        """
        _2tuple_SS = _2TupleSS([])
        for item in self._list:
            _2tuple_SS.add(item.get_DI_2tuple_S())
        return _2tuple_SS

    def get_unfeasible_asc_DI_2tuple_TS(self):
        pass
    def set_unfeasible_asc_DI_2tuple_TS(self, unfeasible_asc_DI_2tuple_TS: _2TupleTS):
        pass

    def set_unfeasible_DI_2tuple_info(self,
                                      unfeasible_DI_2tuple_TS: _2TupleTS,
                                      unfeasible_PDIE_tuple: Tuple[AbstractPDIE,...]):
        """

        Args:
            unfeasible_DI_2tuple_TS:
            unfeasible_PDIE_tuple:

        Returns:

        """
        for _2tuple_T in unfeasible_DI_2tuple_TS:
            if len(_2tuple_T) != len(unfeasible_PDIE_tuple):
                raise ValueError(f"Wrong unfeasible DI 2tuple info")
            for i in range(len(_2tuple_T)):
                cur_tuple = _2tuple_T[i]
                if cur_tuple == '*':
                    continue
                cur_PDIE = unfeasible_PDIE_tuple[i]
                if cur_tuple not in cur_PDIE.get_DI_2tuple_S():
                    raise ValueError(f"Wrong unfeasible DI 2tuple info")

        self._unfeasible_DI_2tuple_TS = unfeasible_DI_2tuple_TS
        self._unfeasible_PDIE_tuple = unfeasible_PDIE_tuple

    # def get_unfeasible_DI_2tuple_info(self):
    #     return self._unfeasible_PDIE_tuple, self._unfeasible_DI_2tuple_TS

    def get_CP_of_DI_2tuple_SS(self, p_op_idx_T: Tuple[int, ...] | None) -> _2TupleTS:
        """
        按照p_op_idx_T的顺序获取集合元素的DI2TupleS的笛卡尔积,
        如果p_op_idx_T为None, 顺序为默认索引元组(1, 2, 3, ..., n)
        Args:
            p_op_idx_T: 笛卡尔积表达式运算数的索引顺序元组

        Returns:
            集合元素的DI2TupleS的笛卡尔积
        """

        default_idx_T = tuple(range(1, len(self._list) + 1))
        if p_op_idx_T is None:
            p_op_idx_T = default_idx_T
        else:
            sorted_idx_T = tuple(sorted(p_op_idx_T))
            if sorted_idx_T != default_idx_T:
                raise ValueError("Wrong p_op_idx_T !")

        DI_2tuple_SS = self.get_DI_2tuple_SS()
        _2tuple_TS = get_CP_of_2tuple_SS(DI_2tuple_SS, p_op_idx_T)

        return _2tuple_TS


    # todo: 增加定义16, 使用get_unfeasible_DI_2tuple_TS补充
    def get_wildcard_unfeasible_DI_2tuple_TS(self, p_op_idx_T: tuple[int,...]) -> _2TupleTS:

        unfeasible_DI_idx_list = []

        for unfeasible_PDIE in self._unfeasible_PDIE_tuple:
            cur_idx = self.get_dict_key(unfeasible_PDIE)
            if cur_idx is None:
                return _2TupleTS([])
            unfeasible_DI_idx_list.append(cur_idx)

        return get_op_ordered_unfeasible_DI_2tuple_TS(self._unfeasible_DI_2tuple_TS,
                                                      p_op_idx_T,
                                                      tuple(unfeasible_DI_idx_list))

    # todo: S2放到这
    def get_largest_comm_cut_2tuple_S2(self, p_2tuple_TS: _2TupleTS) -> _2TupleS:
        pass


class AtomPDIES(PDIES):
    pass