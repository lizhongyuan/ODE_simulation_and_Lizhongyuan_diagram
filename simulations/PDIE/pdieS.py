"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/20
"""
from typing import List

from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.structure import MySet, _2TupleSS


class PDIES(MySet):
    """
    PDIE Set
    """


    def get_DI_2tuple_SS(self) -> _2TupleSS:
        """
        获取自身的持续区间二元组的集合的集合(Get the "set composed of duration interval 2-tuple sets" of itself)
        Returns:
            (_2TupleSS): 持续区间二元组的集合的集合(set composed of duration interval 2-tuple sets)
        """
        _2tuple_SS = _2TupleSS([])
        for item in self._list:
            _2tuple_SS.add(item.getDI2tupleS())
        return _2tuple_SS

    def setTestList(self, PDIE_list: List[AbstractPDIE]):
        pass


class AtomPDIES(PDIES):
    pass