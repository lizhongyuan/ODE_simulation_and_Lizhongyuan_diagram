from locale import format_string

from simulations.structure import MySet, _2TupleS, _2TupleSS


class PDIES(MySet):

    def get_DI_2tuple_SS(self) -> _2TupleSS:
        _2tuple_SS = _2TupleSS([])
        for item in self._list:
            _2tuple_SS.add(item.getDI2tupleS())
        return _2tuple_SS



class AtomPDIES(PDIES):
    # def get_DI_2tuple_SS(self) -> _2TupleSS:
    #     _2tuple_SS = _2TupleSS([])
    #     for item in self._list:
    #         _2tuple_SS.add(item.getDI2tupleS())
    #     return _2tuple_SS
    pass


# todo: 补充名字
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
#             f"\tmeta_PDIE: {str(self._meta_PDIE)},\n" +
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


class AtomPDIE(PDIE):
    def __init__(self, DI_2tuple_S: _2TupleS):
        super().__init__(is_atom=True,
                         meta_PDIES=PDIES([]),
                         DI_2tuple_S=DI_2tuple_S)

    def __add__(self, other):
        pass

    # def print(self):
    #     print("print")
    #

