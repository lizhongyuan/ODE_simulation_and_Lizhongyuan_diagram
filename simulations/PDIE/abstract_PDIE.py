"""
@file abstract_PDIE.py
@brief: AbstractPDIE class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from simulations.PDIE._2Tuple_S import _2TupleS
from simulations.PDIE._2Tuple_TS import _2TupleTS


class AbstractPDIE:
    """
    An abstract class that defines the interface for PDIE
    """

    def f_DI_2tuple_S(self) -> _2TupleS:
        pass

    def f_meta_DI_2tuple_TS(self) -> _2TupleTS:
        pass

    def getExpression(self) -> str:
        pass
