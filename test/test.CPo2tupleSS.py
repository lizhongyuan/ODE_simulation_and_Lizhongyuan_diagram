from simulations.function import get_CP_of_2tuple_SS
from simulations.structure import TwoTuple, TwoTupleSS
from simulations.structure import TwoTupleS

if __name__ == '__main__':
    twoT1 = TwoTuple([1, 2])
    twoT2 = TwoTuple([3, 4])
    twoTplS1 = TwoTupleS([twoT1, twoT2])

    twoT3 = TwoTuple([1, 3])
    twoT4 = TwoTuple([2, 4])
    twoTplS2 = TwoTupleS([twoT3, twoT4])

    twoT5 = TwoTuple([1, 2])
    twoT6 = TwoTuple([3, 4])
    twoT7 = TwoTuple([4, 5])
    twoTplS3 = TwoTupleS([twoT5, twoT6, twoT7])

    twoTupleSS = TwoTupleSS([twoTplS1, twoTplS2, twoTplS3])
    print(str(twoTupleSS))
    idxT = [1, 2, 3]

    # 2tupleSS做某个顺序的笛卡尔积
    twoTupleTS_CP = get_CP_of_2tuple_SS(twoTupleSS, idxT)

    print(str(twoTupleTS_CP))