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
    arrange_arr = [[]]

    for i in range(str_len):
        if i == 0:
            cur_arrange_arr = arrange_arr[0]
            for j in range(str_len):
                cur_data = {
                    'value': event_indexes[j],
                    'last_idx': j
                }
                cur_arrange_arr.insert(len(cur_arrange_arr), cur_data)
        else:
            pre_arrange_arr = arrange_arr[i - 1]
            cur_arrange_arr = []

            for pre_arrange_arr_idx in range(len(pre_arrange_arr)):

                cur_pre_arrange_str = pre_arrange_arr[pre_arrange_arr_idx]['value']

                for cur in range(pre_arrange_arr[pre_arrange_arr_idx]['last_idx'] + 1, str_len):
                    cur_new_str = cur_pre_arrange_str + event_indexes[cur]
                    cur_data = {
                        'value': cur_new_str,
                        'last_idx': cur
                    }
                    cur_arrange_arr.insert(len(cur_arrange_arr), cur_data)

            arrange_arr.insert(len(arrange_arr), cur_arrange_arr)

    table_headers = []
    table_header_groups = []
    for i in range(str_len):
        table_header_groups.append([])
        for j in range(len(arrange_arr[i])):
            cur_value = arrange_arr[i][j]['value']
            table_headers.append(cur_value)
            table_header_groups[i].append(cur_value)

    # return arrange_arr
    return {
        'table_headers': table_headers,
        'table_header_groups': table_header_groups
    }


def build_data_frame(data_frame):
    for row in data_frame.index:
        for col in data_frame.columns:
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

    data_frame = init_data_frame(res['table_headers'])

    build_data_frame(data_frame)
    color_up_data_frame(data_frame, plt)

    plt.show()

    print(data_frame)
