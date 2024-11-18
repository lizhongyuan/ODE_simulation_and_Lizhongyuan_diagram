"""
@brief: Brief description of the class.
@author: ZhongYuan.Li
@date: 2024/11/18
"""
from typing import Tuple

from simulations.pdie import PDIES, PDIE, PDIE_ERROR
from simulations.structure import _2Tuple


def atom_add(p_PDIE_S: PDIES,
             p_idx_T: Tuple[int,...],
             p_comm_cut_2tuple: _2Tuple,
             p_unfeasible_DI_2tuple_TS_dict: dict) -> PDIE | None:
    print(f"PDIES 时序加法:\n\n")

    for pdie in p_PDIE_S:
        if pdie.isError():
            return PDIE_ERROR()


