from simulations.function import fMin1oS, fMax2oS
from simulations.structure import TwoTuple, TwoTupleT
from simulations.structure import TwoTupleS

if __name__ == '__main__':
    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([2, 3])
    print(str(twoT1))

    twoTplS = TwoTupleS([twoT1, twoT2])
    print(str(twoTplS))
#    print(str(len(twoTplS.List())))         # OK

    minFirst = fMin1oS(twoTplS)
    maxSecond = fMax2oS(twoTplS)
    print(minFirst)
    print(maxSecond)

    twoTplT = TwoTupleT([twoT1, twoT2])
    print(str(twoTplT))
