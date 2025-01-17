from typing import List

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from matplotlib import colors
import matplotlib as mpl
from matplotlib.colors import ListedColormap
from pandas.core.interchange.dataframe_protocol import DataFrame


def init_data_frame(p_table_headers: List[str]) -> DataFrame:
    return pd.DataFrame(index=p_table_headers,
                        columns=p_table_headers)


def has_no_common_element(combination1, combination2):
    """
    检查两个元素组合是否没有相同元素
    @param combination1: 元素组合1
    @param combination2: 元素组合2
    @return: 是否没有相同元素
    """

    for element in combination1:
        if element in combination2:
            return False

    return True


def combination_merge(combination1, combination2):
    """
    合并组合
    @param combination1: 元素组合1
    @param combination2: 元素组合2
    @return: 合并后的组合
    """

    merged_combination = combination1 + combination2
    merged_combination = ''.join(sorted(merged_combination))

    return merged_combination


def gen_combinations_data(p_elements: str):
    """
    生成组合数据
    @param p_elements: 元素集合
    @return: 组合数据
    """

    combinations_and_pivots_cache: List[List[dict]] = []

    zero_element: str = '0'
    zero_elements: List[str] = ['0']
    combinations: List[str] = [zero_element]
    binomial_theorem_array: List[List[str]] = [zero_elements]

    for i in range(len(p_elements)):
        cur_combinations_and_pivots: List[dict] = []
        if i == 0:
            for j in range(len(p_elements)):
                cur_combination_and_pivot: dict = {
                    'combination': p_elements[j],
                    'pivot': j
                }
                cur_combinations_and_pivots.insert(len(cur_combinations_and_pivots), cur_combination_and_pivot)
        else:
            pre_combinations_and_pivots: List[dict] = combinations_and_pivots_cache[i - 1]

            for j in range(len(pre_combinations_and_pivots)):
                pre_combination: str = pre_combinations_and_pivots[j]['combination']
                for k in range(pre_combinations_and_pivots[j]['pivot'] + 1, len(p_elements)):
                    cur_combination: str = pre_combination + p_elements[k]
                    cur_combination_and_pivot: dict = {
                        'combination': cur_combination,
                        'pivot': k
                    }
                    cur_combinations_and_pivots.append(cur_combination_and_pivot)

        combinations_and_pivots_cache.append(cur_combinations_and_pivots)

    for i in range(len(p_elements)):
        binomial_theorem_array.append([])
        cur_binomial_theorem_item: List[str] = []
        for j in range(len(combinations_and_pivots_cache[i])):
            cur_combination: str = combinations_and_pivots_cache[i][j]['combination']
            combinations.append(cur_combination)
            cur_binomial_theorem_item.append(cur_combination)
        binomial_theorem_array.append(cur_binomial_theorem_item)

    return {
        'combinations': combinations,
        'binomial_theorem_array': binomial_theorem_array
    }


def gen_combinations_data_recur(elements):
    """
    生成组合数据(递归)
    @param elements: 元素集合
    @return: 组合数据
    """

    combinations_and_pivots_cache = []

    zero_element = '0'
    zero_element_array = ['0']
    combinations = [zero_element]
    binomial_theorem_array = [zero_element_array]

    gen_sub_combinations_data_recur(combinations_and_pivots_cache,
                                    combinations,
                                    binomial_theorem_array,
                                    len(elements),
                                    elements)

    return {
        'combinations': combinations,
        'binomial_theorem_array': binomial_theorem_array
    }


def gen_sub_combinations_data_recur(combinations_and_pivots_cache,
                                    combinations,
                                    binomial_theorem_array,
                                    count,
                                    elements):
    """
    生成子axes的headers
    @param combinations_and_pivots_cache: 元素组合和结尾元素位置数组
    @param combinations: 元素组合数组
    @param binomial_theorem_array: 二项式定理分布数组
    @param count: 参与组合的元素数
    @param elements: 全部元素数组
    @return
    """

    cur_combinations_and_pivots = []                                                        # 声明"当前组合和枢轴数组"

    if count == 1:                                                                          # if elements元素数为1
        for i in range(len(elements)):                                                      # 遍历elements数组:
            cur_combination_and_pivot = {                                                   #
                'combination': elements[i],
                'pivot': i
            }
            cur_combinations_and_pivots.append(cur_combination_and_pivot)
    else:
        gen_sub_combinations_data_recur(combinations_and_pivots_cache,
                                        combinations,
                                        binomial_theorem_array,
                                        count - 1,
                                        elements)

        pre_combinations_and_pivots = combinations_and_pivots_cache[count - 2]

        for i in range(len(pre_combinations_and_pivots)):
            pre_combination = pre_combinations_and_pivots[i]['combination']

            for j in range(pre_combinations_and_pivots[i]['pivot'] + 1, len(elements)):
                cur_combination = pre_combination + elements[j]
                cur_combination_and_pivot = {
                    'combination': cur_combination,
                    'pivot': j
                }
                cur_combinations_and_pivots.append(cur_combination_and_pivot)

    combinations_and_pivots_cache.append(cur_combinations_and_pivots)

    cur_binomial_theorem_item = []
    binomial_theorem_array.append([])
    for i in range(len(cur_combinations_and_pivots)):
        cur_combination = cur_combinations_and_pivots[i]['combination']
        combinations.append(cur_combination)
        cur_binomial_theorem_item.append(cur_combination)

    binomial_theorem_array.append(cur_binomial_theorem_item)


