"""
@brief: _2TupleT class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""

from simulations.structure import LiZhongYuanTuple


class _2TupleT(LiZhongYuanTuple):
    def wildcard_match(self, p_pattern_2tuple_T) -> bool:
        if len(self._list) != len(p_pattern_2tuple_T):
            return False

        match = True
        for i in range(0, len(self._list)):
            if p_pattern_2tuple_T[i] != self._list[i] and p_pattern_2tuple_T[i] != '*':
                match = False
                break

        return match
