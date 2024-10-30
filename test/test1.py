from simulations.function import fMin1oS, fMax2oS
from simulations.structure import TwoTuple, TwoTupleT, TwoTupleSS
from simulations.structure import TwoTupleS

if __name__ == '__main__':
    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([4, 5])
    twoTplS1 = TwoTupleS([twoT1, twoT2])

    twoT3 = TwoTuple([1, 3])
    twoT4 = TwoTuple([2, 4])
    twoTplS2 = TwoTupleS([twoT3, twoT4])

    twoTplSS = TwoTupleSS([twoTplS1, twoTplS2, twoTplS3])
    print(str(twoTplSS))

#     print(str(twoTplS))
#     print(str(len(twoTplS.List())))         # OK
#
#     minFirst = fMin1oS(twoTplS)
#     maxSecond = fMax2oS(twoTplS)
#     print(minFirst)
#     print(maxSecond)
#
#     twoTplT = TwoTupleT([twoT1, twoT2])
#     print(str(twoTplT))

    # 2tupleSS做某个顺序的笛卡尔积