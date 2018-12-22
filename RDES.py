import libcrypt as lc
import random as rnd
import argparse

min_key = 9223372036854775808
max_key = 18446744073709551615


def main():
    path = parse_arguments().path
    text = read_txt(path)

    s = chr_to_bin(text)
    keys = []
    for i in range(3):
        key = gpsc(min_key)
        keys.append(key)
    ss = algoritmBlocks(s, keys)
    print("ss - > ", ss)

    result_bin = un_algoritmBlocks(ss, keys)
    result_text = bin_to_txt(result_bin)
    print(result_text)
# 16*4
initial_d = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
             40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13,
             5, 63, 55, 47, 39, 31, 23, 15, 7]
# 16*2
half_d = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
          11, 4, 25]
# 16*4
final_d = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13,
           53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]
# 16*4
s1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8, 4, 1,
      14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
# 16*4
s2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, 0, 14,
      7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
# 16*4
s3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 13, 6,
      4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
# 16*4
s4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, 10, 6,
      9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
# 16*4
s5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, 4, 2,
      1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
# 16*4
s6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, 9, 14,
      15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
# 16*4
s7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6, 1, 4,
      11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
# 16*4
s8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, 7, 11,
      4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
# 7*4
key_dc = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
# 7*4
key_dd = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
# 12*4
key_final_d = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37,
               47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

un_final_d = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47,
              39, 31, 23, 15, 7, 56, 48, 40, 32, 24, 16, 8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20,
              12, 4, 62, 54, 46, 38, 30, 22, 14, 6]
un_half_d = [8, 16, 22, 30, 12, 27, 1, 17, 23, 15, 29, 5, 25, 19, 9, 0, 7, 13, 24, 2, 3, 28, 10, 18, 31, 11, 21, 6, 4,
             26, 14, 20]
un_initial_d = [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44,
                12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17,
                57, 25, 32, 0, 40, 8, 48, 16, 56, 24]


def read_txt(path):
    with open(path) as file:
        text = file.read()
    file.close()
    return (text)


def bin_to_txt(result_text):
    res = ''
    i = 0
    tmp_txt = result_text
    while len(tmp_txt) != 0:
        tmp_ord_bin = tmp_txt[(len(tmp_txt) - 11):len(tmp_txt)]
        tmp_txt = tmp_txt[0:(len(tmp_txt) - 11)]
        tmp_ord = int(tmp_ord_bin, 2)
        if tmp_ord != 0:
            res = chr(tmp_ord) + res
        i += 1
    return (res)
# print('unshifr: ', res)
def chr_to_bin(text):
    i = 0
    s = ''
    while i < len(text):
        tmp_ord = ord(text[i])
        tmp_s = '{0:b}'.format(tmp_ord)
        while len(tmp_s) % 11 != 0:
            tmp_s = '0' + tmp_s
        s += tmp_s
        i += 1
    while len(s) % 64 != 0:
        s = '0' + s
    return (s)


def f1(x):
    a = 4
    b = 101
    x = ((a * x) + b)
    return (x)


def f2(x):
    a = 3
    b = 92
    x = ((x / a) + b)
    return (x)


def gpsc(x):
    i = 0
    mas = []
    while i < 100:
        # print('%f'%x)

        if i % 2 == 0:
            x = f1(x)
        else:
            x = f2(x)
        if x < min_key:
            x = f1(x)
        if x > max_key:
            x = f2(x)
        mas.append(int(x))
        i += 1
    rnd_num = int(rnd.uniform(0, 99))
    key = lc.find_primes(mas[rnd_num], 100, 1)
    tmp = '{0:b}'.format(key[0])
    while len(tmp) != 64:
        tmp = '0' + tmp
    return (tmp)


def key_inc(key64):
    # key56=key64[0:7]+key64[8:15]+key64[16:23]+key64[24:31]+key64[32:39]+key64[40:47]+key64[48:55]+key64[56:63]
    key_mas = []
    j = 1
    key28c = ''
    key28d = ''
    i = 0
    while i < 28:
        key28c += key64[key_dc[i] - 1]
        key28d += key64[key_dd[i] - 1]
        i += 1
    while j <= 16:
        if j in [1, 2, 9, 16]:
            key28c1 = key28c[1:28] + key28c[0]
            key28d1 = key28d[1:28] + key28d[0]
        else:
            key28c1 = key28c[2:28] + key28c[0:2]
            key28d1 = key28d[2:28] + key28d[0:2]
        key28c = key28c1
        key28d = key28d1
        key56 = key28c1 + key28d1
        key48 = ''
        k = 0
        while k < 48:
            key48 += key56[key_final_d[k] - 1]
            k += 1
        key_mas.append(key48)
        j += 1
    return (key_mas)


def func_f(b, key):
    ext_b = b[31] + b[0] + b[1] + b[2] + b[3] + b[4] + b[3] + b[4] + b[5] + b[6] + b[7] + b[8] + b[7] + b[8] + b[9] + b[
        10] + b[11] + b[12] + b[11] + b[12] + b[13] + b[14] + b[15] + b[16] + b[15] + b[16] + b[17] + b[18] + b[19] + b[
                20] + b[19] + b[20] + b[21] + b[22] + b[23] + b[24] + b[23] + b[24] + b[25] + b[26] + b[27] + b[28] + b[
                27] + b[28] + b[29] + b[30] + b[31] + b[0]
    i = 0
    xor_res = ''
    while i < 48:
        if key[i] == ext_b[i]:
            xor_res += '0'
        else:
            xor_res += '1'
        i += 1
    aft_s = func_s(xor_res[0:6], s1) + func_s(xor_res[6:12], s2) + func_s(xor_res[12:18], s3) + func_s(xor_res[18:24],
                                                                                                       s4) + func_s(
        xor_res[24:30], s5) + func_s(xor_res[30:36], s6) + func_s(xor_res[36:42], s7) + func_s(xor_res[42:48], s8)
    j = 0
    result = ''
    while j < 32:
        result += aft_s[half_d[j] - 1]
        j += 1
    return (result)


