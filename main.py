import pandas as pd


def print_hi(name):
    print(f'Hi, {name}')


def init_table(table_headers):
    df = pd.DataFrame(index=list(table_headers), columns=list(table_headers))

    return df


def no_same_chr(str1, str2):
    for char in str1:
        if char in str2:
            return False

    return True


def string_merge(str1, str2):
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


def build_table(table):
    for item1 in table.axes[0].values:
        for item2 in table.axes[1].values:
            if no_same_chr(item1, item2):
                table[item1][item2] = string_merge(item1, item2)
            else:
                table[item1][item2] = 'ERR'


if __name__ == '__main__':
    print_hi('PyCharm')

    str1 = 'abc'
    # a, b, c, ab, ac, bc, abc

    str2 = 'abcd'
    # a, b, c, d, ab, ac, ad, bc, bd, cd, abc, abd, bcd, abcd

    str3 = 'abcde'
    # a, b, c, d, e,
    # ab, ac, ad, ae, bc, bd, be, cd, ce, de,
    # abc, abd, abe, acd, ace, ade, bcd, bce, bde, cde,
    # abcd, abce, abde, acde, bcde
    # abcde

    str4 = 'abcdef'
    str5 = 'abcdefg'
    str6 = 'abcdefghijklmn'

    # arr = test(str1)
    # arr = test(str2)
    res = gen_table_header_arr(str1)

    # print(res)
    table = init_table(res['table_headers'])
    build_table(table)

    print(table)
