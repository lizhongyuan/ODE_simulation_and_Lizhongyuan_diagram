from simulations.function import get_min_first_of_2tuple_S, get_max_second_of_2tuple_S
from simulations.structure import _2Tuple, _2TupleT, _2TupleSS
from simulations.structure import _2TupleS

if __name__ == '__main__':
    twoT1 = _2Tuple([1, 2])
    twoT2 = _2Tuple([4, 5])
    twoTplS1 = _2TupleS([twoT1, twoT2])

    twoT3 = _2Tuple([1, 3])
    twoT4 = _2Tuple([2, 4])
    twoTplS2 = _2TupleS([twoT3, twoT4])

    twoTplSS = _2TupleSS([twoTplS1, twoTplS2, twoTplS3])
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