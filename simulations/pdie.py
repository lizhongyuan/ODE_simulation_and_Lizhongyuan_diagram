from locale import format_string

from simulations.structure import MySet, _2TupleS


class PDIES(MySet):
    pass


class PDIE:
    def __init__(self,
                 is_atom: bool,
                 meta_PDIES: PDIES,
                 DI_2tuple_S: _2TupleS,
                 #                 expressionIdx: int = 0,    # todo: 应该不需要
                 ):
        self._is_atom = is_atom
        self._meta_PDIE = meta_PDIES
        self._DI_2tuple_S = DI_2tuple_S
        self._expression_idx = 0

    def __str__(self):
        format_str =\
            (f"{{\n" +
             f"\tis_atom: {self._is_atom},\n" +
             f"\tmeta_PDIE: {str(self._meta_PDIE)},\n" +
             f"\tDI_2tuple_S: {str(self._DI_2tuple_S)}\n" +
             f"}}"
             )
        return format_str

    def setMetaPDIES(self, metaPDIES: PDIES):
        self._meta_PDIE = metaPDIES

    def setDI2tupleS(self, DI2tupleS: _2TupleS):
        self._DI_2tuple_S = DI2tupleS

    def getDI2tupleS(self):
        return self._DI_2tuple_S

    # def print(self):
    #     print("print")
    #

#
# pdie = PDIE(isAtom=True,
#             metaPDIES=None,
#             DI2tupleS=None)
