class TwoT:

    def __init__(self, first, second):
        self._twoTuple = (first, second)

    def First(self):
        return self._twoTuple[0]
    def Second(self):
        return self._twoTuple[1]

    def Print(self):
        print(f"({self._twoTuple[0]}, {self._twoTuple[1]})")


twoT = TwoT(1,2)
twoT.Print()