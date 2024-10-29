

class Set:
    def __init__(self, setList):
        self._setList = setList

    def __str__(self):
        formatStr = "{ "
        for i, elem in enumerate(self._setList):
            if i < len(self._setList) - 1:
                formatStr += (str(elem) + ", ")
            else:
                formatStr += str(elem)
        return formatStr + " }"

    def Cardinality(self):
        return len(self._setList)

    def List(self):
        return self._setList

    def Empty(self):
        return len(self._setList) == 0


class Tuple:
    def __init__(self, tupleList):
        self._tupleList = tupleList

    def __str__(self):
        return f"({self._tupleList[0]}, {self._tupleList[1]})"

    def __len__(self):
        return len(self._tupleList)

    def List(self):
        return self._tupleList


class TwoT(Tuple):

    def First(self):
        return self._tupleList[0]

    def Second(self):
        return self._tupleList[1]


class TwoTplS(Set):
    pass

class TwoTplSS(Set):
    pass


class TwoTplT(Tuple):

    def First(self):
        return self._tupleList[0]

    def Second(self):
        return self._tupleList[1]
