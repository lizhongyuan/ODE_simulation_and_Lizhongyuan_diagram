

class MySet(set):
    def __init__(self, setList):
        self._setList = setList

    def __str__(self) -> str:
        formatStr = "{"
        for i, elem in enumerate(self._setList):
            if i < len(self._setList) - 1:
                formatStr += (str(elem) + ", ")
            else:
                formatStr += str(elem)
        return formatStr + "}"

    def Cardinality(self) -> int:
        return len(self._setList)

    def List(self) -> list:
        return self._setList

    def Empty(self) -> bool:
        return len(self._setList) == 0


class Tuple:

    def __init__(self, tupleList):
        self._tupleList = tupleList

    def __str__(self) -> str:
        return f"({self._tupleList[0]}, {self._tupleList[1]})"

    def __len__(self) -> int:
        return len(self._tupleList)

    def List(self) -> list:
        return self._tupleList


class TwoTuple(Tuple):

    def First(self) -> object:
        return self._tupleList[0]

    def Second(self):
        return self._tupleList[1]


class TwoTupleS(MySet):
    pass

class TwoTupleSS(MySet):
    pass

class TwoTupleTS(MySet):
    pass


class TwoTupleT(Tuple):

    def First(self):
        return self._tupleList[0]

    def Second(self):
        return self._tupleList[1]
