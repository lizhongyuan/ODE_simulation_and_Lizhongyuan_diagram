"""
@brief: PDIE, PDIES, AtomPDIE, AtomPDIES and PDIE_ERROR
@author: ZhongYuan.Li
@date: 2024/11/15
"""
from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.PDIE.pdieS import PDIES
from simulations.expression_tree import expression
from simulations.sameBound import get_distinct_same_bound_2tuple_TSS
from simulations.structure import MySet, _2TupleS, _2TupleSS, _2TupleTS, _2TupleT








# todo: 补充名字
class PDIE(AbstractPDIE):
    def __init__(self,
                 expression: str | None,
                 is_error: bool,
                 is_atom: bool,
                 OP: str | None,
                 meta_PDIES: PDIES,         # todo: 改为factor_PDIES ?
                 DI_2tuple_S: _2TupleS,
                 factor_DI_2tuple_TS: _2TupleTS,
                 #                 expressionIdx: int = 0,    # todo: 应该不需要
                 ):
        super().__init__()

        self._expression = expression
        self._is_error = is_error
        self._is_atom = is_atom
        self._OP = OP
        self._meta_PDIE = meta_PDIES
        self._DI_2tuple_S = DI_2tuple_S
        self._factor_DI_2tuple_TS = factor_DI_2tuple_TS
        self._expression_idx = 0

    def __str__(self):
        format_str = f"PDIE_error"
        if self._is_error:
            return format_str

        format_str =\
            (f"{{\n" +
             f"\texpression: {self._expression},\n" +
             f"\tis_error: {self._is_error},\n" +
             f"\tis_atom: {self._is_atom},\n" +
#             f"\tmeta_PDIE: {str(self._meta_PDIE)},\n" +
             f"\tDI_2tuple_S: {str(self._DI_2tuple_S)}\n" +
             f"}}"
             )
        return format_str

    def getExpression(self) -> str:
        return self._expression

    def isError(self):
        return self._is_error

    def setMetaPDIES(self, metaPDIES: PDIES):
        self._meta_PDIE = metaPDIES

    def setDI2tupleS(self, DI2tupleS: _2TupleS):
        self._DI_2tuple_S = DI2tupleS

    def getDI2tupleS(self):
        return self._DI_2tuple_S

    def get_factor_DI_distinct_same_bound_2tuple_TSS(self): # todo: 改论文
        return get_distinct_same_bound_2tuple_TSS(self._factor_DI_2tuple_TS)


class AtomPDIE(PDIE):
    def __init__(self, expression: str | None, DI_2tuple_S: _2TupleS):

        factor_DI_2tuple_T_list = []
        for DI_2tuple in DI_2tuple_S:
            factor_DI_2tuple_T_list.append(_2TupleT([DI_2tuple]))
        factor_DI_2tuple_TS = _2TupleTS(factor_DI_2tuple_T_list)

        super().__init__(expression=expression,
                         is_error=False,
                         is_atom=True,
                         OP=None,
                         meta_PDIES=PDIES([]),
                         DI_2tuple_S=DI_2tuple_S,
                         factor_DI_2tuple_TS=factor_DI_2tuple_TS)

    def __add__(self, other):
        pass


class PDIE_ERROR(PDIE):
    def __init__(self):
        super().__init__(
                         expression='PDIE_error',
                         is_error=True,
                         is_atom=False,
                         OP=None,
                         meta_PDIES=PDIES([]),
                         DI_2tuple_S=_2TupleS([]),
                         factor_DI_2tuple_TS=_2TupleTS([]))

    def __str__(self):
        return f"PDIE_error"