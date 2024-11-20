"""
@brief: Brief description of the class.
@author: Your Name
@date: 2024/11/20
"""

class AbstractPDIE:
    def __init__(self,
                 expression: str | None,
                 is_error: bool,
                 is_atom: bool,
                 OP: str | None,
                 # meta_PDIES: PDIES,
                 # DI_2tuple_S: _2TupleS,
                 # factor_DI_2tuple_TS: _2TupleTS,
                 ):
        pass

    def __str__(self):
        pass

    def getExpression(self) -> str:
        pass

    def isError(self) -> bool:
        pass
    #
    # def setMetaPDIES(self, metaPDIES: PDIES):
    #     self._meta_PDIE = metaPDIES
    #
    # def setDI2tupleS(self, DI2tupleS: _2TupleS):
    #     self._DI_2tuple_S = DI2tupleS
    #
    # def getDI2tupleS(self):
    #     pass
    #
    # def get_factor_DI_distinct_same_bound_2tuple_TSS(self): # todo: 改论文
    #     pass