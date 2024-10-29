class TwoT:

    def __init__(self, first, second):
        self._twoTuple = (first, second)

    def __str__(self):
        return f"({self._twoTuple[0]}, {self._twoTuple[1]})"

    def First(self):
        return self._twoTuple[0]
    def Second(self):
        return self._twoTuple[1]


class TwoTplS:
    def __init__(self, twoTplList):
        self._twoTplList = twoTplList

    def __str__(self):
        formatStr = "{ "
        for i, twoT in enumerate(self._twoTplList):
            if i < len(self._twoTplList) - 1:
                formatStr += (str(twoT) + ", ")
            else:
                formatStr += str(twoT)
        return formatStr + " }"

twoT1 = TwoT(1,2)
twoT2 = TwoT(2,3)
print(str(twoT1))

twoTplS = TwoTplS([twoT1, twoT2])
print(str(twoTplS))