def build_data_frame(p_data_frame: DataFrame, p_zero_elem: str):
    """
    构造p_data_frame
    @param p_data_frame: DataFrame instance
    @param p_zero_elem: 0 element
    @return:
    """
    for row in p_data_frame.index:
        for col in p_data_frame.columns:
            if row == p_zero_elem:
                p_data_frame.loc[row, col] = col
            elif col == p_zero_elem:
                p_data_frame.loc[row, col] = row
            else:
                if has_no_common_element(row, col):
                    p_data_frame.loc[row, col] = combination_merge(row, col)
                else:
                    p_data_frame.loc[row, col] = 'ERR'


def render_plot(p_data_frame: DataFrame,
                p_plt: pyplot,
                p_dpi: int,
                p_font_size: float,
                p_no_tick_marks: bool):
    """
    Render the plot
    @param p_data_frame: graph frame
    @param p_plt: matplotlib.pyplot
    @param p_dpi: dots per inch
    @param p_font_size: font size
    @param p_no_tick_marks: whether it has a tick mark
    @return:
    """

    mpl.rcParams["font.size"] = p_font_size

    if p_dpi is not None:
        mpl.rcParams["figure.dpi"] = p_dpi

    fig, ax = p_plt.subplots()

    if p_no_tick_marks:
        ax.tick_params(axis='both', which='both', length=0)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    color_matrix: List[List[int]] = []
    for row_idx in range(p_data_frame.index.size):
        row_colors: List[int] = []
        for col_idx in range(p_data_frame.columns.size):
            if p_data_frame.values[row_idx][col_idx] == 'ERR':
                row_colors.append(0)        # set black
            else:
                row_colors.append(100)      # set color
        color_matrix.append(row_colors)

    # ax.imshow(X=color_arr, cmap=plt.cm.get_cmap('gist_heat'))
    cmap: ListedColormap = colors.ListedColormap(['#080402', '#D03D33'])
    ax.imshow(X=np.array(color_matrix),
              cmap=cmap)

    ax.set_xticks(np.arange(p_data_frame.columns.size),
                  labels=p_data_frame.columns)
    ax.set_yticks(np.arange(p_data_frame.index.size),
                  labels=p_data_frame.index)

    ax.tick_params(top=True,
                   bottom=False,
                   labeltop=True,
                   labelbottom=False)

    # Rotate the tick labels and set their alignment.
    p_plt.setp(ax.get_xticklabels(),
               rotation=-70,
               ha="right",
               rotation_mode="anchor")

    fig.tight_layout()


if __name__ == '__main__':
    elements1 = 'A'
    elements2 = 'AB'
    elements3 = 'ABC'
    elements4 = 'ABCD'
    elements5 = 'ABCDE'
    elements6 = 'ABCDEF'
    elements7 = 'ABCDEFG'
    elements8 = 'ABCDEFGH'
    elements9 = 'ABCDEFGHI'
    elements10 = 'ABCDEFGHIJ'
    elements11 = 'ABCDEFGHIJK'  # 再增加字符等待的时间会很久

    dpi = 100
    font_size = 10
#    axis_length_zero = False
    no_tick_marks = True
    res = gen_combinations_data(p_elements=elements3)

    # 9: 3000, 0.75
    # dpi = 3000
    # font_size = 0.75
    # axis_length_zero = True
    # res = gen_combinations_data(elements9)

    # 10: 4000, 0.5
    # dpi = 3000
    # font_size = 0.3
    # axis_length_zero = True
    # res = gen_combinations_data(elements10)

    headers: List[str] = res['combinations']

    data_frame: DataFrame = init_data_frame(p_table_headers=headers)

    build_data_frame(p_data_frame=data_frame,
                     p_zero_elem='0')

    render_plot(p_data_frame=data_frame,
                p_plt=pyplot,
                p_dpi=dpi,
                p_font_size=font_size,
                p_no_tick_marks=no_tick_marks)

    # plt.show()

    pyplot.savefig('pic.png')
