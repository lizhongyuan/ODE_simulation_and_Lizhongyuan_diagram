import pandas as pd
import matplotlib.pyplot as plt


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
    str_len = len(event_indexes)
    combinations_and_pivots_array = [[]]

    for i in range(str_len):
        if i == 0:
            cur_array = combinations_and_pivots_array[0]
            for j in range(str_len):
                cur_item = {
                    'combination': event_indexes[j],
                    'pivot': j
                }
                cur_array.insert(len(cur_array), cur_item)
        else:
            pre_array = combinations_and_pivots_array[i - 1]
            cur_array = []

            for j in range(len(pre_array)):

                cur_pre_combination = pre_array[j]['combination']

                for k in range(pre_array[j]['pivot'] + 1, str_len):
                    cur_combination = cur_pre_combination + event_indexes[k]
                    cur_item = {
                        'combination': cur_combination,
                        'pivot': k
                    }
                    cur_array.insert(len(cur_array), cur_item)

            combinations_and_pivots_array.insert(len(combinations_and_pivots_array), cur_array)

    combination_array = []
    binomial_theorem_array = []
    for i in range(str_len):
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

    fig, ax = plt.subplots(1, 1)

    color_table = ax.table(cellText=data_frame.values,
                           colLabels=data_frame.columns,
                           rowLabels=data_frame.index,
                           loc="center"
                           )

    ax.axis('tight')
    ax.axis('off')

    for row_idx in range(data_frame.index.size):
        for col_idx in range(data_frame.columns.size):
            if data_frame.values[row_idx][col_idx] == 'ERR':
                color_table.get_celld()[(row_idx + 1, col_idx)].set_facecolor('#222222')
            else:
                color_table.get_celld()[(row_idx + 1, col_idx)].set_facecolor('#D40000')


if __name__ == '__main__':
    # str1 = 'abc'
    test_str1 = 'ABC'
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
    str5 = 'abcdefg'
    str6 = 'abcdefghijklmn'

    # arr = test(str1)
    # arr = test(str2)
    res = gen_table_header_arr(str2)

    data_frame = init_data_frame(res['combination_array'])

    build_data_frame(data_frame)
    color_up_data_frame(data_frame, plt)

    plt.show()

    print(data_frame)
