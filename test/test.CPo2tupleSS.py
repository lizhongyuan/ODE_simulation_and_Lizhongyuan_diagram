from simulations.function import get_custom_ordered_CP_of_2tuple_SS
from simulations.structure import _2Tuple, _2TupleSS
from simulations.structure import _2TupleS


if __name__ == '__main__':
    twoT1 = _2Tuple([1, 2])
    twoT2 = _2Tuple([3, 4])
    twoTplS1 = _2TupleS([twoT1, twoT2])

    twoT3 = _2Tuple([1, 3])
    twoT4 = _2Tuple([2, 4])
    twoTplS2 = _2TupleS([twoT3, twoT4])

    twoT5 = _2Tuple([1, 2])
    twoT6 = _2Tuple([3, 4])
    twoT7 = _2Tuple([4, 5])
    twoTplS3 = _2TupleS([twoT5, twoT6, twoT7])

    twoTupleSS = _2TupleSS([twoTplS1, twoTplS2, twoTplS3])
    print(str(twoTupleSS))
    idxT = [1, 2, 3]

    # 2tupleSS做某个顺序的笛卡尔积
    twoTupleTS_CP = get_custom_ordered_CP_of_2tuple_SS(twoTupleSS, idxT)

    print(str(twoTupleTS_CP))