def func_s(bp, s):
    strg = int(bp[0] + bp[5], 2)
    clmn = int(bp[1:5], 2)
    res = s[strg * 16 + clmn]
    res = '{0:b}'.format(res)
    res = '{:0>4}'.format(res)
    return (res)


def iround(a, b, k):
    ai = b
    f_res = func_f(b, k)
    i = 0
    bi = ''
    while i < 32:
        if a[i] == f_res[i]:
            bi += '0'
        else:
            bi += '1'
        i += 1
    return (ai, bi)


def algoritmBlock(a, b, k):
    ai = b
    mas_key = key_inc(k)
    # print("a", a)
    f_res = algoritm64(b, mas_key)
    i = 0
    bi = ''
    while i < 64:
        if a[i] == f_res[i]:
            bi += '0'
        else:
            bi += '1'
        i += 1
    return (ai, bi)

def un_algoritmBlock(a, b, k):
    # ai = b
    mas_key = key_inc(k)
    # print("a", a)
    f_res = un_algoritm64(a, mas_key)
    i = 0
    bi = ''
    while i < 64:
        if b[i] == f_res[i]:
            bi += '0'
        else:
            bi += '1'
        i += 1
    return (bi)
def algoritm64(text, key_mas):
    i = 0
    initial = ''
    while i < 64:
        initial += text[initial_d[i] - 1]
        i += 1
    a = initial[0:32]
    b = initial[32:64]
    iter = 1
    while iter <= 15:
        a1 = a
        b1 = b
        a, b = iround(a1, b1, key_mas[iter - 1])
        iter += 1
    a1 = a
    b1 = b
    b, a = iround(a1, b1, key_mas[15])
    res64 = a + b
    i = 0
    final = ''
    while i < 64:
        final += res64[final_d[i] - 1]
        i += 1
    return (final)
    # return(res64)


def un_algoritm64(text, key_mas):
    i = 0
    initial = ''
    while i < 64:
        initial += text[un_final_d[i]]
        i += 1
    a = initial[0:32]
    b = initial[32:64]
    iter = 1
    while iter <= 15:
        a1 = a
        b1 = b
        a, b = iround(a1, b1, key_mas[16 - iter])
        iter += 1
    a1 = a
    b1 = b
    b, a = iround(a1, b1, key_mas[0])
    res64 = a + b
    i = 0
    final = ''
    while i < 64:
        final += res64[un_initial_d[i]]
        i += 1
    return (final)
    # return(res64)


def algoritmBlocks(text, keys):
    # write_txt(key, 'key.txt')
    j = 0
    result_text = ''
    while j < (len(text) / 128):
        # text128 = text[j * 128:128 * (j + 1)]

        text64a = text[j * 128:128 * j + 64]
        text64b = text[128 * j + 64:128 * (j + 1)]

        # print("text64a",text64a)
        # mas_key = key_inc(keys[0])
        while iter <= 15:
            a1 = a
            b1 = b
            a, b = iround(a1, b1, key_mas[iter - 1])
            iter += 1
        a1 = a
        b1 = b
        b, a = iround(a1, b1, key_mas[15])
        res64 = a + b
        a = algoritmBlock(text64a, text64b, keys[0])
        b = algoritmBlock(text64b, text64a, keys[1])
        # a, b = algoritmBlock(a, b, keys[2])

        # result_text += algoritm64(text64, mas_key)
        result_text += a + b

        j += 1
    write_txt(result_text, 'res.txt')
    return (result_text)


def algoritm(text, key):
    write_txt(key, 'key.txt')
    mas_key = key_inc(key)
    j = 0
    result_text = ''
    while j < (len(text) / 64):
        text64 = text[j * 64:64 * (j + 1)]
        result_text += algoritm64(text64, mas_key)
        j += 1
    write_txt(result_text, 'res.txt')
    return (result_text)


def write_txt(shifr, path):
    txt_file = open(path, "w")
    for item in shifr:
        txt_file.write(item)
    txt_file.close()


def un_algoritm(text, key):
    mas_key = key_inc(key)
    j = 0
    result_text = ''
    while j < (len(text) / 64):
        text64 = text[j * 64:64 * (j + 1)]
        result_text += un_algoritm64(text64, mas_key)
        j += 1
    write_txt(result_text, 'un_shifr.txt')
    return (result_text)
def un_algoritmBlocks(text, keys):
    # mas_key = key_inc(key)
    j = 0
    result_text = ''
    while j < (len(text) / 128):
        text64a = text[j * 128:128 * j + 64]
        text64b = text[128 * j + 64:128 * (j + 1)]

        a  = un_algoritmBlock(text64a, text64b, keys[0])
        b = un_algoritmBlock(text64b, text64a, keys[1])
        # a, b = un_algoritmBlock(a, b, keys[2])

        # result_text += un_algoritm64(text64, mas_key)
        result_text += a + b
        j += 1
    write_txt(result_text, 'un_shifr.txt')
    return (result_text)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
