"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/20
"""
from locale import format_string
from typing import List, Tuple

from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.function import get_CP_of_2tuple_SS
from simulations.structure import MySet, _2TupleSS, _2TupleTS


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

    def get_unfeasible_DI_2tuple_TS(self, p_idx_T: Tuple[int,...]):
        """
        获取p_idx_T顺序下的不可能DI的二元组的元组的集合
        Args:
            p_idx_T: 一个索引号元组

        Returns:
            p_idx_T顺序下的不可能DI的二元组的元组的集合
        """
        pass
    def set_unfeasible_DI_2tuple_info(self,
                                      unfeasible_DI_2tuple_TS: _2TupleTS,
                                      unfeasible_PDIE_tuple: Tuple[AbstractPDIE, ...]):
        self._unfeasible_DI_2tuple_TS = unfeasible_DI_2tuple_TS
        self._unfeasible_PDIE_tuple = unfeasible_PDIE_tuple

    def get_unfeasible_DI_2tuple_info(self):
        return self._unfeasible_PDIE_tuple, self._unfeasible_DI_2tuple_TS

    def get_CP_of_DI_2tuple_SS(self, p_idx_T: Tuple[int, ...] | None) -> _2TupleTS:
        """

        Args:
            p_idx_T:

        Returns:

        """

        default_idx_T = tuple(range(1, len(self._list) + 1))
        if p_idx_T is None:
            p_idx_T = default_idx_T
        else:
            sorted_idx_T = tuple(sorted(p_idx_T))
            if sorted_idx_T != default_idx_T:
                raise ValueError("p_idx_T error")

        DI_2tuple_SS = self.get_DI_2tuple_SS()
        _2tuple_TS = get_CP_of_2tuple_SS(DI_2tuple_SS, p_idx_T)

        return _2tuple_TS


class AtomPDIES(PDIES):
    pass