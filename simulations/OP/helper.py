"""
@brief: Complete sequential addition & Complete sequential multiplication.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/14
"""

from typing import Tuple


def check_idx_tuple_border(p_idx_T: Tuple[int,...], length: int) -> bool:
    """
    Check the upper and lower bounds of the index tuple
    Args:
        p_idx_T (Tuple[int,...]): An index tuple
        length (int): The extent of the range

    Returns:
        bool: Whether the bound of p_idx_T is legal
    """

    for idx in p_idx_T:
        if not isinstance(idx, int) or idx < 1 or idx > length:
            return False
    return True

def has_duplicates(tup) -> bool:
    return len(set(tup)) != len(tup)


def print_finish_line() -> None:
    print(f"############################## Finish ##############################\n\n\n\n")
