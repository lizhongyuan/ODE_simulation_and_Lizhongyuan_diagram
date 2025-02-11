"""
@file: main.py
@brief: Test cases of complete sequential addition & complete sequential multiplication
@author: li.zhong.yuan@outlook.com
@date: 2025/1/23
"""


from simulations.test.pdieOP.test_add import (test_complete_sequential_addition_1,
                                              test_complete_sequential_addition_2,
                                              test_complete_sequential_addition_3,
                                              test_complete_sequential_addition_4,
                                              test_complete_sequential_addition_5,
                                              test_complete_sequential_addition_6)
from simulations.test.pdieOP.test_multi import (test_complete_sequential_multiplication_1,
                                                test_complete_sequential_multiplication_2,
                                                test_complete_sequential_multiplication_3)
from simulations.test.base.test_f_feasible_DI_2tuple_TS import test_f_feasible_DI_2tuple_TS


if __name__ == '__main__':

#    test_f_feasible_DI_2tuple_TS()

    test_complete_sequential_addition_1()

    test_complete_sequential_addition_2()

    test_complete_sequential_addition_3()

    test_complete_sequential_addition_4()

    test_complete_sequential_addition_5()

    test_complete_sequential_addition_6()

    test_complete_sequential_multiplication_1()

    test_complete_sequential_multiplication_2()

    test_complete_sequential_multiplication_3()
