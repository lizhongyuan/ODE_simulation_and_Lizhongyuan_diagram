import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors


def init_data_frame(table_headers):
    df = pd.DataFrame(index=list(table_headers), columns=list(table_headers))

    return df


def has_no_common_chr(str1, str2):
    """
    检查两个字符串是否有公共字符
    @param str1: 字符串1
    @param str2: 字符串2
    @return: 是否有公共字符
    """

    for chr in str1:
        if chr in str2:
            return False

    return True


def string_merge(str1, str2):
    """
    合并字符串
    @param str1: 字符串1
    @param str2: 字符串2
    @return: 合并的字符串
    """

    merged_str = str1 + str2
    merged_str = ''.join(sorted(merged_str))

    return merged_str


def gen_table_header_arr(event_indexes):
    count = len(event_indexes)
    combinations_and_pivots_array = [[]]

    for i in range(count):
        if i == 0:
            cur_items = combinations_and_pivots_array[0]
            for j in range(count):
                cur_item = {
                    'combination': event_indexes[j],
                    'pivot': j
                }
                cur_items.insert(len(cur_items), cur_item)
        else:
            pre_items = combinations_and_pivots_array[i - 1]
            cur_items = []

            for j in range(len(pre_items)):

                pre_combination = pre_items[j]['combination']

                for k in range(pre_items[j]['pivot'] + 1, count):
                    cur_combination = pre_combination + event_indexes[k]
                    cur_item = {
                        'combination': cur_combination,
                        'pivot': k
                    }
                    cur_items.insert(len(cur_items), cur_item)

            combinations_and_pivots_array.insert(len(combinations_and_pivots_array), cur_items)

    combination_array = []
    binomial_theorem_array = []
    for i in range(count):
        binomial_theorem_array.append([])
        for j in range(len(combinations_and_pivots_array[i])):
            cur_value = combinations_and_pivots_array[i][j]['combination']
            combination_array.append(cur_value)
            binomial_theorem_array[i].append(cur_value)

    combination_array.insert(0, '0')
    binomial_theorem_array.insert(0, ['0'])

    # return combinations_and_pivots
    return {
        'combination_array': combination_array,
        'binomial_theorem_array': binomial_theorem_array
    }


def build_data_frame(data_frame):
    for row in data_frame.index:
        for col in data_frame.columns:
            if row == '0':
                data_frame.loc[row, col] = col
            elif col == '0':
                data_frame.loc[row, col] = row
            else:
                if has_no_common_chr(row, col):
                    data_frame.loc[row, col] = string_merge(row, col)
                else:
                    data_frame.loc[row, col] = 'ERR'


def color_up_data_frame(data_frame, plt):
    print('color_up_table')

    fig, ax = plt.subplots()

    # color_table = ax.table(cellText=data_frame.values,
    #                        colLabels=data_frame.columns,
    #                        rowLabels=data_frame.index,
    #                        loc="center")

    color_arr = []
    for row_idx in range(data_frame.index.size):
        cur_row_arr = []
        for col_idx in range(data_frame.columns.size):
            if data_frame.values[row_idx][col_idx] == 'ERR':
                # color_table.get_celld()[(row_idx + 1, col_idx)].set_facecolor('#222222')
                cur_row_arr.append(0.0)
            else:
                # color_table.get_celld()[(row_idx + 1, col_idx)].set_facecolor('#D40000')
                cur_row_arr.append(1.1)
        color_arr.append(cur_row_arr)

    color_arr = np.array(color_arr)
    print(color_arr)
    # ax.imshow(X=color_arr, cmap=plt.cm.get_cmap('gist_heat'))
    cmap = colors.ListedColormap(['#080402', '#D03D33'])
    ax.imshow(X=np.array(color_arr), cmap=cmap)
    # ax.imshow(X=np.array(color_arr), cmap=mpl.colormaps['copper'])

    ax.set_xticks(np.arange(data_frame.columns.size), labels=data_frame.columns)
    ax.set_yticks(np.arange(data_frame.index.size), labels=data_frame.index)

    fig.tight_layout()
    plt.show()
    #
    # for row_idx in range(data_frame.index.size):
    #     for col_idx in range(data_frame.columns.size):
    #         if data_frame.values[row_idx][col_idx] == 'ERR':
    #             color_table.get_celld()[(row_idx + 1, col_idx)].set_facecolor('#222222')
    #         else:
    #             color_table.get_celld()[(row_idx + 1, col_idx)].set_facecolor('#D40000')
    #

if __name__ == '__main__':
    # str1 = 'abc'
    str1 = 'ABC'
    # a, b, c, ab, ac, bc, abc

    str2 = 'ABCD'
    # a, b, c, d, ab, ac, ad, bc, bd, cd, abc, abd, bcd, abcd

    str3 = 'ABCDE'
    # a, b, c, d, e,
    # ab, ac, ad, ae, bc, bd, be, cd, ce, de,
    # abc, abd, abe, acd, ace, ade, bcd, bce, bde, cde,
    # abcd, abce, abde, acde, bcde
    # abcde

    str4 = 'ABCDEF'
    str5 = 'ABCDEFG'
    str6 = 'ABCDEFGH'
    str7 = 'ABCDEFGHIJK'    # 再增加字符等待的时间会很久

    # arr = test(str1)
    # arr = test(str2)
    res = gen_table_header_arr(str2)
    headers = res['combination_array']

    data_frame = init_data_frame(headers)

    build_data_frame(data_frame)
    color_up_data_frame(data_frame, plt)

    # plt.show()

    print(data_frame)
