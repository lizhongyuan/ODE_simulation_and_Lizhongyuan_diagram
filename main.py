import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib as mpl


def init_data_frame(table_headers):
    df = pd.DataFrame(index=list(table_headers), columns=list(table_headers))
    return df


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


def gen_combinations_data(elements):
    """
    生成组合数据
    @param elements: 元素集合
    @return: 组合数据
    """

    # total = len(elements)
    combinations_and_pivots_cache = []

    zero_element = '0'
    zero_elements = ['0']
    combinations = [zero_element]
    binomial_theorem_array = [zero_elements]

    for i in range(len(elements)):
        cur_combinations_and_pivots = []
        if i == 0:
            for j in range(len(elements)):
                cur_combination_and_pivot = {
                    'combination': elements[j],
                    'pivot': j
                }
                cur_combinations_and_pivots.insert(len(cur_combinations_and_pivots), cur_combination_and_pivot)
        else:
            pre_combinations_and_pivots = combinations_and_pivots_cache[i - 1]

            for j in range(len(pre_combinations_and_pivots)):
                pre_combination = pre_combinations_and_pivots[j]['combination']
                for k in range(pre_combinations_and_pivots[j]['pivot'] + 1, len(elements)):
                    cur_combination = pre_combination + elements[k]
                    cur_combination_and_pivot = {
                        'combination': cur_combination,
                        'pivot': k
                    }
                    cur_combinations_and_pivots.append(cur_combination_and_pivot)

        combinations_and_pivots_cache.append(cur_combinations_and_pivots)

    for i in range(len(elements)):
        binomial_theorem_array.append([])
        cur_binomial_theorem_item = []
        for j in range(len(combinations_and_pivots_cache[i])):
            cur_combination = combinations_and_pivots_cache[i][j]['combination']
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


def build_data_frame(data_frame, zero_element):
    """
    构造data_frame
    @param data_frame:
    @param zero_element: 0元素
    @return:
    """
    for row in data_frame.index:
        for col in data_frame.columns:
            if row == zero_element:
                data_frame.loc[row, col] = col
            elif col == zero_element:
                data_frame.loc[row, col] = row
            else:
                if has_no_common_element(row, col):
                    data_frame.loc[row, col] = combination_merge(row, col)
                else:
                    data_frame.loc[row, col] = 'ERR'


def color_up_plot(data_frame, plt, dpi, font_size, axis_length_zero):
    """
    plot上色
    @param data_frame:
    @param plt:
    @return:
    """

    mpl.rcParams["font.size"] = font_size

    if dpi is not None:
        mpl.rcParams["figure.dpi"] = dpi

    fig, ax = plt.subplots()

    if axis_length_zero:
        ax.tick_params(axis='both', which='both', length=0)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    color_matrix = []
    for row_idx in range(data_frame.index.size):
        row_colors = []
        for col_idx in range(data_frame.columns.size):
            if data_frame.values[row_idx][col_idx] == 'ERR':
                row_colors.append(0)        # set black
            else:
                row_colors.append(100)      # set color
        color_matrix.append(row_colors)

    # ax.imshow(X=color_arr, cmap=plt.cm.get_cmap('gist_heat'))
    cmap = colors.ListedColormap(['#080402', '#D03D33'])
    ax.imshow(X=np.array(color_matrix), cmap=cmap)

    ax.set_xticks(np.arange(data_frame.columns.size), labels=data_frame.columns)
    ax.set_yticks(np.arange(data_frame.index.size), labels=data_frame.index)

    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-70, ha="right", rotation_mode="anchor")

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

    # dpi = 100
    # font_size = 10
    # axis_length_zero = False
    # res = gen_combinations_data(elements3)

    # 9: 3000, 0.75
    dpi = 3000
    font_size = 0.75
    axis_length_zero = True
    res = gen_combinations_data(elements3)

    # 10: 4000, 0.5
    # dpi = 3000
    # font_size = 0.3
    # axis_length_zero = True
    # res = gen_combinations_data(elements10)

    headers = res['combinations']

    data_frame = init_data_frame(headers)

    build_data_frame(data_frame, zero_element='0')
    color_up_plot(data_frame, plt, dpi, font_size, axis_length_zero)

    # plt.show()

    plt.savefig('pic.png')
