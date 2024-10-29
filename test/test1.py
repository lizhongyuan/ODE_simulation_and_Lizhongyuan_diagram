from simulations.structure import TwoT
from simulations.structure import TwoTplS

if __name__ == '__main__':
    twoT1 = TwoT(1,2)
    twoT2 = TwoT(2,3)
    print(str(twoT1))

    twoTplS = TwoTplS([twoT1, twoT2])
    print(str(twoTplS))
    print(str(len(twoTplS.list())))         # OK
