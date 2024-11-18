

class MySet:
    def __init__(self, setList: list):
        self._list = setList
        self._dict = {i: self._list[i - 1] for i in range(1, len(self._list) + 1)}

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value
        self._dict[index + 1] = value

    def __str__(self) -> str:
        format_str = "{"
        for i, elem in enumerate(self._list):
            if i < len(self._list) - 1:
                format_str += (str(elem) + ", ")
            else:
                format_str += str(elem)
        format_str += "}"

        return format_str

    # todo: __eq__
    def __eq__(self, other):
        if len(self._list) != other.cardinality():
            return False

        for item in self._list:
            cur_equal = False
            for other_item in other:
                if item == other_item:
                    cur_equal = True
                    break
            if not cur_equal:
                return False

        return True

    def get(self, num: int) -> object:
        if num < 1 or num > len(self._list):
            return None
        return self._list[num - 1]

    def index(self, item):
        """

        Args:
            item:

        Returns:

        """
        for i in range(1, len(self._list) + 1):
            if self._list[i] == item:
                return i
        return 0

    def dict(self):
        return self._dict

    def cardinality(self) -> int:
        return len(self._list)

    def list(self) -> list:
        return self._list

    def empty(self) -> bool:
        return len(self._list) == 0

    def has(self, item: object) -> bool:
        for elem in self._list:
            if item == elem:
                return True
        return False

    def add(self, elem):
        if self.has(elem):
            return

        self._list.append(elem)


class MyTuple:

    def __init__(self, tupleList):
        self._list = tupleList

    def __getitem__(self, index):
#        return self._list[index - 1]
        return self._list[index]

    def __setitem__(self, index, value):
#        self._list[index - 1] = value
        self._list[index] = value

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
        if len(self._list) != len(other):
            return False

        for i in range(0, len(self._list)):
            if self.__getitem__(i) != other[i]:
                return False
        return True


class _2Tuple(MyTuple):

    def first(self) -> object:
#        return self.__getitem__(1)
        return self.__getitem__(0)

    def second(self):
#        return self.__getitem__(2)
        return self.__getitem__(1)

    def instance(self) -> tuple[object, object]:
#        return self.__getitem__(1), self.__getitem__(2)
        return self.__getitem__(0), self.__getitem__(1)


class _2TupleS(MySet):
    pass

class Cut2TupleS(MySet):
    pass

class _2TupleSS(MySet):
    pass

class _2TupleT(MyTuple):
    pass

class _2TupleTS(MySet):
    pass

class _2TupleTSS(MySet):
    pass
