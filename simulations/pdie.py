import json

from simulations.structure import MySet


class PDIE:
    def __init__(self,
                 isAtom: bool,
                 metaPDIES,
                 DI2tupleS,
                 expressionIdx = 0,
                 ):
        self._isAtom = isAtom
        self._metaPDIE = metaPDIES
        self._DI2tupleS = DI2tupleS
        self._expressionIdx = expressionIdx

    def setMetaPDIES(self, metaPDIES):
        self._metaPDIE = metaPDIES

    def setDI2tupleS(self, DI2tupleS):
        self._DI2tupleS = DI2tupleS

    def getDI2tupleS(self):
        return set(self._DI2tupleS)

    def print(self):
        print("print")

class PDIES(MySet):

    def set_unfeasible(self, unfeasible_info):
        self._unfeasible_info = unfeasible_info


pdie = PDIE(isAtom=True,
            metaPDIES=None,
            DI2tupleS=None)

# DI2tupleS = list()
# DI2tupleS.append((0, 1))
# DI2tupleS.append((1, 2))
# DI2tupleS.append((3, 4))
#
# pdie.setDI2tupleS(DI2tupleS)
#
# pdie.print()
# print(pdie.getDI2tupleS())