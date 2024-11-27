"""
@brief: PDIE, PDIES, AtomPDIE, AtomPDIES and PDIE_ERROR
@author: ZhongYuan.Li
@date: 2024/11/15
"""
from simulations.PDIE.AbstractPDIE import AbstractPDIE
from simulations.PDIE.pdieS import PDIES
from simulations.structure import MySet, _2TupleS, _2TupleSS, _2TupleTS, _2TupleT








# todo: 补充名字
class PDIE(AbstractPDIE):
    def __init__(self,
                 p_expression: str | None,
                 p_is_error: bool,
                 p_is_atom: bool,
                 p_OP: str | None,
                 p_meta_PDIE_S: PDIES,
                 p_meta_DI_2tuple_TS: _2TupleTS,
                 p_DI_2tuple_S: _2TupleS,
                 ):
        super().__init__()

        self._expression = p_expression   # todo: 可能需要改为operand_tuple
        self._is_error = p_is_error
        self._is_atom = p_is_atom
        self._OP = p_OP
        self._meta_PDIE_S = p_meta_PDIE_S
        self._meta_DI_2tuple_TS = p_meta_DI_2tuple_TS
        self._DI_2tuple_S = p_DI_2tuple_S


    def __str__(self):
        format_str: str = f"PDIE_error"
        if self._is_error:
            return format_str

        format_str =\
            (f"{{\n" +
             f"\texpression: {self._expression},\n" +
             f"\tis_error: {self._is_error},\n" +
             f"\tis_atom: {self._is_atom},\n" +
#             f"\tmeta_PDIE: {str(self._meta_PDIE)},\n" +
             f"\tmeta_DI_2tuple_TS: {str(self._meta_DI_2tuple_TS)}\n" +
             f"\tDI_2tuple_S: {str(self._DI_2tuple_S)}\n" +
#             f"\tfactor_DI_2tuple_TS: {str(self._factor_DI_2tuple_TS)}\n" +
#             f"\tdistinct_same_bound_2tuple_TSS: {str(self.get_factor_DI_distinct_same_bound_2tuple_TSS())}\n" +
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
        self._meta_PDIE_S = metaPDIES

    def set_meta_DI_2tuple_TS(self, p_meta_DI_2tuple_TS: _2TupleTS):
        self._meta_DI_2tuple_TS = p_meta_DI_2tuple_TS

    def set_DI_2tuple_S(self, DI2tupleS: _2TupleS):
        self._DI_2tuple_S = DI2tupleS

    def get_DI_2tuple_S(self):
        return self._DI_2tuple_S

    def __add__(self, other):
        pass


class AtomPDIE(PDIE):
    def __init__(self, p_expression: str | None, p_DI_2tuple_S: _2TupleS):

        super().__init__(p_expression=p_expression,
                         p_is_error=False,
                         p_is_atom=True,
                         p_OP=None,
                         p_meta_PDIE_S=PDIES([]),
                         p_meta_DI_2tuple_TS=_2TupleTS([]),
                         p_DI_2tuple_S=p_DI_2tuple_S)


class PDIE_ERROR(PDIE):
    def __init__(self, p_expression: str | None):
        super().__init__(p_expression=p_expression,
                         p_is_error=True,
                         p_is_atom=False,
                         p_OP=None,
                         p_meta_PDIE_S=PDIES([]),
                         p_meta_DI_2tuple_TS=_2TupleTS([]),
                         p_DI_2tuple_S=_2TupleS([]))

    def __str__(self):
        return f"PDIE_error"