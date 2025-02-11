"""
@file partial_duration_interval_event_set.py
@brief: PDIES & AtomPDIES.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from typing import List, Tuple, Any
from simulations.PDIE.abstract_PDIE import AbstractPDIE
from simulations.structure import LiZhongYuanSet
from simulations.PDIE._2Tuple_SS import _2TupleSS
from simulations.PDIE._2Tuple_TS import _2TupleTS
from simulations.PDIE.cartesian_product import f_CP_of_2tuple_SS
from simulations.PDIE.unfeasible import get_custom_ordered_wildcard_unfeasible_2tuple_TS


class PDIES(LiZhongYuanSet):
    """
    PDIE set class
    """

    def __init__(self, p_set_list: list):
        super().__init__(p_set_list)
        self._unfeasible_PDIE_tuple = None
        self._wildcard_unfeasible_DI_2tuple_TS = None


    def __str__(self):

        dict_str: str = self._get_dict_str()

        format_str: str = \
            (f"{{\n" +
             f"\tdict: {dict_str},\n" +
             f"}}"
             )
        return format_str


    def __len__(self):
        return len(self._list)


    def _get_dict_str(self) -> str:
        dict_str: str = f"{{ "
        for i in range(len(self._dict.keys())):
            key: any = list(self._dict.keys())[i]
            dict_str += f"{key}: {self._dict[key].getExpression()}"
            if i != len(self._dict.keys()) - 1:
                dict_str += ", "
        dict_str += f" }}"

        return dict_str


    def get_dict_key(self, p_pdie: AbstractPDIE) -> str | None:
        for key in list(self._dict.keys()):
            if self._dict[key] == p_pdie:
                return key
        return None


    def f_DI_2tuple_SS(self) -> _2TupleSS:
        """
        (定义11)Get the "set composed of duration interval 2-tuple's sets" of itself

        Returns:
            (_2TupleSS): Set composed of duration interval 2-tuple's sets
        """

        DI_2tuple_SS: _2TupleSS = _2TupleSS()

        for item in self._list:
            DI_2tuple_SS.add(item.f_DI_2tuple_S())

        return DI_2tuple_SS


    def set_wildcard_unfeasible_DI_2tuple_info(self,
                                               p_wildcard_unfeasible_DI_2tuple_TS: _2TupleTS,
                                               p_PDIE_tuple: Tuple[AbstractPDIE,...]) -> None:
        """
        Set _wildcard_unfeasible_DI_2tuple_TS and _unfeasible_PDIE_tuple.

        Args:
            (p_wildcard_unfeasible_DI_2tuple_TS): Wildcard unfeasible DI2TupleTS instance
            (p_PDIE_tuple): A PDIE instance tuple

        Returns:
            None
        """

        for _2tuple_T in p_wildcard_unfeasible_DI_2tuple_TS:
            if len(_2tuple_T) != len(p_PDIE_tuple):
                raise ValueError(f"Wrong wildcard unfeasible DI 2tuple info")

            for i in range(len(_2tuple_T)):
                if _2tuple_T[i] == '*':
                    continue
                pdie: AbstractPDIE = p_PDIE_tuple[i]
                if _2tuple_T[i] not in pdie.f_DI_2tuple_S():
                    raise ValueError(f"Wrong wildcard unfeasible DI 2tuple info")

        self._wildcard_unfeasible_DI_2tuple_TS = p_wildcard_unfeasible_DI_2tuple_TS
        self._unfeasible_PDIE_tuple = p_PDIE_tuple


    def get_custom_ordered_CP_of_DI_2tuple_SS(self,
                                              p_DI_2tuple_SS: _2TupleSS,
                                              p_op_idx_T: Tuple[int,...] | None) -> _2TupleTS:
        """
        获取p_op_idx_T作为表达式操作数索引顺序的, 集合内所有元素的DI2TupleS的笛卡尔积.
        如果p_op_idx_T为None, 表达式操作数索引顺序为(1, 2, 3, ..., n)
        Args:
            p_DI_2tuple_SS:
            p_op_idx_T: 笛卡尔积表达式运算数的索引顺序元组 或者 None

        Returns:
            _2TupleSS: 集合所有元素的DI2TupleS的笛卡尔积
        """

        # ---------- 1 None参数处理和参数检查----------

        default_idx_T: tuple[int,...] = tuple(range(1, len(self._list) + 1))
        if p_op_idx_T is None:
            p_op_idx_T = default_idx_T
        else:
            sorted_idx_T: Tuple[int,...] = tuple(sorted(p_op_idx_T))
            if sorted_idx_T != default_idx_T:
                raise ValueError("Wrong p_op_idx_T !")

        # ---------- 2 获取p_op_idx_T作为表达式操作数索引顺序的, 集合内所有元素的DI2TupleS的笛卡尔积 ----------

        _2tuple_TS: _2TupleTS = f_CP_of_2tuple_SS(p_2tuple_SS=p_DI_2tuple_SS,
                                                  p_opr_idx_T=p_op_idx_T)

        return _2tuple_TS


    def get_custom_ordered_wildcard_unfeasible_DI_2tuple_TS(self,
                                                            p_op_idx_T: tuple[Any,...]) -> _2TupleTS:
        """
        todo:
        Args:
            p_op_idx_T:

        Returns:

        """

        unfeasible_DI_idx_list: List[any] = []

        for unfeasible_PDIE in self._unfeasible_PDIE_tuple:
            cur_idx: any = self.get_dict_key(unfeasible_PDIE)
            if cur_idx is None:
                return _2TupleTS()
            unfeasible_DI_idx_list.append(cur_idx)

        wildcard_unfeasible_DI_2tuple_TS: _2TupleTS \
            = get_custom_ordered_wildcard_unfeasible_2tuple_TS(p_op_idx_T=p_op_idx_T,
                                                               p_wildcard_unfeasible_2tuple_TS=self._wildcard_unfeasible_DI_2tuple_TS,
                                                               p_wildcard_unfeasible_idx_T=tuple(unfeasible_DI_idx_list))

        return wildcard_unfeasible_DI_2tuple_TS


class AtomPDIES(PDIES):
    pass
