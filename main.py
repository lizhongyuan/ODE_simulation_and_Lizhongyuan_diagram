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
    total = len(event_indexes)
    combinations_and_pivots_array = []

    zero_event_idx = '0'
    zero_items = ['0']
    combination_array = [zero_event_idx]
    binomial_theorem_array = [zero_items]

    for i in range(total):
        cur_items = []
        if i == 0:
            for j in range(total):
                cur_item = {
                    'combination': event_indexes[j],
                    'pivot': j
                }
                cur_items.insert(len(cur_items), cur_item)
        else:
            pre_items = combinations_and_pivots_array[i - 1]

            for j in range(len(pre_items)):

                pre_combination = pre_items[j]['combination']

                for k in range(pre_items[j]['pivot'] + 1, total):
                    cur_combination = pre_combination + event_indexes[k]
                    cur_item = {
                        'combination': cur_combination,
                        'pivot': k
                    }
                    cur_items.insert(len(cur_items), cur_item)

        combinations_and_pivots_array.insert(len(combinations_and_pivots_array), cur_items)

    for i in range(total):
        binomial_theorem_array.append([])
        for j in range(len(combinations_and_pivots_array[i])):
            cur_value = combinations_and_pivots_array[i][j]['combination']
            combination_array.append(cur_value)
            binomial_theorem_array[i].append(cur_value)

    return {
        'combination_array': combination_array,
        'binomial_theorem_array': binomial_theorem_array
    }


def gen_table_headers_recur(event_indexes):
    print('recur version')

    total = len(event_indexes)
    combinations_and_pivots_array = []

    zero_event_idx = '0'
    zero_items = ['0']
    combination_array = [zero_event_idx]
    binomial_theorem_array = [zero_items]

    get_sub_table_headers_recur(combinations_and_pivots_array, combination_array, binomial_theorem_array, total, event_indexes)

    return {
        'combination_array': combination_array,
        'binomial_theorem_array': binomial_theorem_array
    }


def get_sub_table_headers_recur(combinations_and_pivots_array, combination_array, binomial_theorem_array, count, event_indexes):
    total = len(event_indexes)
    cur_items = []

    if count == 1:
        for i in range(total):
            cur_item = {
                'combination': event_indexes[i],
                'pivot': i
            }
            cur_items.append(cur_item)
    else:
        get_sub_table_headers_recur(combinations_and_pivots_array, combination_array, binomial_theorem_array, count - 1, event_indexes)

        pre_items = combinations_and_pivots_array[count - 2]

        for i in range(len(pre_items)):

            pre_combination = pre_items[i]['combination']

            for j in range(pre_items[i]['pivot'] + 1, total):
                cur_combination = pre_combination + event_indexes[j]
                cur_item = {
                    'combination': cur_combination,
                    'pivot': j
                }
                cur_items.append(cur_item)

    combinations_and_pivots_array.insert(len(combinations_and_pivots_array), cur_items)

    binomial_theorem_array.append([])
    for i in range(len(cur_items)):
        cur_value = cur_items[i]['combination']
        combination_array.append(cur_value)
        binomial_theorem_array[count].append(cur_value)


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

    color_matrix = []
    for row_idx in range(data_frame.index.size):
        row_colors = []
        for col_idx in range(data_frame.columns.size):
            if data_frame.values[row_idx][col_idx] == 'ERR':
                row_colors.append(0)  # set black
            else:
                row_colors.append(100)  # set color
        color_matrix.append(row_colors)

    # ax.imshow(X=color_arr, cmap=plt.cm.get_cmap('gist_heat'))
    cmap = colors.ListedColormap(['#080402', '#D03D33'])
    ax.imshow(X=np.array(color_matrix), cmap=cmap)

    ax.set_xticks(np.arange(data_frame.columns.size), labels=data_frame.columns)
    ax.set_yticks(np.arange(data_frame.index.size), labels=data_frame.index)

    fig.tight_layout()


if __name__ == '__main__':
    str1 = 'A'
    str2 = 'AB'
    str3 = 'ABC'
    # a, b, c, ab, ac, bc, abc

    str4 = 'ABCD'
    # a, b, c, d, ab, ac, ad, bc, bd, cd, abc, abd, bcd, abcd

    str5 = 'ABCDE'
    # a, b, c, d, e,
    # ab, ac, ad, ae, bc, bd, be, cd, ce, de,
    # abc, abd, abe, acd, ace, ade, bcd, bce, bde, cde,
    # abcd, abce, abde, acde, bcde
    # abcde

    str6 = 'ABCDEF'
    str7 = 'ABCDEFG'
    str8 = 'ABCDEFGH'
    str9 = 'ABCDEFGHI'
    str10 = 'ABCDEFGHIJ'
    str11 = 'ABCDEFGHIJK'  # 再增加字符等待的时间会很久

    res = gen_table_header_arr(str7)
    # res = gen_table_header_arr2(str7)
    headers = res['combination_array']

    data_frame = init_data_frame(headers)

    build_data_frame(data_frame)
    color_up_data_frame(data_frame, plt)

    plt.show()

    # print(data_frame)
