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

    def cardinality(self):
        return len(self._setList)

    def list(self):
        return self._setList


class Tuple:
    def __init__(self, tupleList):
        self._tupleList = tupleList


class TwoT:

    def __init__(self, first, second):
        self._twoTuple = (first, second)

    def __str__(self):
        return f"({self._twoTuple[0]}, {self._twoTuple[1]})"

    def First(self):
        return self._twoTuple[0]
    def Second(self):
        return self._twoTuple[1]


class TwoTplS(Set):
    def test(self):
        print("test")
    # def __init__(self, twoTplList):
    #     self._twoTplList = twoTplList
    #
    # def __str__(self):
    #     formatStr = "{ "
    #     for i, twoT in enumerate(self._twoTplList):
    #         if i < len(self._twoTplList) - 1:
    #             formatStr += (str(twoT) + ", ")
    #         else:
    #             formatStr += str(twoT)
    #     return formatStr + " }"

    # def list(self):
    #     return self._twoTplList


