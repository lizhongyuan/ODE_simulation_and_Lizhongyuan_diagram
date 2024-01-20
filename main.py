def print_hi(name):
    print(f'Hi, {name}')


def test(str):
    str_len = len(str)
    arrange_arr = [[]]

    for i in range(str_len):
        if i == 0:
            cur_arrange_arr = arrange_arr[0]
            for j in range(str_len):
                cur_data = {
                    'value': str[j],
                    'last_idx': j
                }
                cur_arrange_arr.insert(len(cur_arrange_arr), cur_data)
        else:
            pre_arrange_arr = arrange_arr[i - 1]
            cur_arrange_arr = []

            for pre_arrange_arr_idx in range(len(pre_arrange_arr)):

                cur_pre_arrange_str = pre_arrange_arr[pre_arrange_arr_idx]['value']

                for cur in range(pre_arrange_arr[pre_arrange_arr_idx]['last_idx'] + 1, str_len):
                    cur_new_str = cur_pre_arrange_str + str[cur]
                    cur_data = {
                        'value': cur_new_str,
                        'last_idx': cur
                    }
                    cur_arrange_arr.insert(len(cur_arrange_arr), cur_data)

            arrange_arr.insert(len(arrange_arr), cur_arrange_arr)

    res1 = []
    res2 = []
    for i in range(str_len):
        res2.append([])
        for j in range(len(arrange_arr[i])):
            cur_value = arrange_arr[i][j]['value']
            res1.append(cur_value)
            res2[i].append(cur_value)

    # return arrange_arr
    return {
        'res1': res1,
        'res2': res2
    }


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
    res = test(str6)

    print(res)