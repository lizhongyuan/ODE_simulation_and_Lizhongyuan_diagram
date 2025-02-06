"""
@brief: _2Tuple class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""

from simulations.structure import LiZhongYuanTuple


class _2Tuple(LiZhongYuanTuple):

    def first(self) -> any:
        return self.__getitem__(0)

    def second(self) -> any:
        return self.__getitem__(1)

    def instance(self) -> tuple[any, any]:
        return self.__getitem__(0), self.__getitem__(1)

