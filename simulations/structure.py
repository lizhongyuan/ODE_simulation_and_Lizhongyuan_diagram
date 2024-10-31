

class MySet:
    def __init__(self, setList):
        self._list = setList
        self._dict = {i: self._list[i - 1] for i in range(1, len(self._list) + 1)}

    def __getitem__(self, index):
        return self._list[index - 1]
    def __setitem__(self, index, value):
        self._list[index - 1] = value

    def __str__(self) -> str:
        format_str = "{"
        for i, elem in enumerate(self._list):
            if i < len(self._list) - 1:
                format_str += (str(elem) + ", ")
            else:
                format_str += str(elem)
        format_str += "}"

        return format_str

    def cardinality(self) -> int:
        return len(self._list)

    def list(self) -> list:
        return self._list

    def empty(self) -> bool:
        return len(self._list) == 0


class MyTuple:

    def __init__(self, tupleList):
        self._list = tupleList

    def __getitem__(self, index):
        return self._list[index - 1]

    def __setitem__(self, index, value):
        self._list[index - 1] = value

    def __str__(self) -> str:
        format_str = "("
        for i, elem in enumerate(self._list):
            if i < len(self._list) - 1:
                format_str += (str(elem) + ", ")
            else:
                format_str += str(elem)
        format_str += ")"

        return format_str

    def __len__(self) -> int:
        return len(self._list)

    def list(self) -> list:
        return self._list

    def __eq__(self, other):
        for i in range(1, len(self._list) + 1):
            if self.__getitem__(i) != other[i]:
                return False
        return True


class TwoTuple(MyTuple):

    def first(self) -> object:
        return self.__getitem__(1)

    def second(self):
        return self.__getitem__(2)

    def instance(self) -> tuple[object, object]:
        return self.__getitem__(1), self.__getitem__(2)


class TwoTupleS(MySet):
    pass

class CutTwoTupleS(MySet):
    pass

class TwoTupleSS(MySet):
    pass

class TwoTupleTS(MySet):
    pass


class TwoTupleT(MyTuple):
    pass
