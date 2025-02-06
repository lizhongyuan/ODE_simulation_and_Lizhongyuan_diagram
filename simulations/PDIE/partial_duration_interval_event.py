"""
@brief: PDIE, PDIES, AtomPDIE, AtomPDIES and PDIE_ERROR
@author: ZhongYuan.Li
@date: 2024/11/15
"""
from typing import Tuple

from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.PDIE.partial_duration_interval_event_set import PDIES
from simulations.PDIE._2TupleTS import _2TupleTS
from simulations.PDIE._2TupleS import _2TupleS


class PDIE(AbstractPDIE):
    def __init__(self,
                 p_expression: str | None,
                 p_is_error: bool,
                 p_is_atom: bool,
                 p_OP: str | None,
                 p_meta_PDIE_T: Tuple[AbstractPDIE,...],
                 p_meta_DI_2tuple_TS: _2TupleTS,
                 p_DI_2tuple_S: _2TupleS):
        super().__init__()

        self._expression: str = p_expression   # todo: 可能需要改为operand_tuple
        self._is_error: bool = p_is_error
        self._is_atom: bool = p_is_atom
        self._OP: str = p_OP
        self._meta_PDIE_T: Tuple[AbstractPDIE,...] = p_meta_PDIE_T
        self._meta_DI_2tuple_TS: _2TupleTS = p_meta_DI_2tuple_TS
        self._DI_2tuple_S: _2TupleS = p_DI_2tuple_S


    def __str__(self):
        # format_str: str = f"PDIE_error"
        # if self._is_error:
        #     return format_str

        format_str =\
            (f"{{\n" +
             f"\texpression: {self._expression},\n" +
             f"\tis_error: {self._is_error},\n" +
             f"\tis_atom: {self._is_atom},\n" +
             f"\tmeta_PDIE_T: {'[ ' + ', '.join([meta_PDIE.getExpression() for meta_PDIE in self._meta_PDIE_T]) + ' ]'}\n" +
             f"\tmeta_DI_2tuple_TS: {str(self._meta_DI_2tuple_TS)}\n" +
             f"\tDI_2tuple_S: {str(self._DI_2tuple_S)}\n" +
             f"}}"
             )
        return format_str

    def getExpression(self) -> str | None:
        return self._expression
    def setExpression(self, p_expression: str):
        self._expression = p_expression

    def isError(self):
        return self._is_error

    def setMetaPDIES(self, metaPDIES: PDIES):
        self._meta_PDIE_T = metaPDIES

    def set_meta_DI_2tuple_TS(self, p_meta_DI_2tuple_TS: _2TupleTS):
        self._meta_DI_2tuple_TS = p_meta_DI_2tuple_TS

    def set_DI_2tuple_S(self, DI2tupleS: _2TupleS):
        self._DI_2tuple_S = DI2tupleS

    def get_DI_2tuple_S(self):
        """
        (定义10) 获取一个PDIE instance的DI2TupleS instance
        Returns:
            (_2TupleS)
        """
        return self._DI_2tuple_S

    def __add__(self, other):
        pass


class AtomPDIE(PDIE):
    def __init__(self, p_expression: str | None, p_DI_2tuple_S: _2TupleS):

        super().__init__(p_expression=p_expression,
                         p_is_error=False,
                         p_is_atom=True,
                         p_OP=None,
                         p_meta_PDIE_T=tuple([]),
                         p_meta_DI_2tuple_TS=_2TupleTS([]),
                         p_DI_2tuple_S=p_DI_2tuple_S)


class PDIE_ERROR(PDIE):

    def __init__(self):
        super().__init__(p_expression='',
                         p_is_error=True,
                         p_is_atom=False,
                         p_OP=None,
                         p_meta_PDIE_T=tuple([]),
                         p_meta_DI_2tuple_TS=_2TupleTS([]),
                         p_DI_2tuple_S=_2TupleS([]))

    def __str__(self):
        return super().__str__()
