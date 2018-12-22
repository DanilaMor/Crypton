import random as rnd
import secrets
from random import randint


def main():
    text = 'Я, Пухов Дмитрий Денисович'
    cr = chrToBin(text)
    key = generatorKey()
    cr2 = algorithm(cr, key)

    unshifr = un_algorithm(cr2, key)
    result = bin_to_txt(unshifr)
    print("result -> ", result)


transOrig = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
             40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13,
             5, 63, 55, 47, 39, 31, 23, 15, 7]
transF = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
          11, 4, 25]
transFinal = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45,
              13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18,
              58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
s1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8, 4, 1,
      14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
s2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5, 0, 14,
      7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
s3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1, 13, 6,
      4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
s4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9, 10, 6,
      9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
s5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, 4, 2,
      1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
s6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, 9, 14,
      15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
s7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6, 1, 4,
      11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
s8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, 7, 11,
      4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
keyExpC = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36]
keyExpD = [63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
keyComprFin = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37,
               47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
un_final_d = [57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47,
              39, 31, 23, 15, 7, 56, 48, 40, 32, 24, 16, 8, 0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20,
              12, 4, 62, 54, 46, 38, 30, 22, 14, 6]
un_half_d = [8, 16, 22, 30, 12, 27, 1, 17, 23, 15, 29, 5, 25, 19, 9, 0, 7, 13, 24, 2, 3, 28, 10, 18, 31, 11, 21, 6, 4,
             26, 14, 20]
un_initial_d = [39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44,
                12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17,
                57, 25, 32, 0, 40, 8, 48, 16, 56, 24]


def chrToBin(text):
    i = 0
    cr = ''
    while i < len(text):
        chrOrd = ord(text[i])
        binCr = '{0:b}'.format(chrOrd)
        while len(binCr) % 11 != 0:
            binCr = '0' + binCr
        cr += binCr
        i += 1
    while len(cr) % 64 != 0:
        cr = '0' + cr
    return (cr)


def generate(n):
    return secrets.randbits(n)


def expmode(base, exp, m):
    if (exp == 0):
        return 1
    elif (exp % 2 == 0):
        return (expmode(base, exp // 2, m)) ** 2 % m
    else:
        return (base * expmode(base, exp - 1, m)) % m


def simple(n):
    a = rnd.randint(2, n - 1)
    return expmode(a, n - 1, n) == 1


def test_ferma(n):
    for i in range(100):
        if (not simple(n)):
            return False
    return True


def generatorKey():
    c = 1442695040888963407
    a = 6364136223846793005
    m = 2 ** 64
    n = generate(64) % m
    while (not test_ferma(n)):
        n = (a * n + c) % m
        print(n)
    n = '{0:b}'.format(n)
    while len(n) != 64:
        n = '0' + n
    return n


def keyExp(key64):
    keyMas = []
    k = 1
    key28c = ''
    key28d = ''
    i = 0
    while i < 28:
        key28c += key64[keyExpC[i] - 1]
        key28d += key64[keyExpD[i] - 1]
        i += 1
    while k <= 16:
        if k in [1, 2, 9, 16]:
            key28c1 = key28c[1:28] + key28c[0]
            key28d1 = key28d[1:28] + key28d[0]
        else:
            key28c1 = key28c[2:28] + key28c[0:2]
            key28d1 = key28d[2:28] + key28d[0:2]
        key28c = key28c1
        key28d = key28d1
        key56 = key28c1 + key28d1
        key48 = ''
        j = 0
        while j < 48:
            key48 += key56[keyComprFin[j] - 1]
            j += 1
        keyMas.append(key48)
        k += 1
    return (keyMas)


def funcOfReolace(xor, s):
    strng = int(xor[0] + xor[5], 2)
    col = int(xor[1:5], 2)
    result = s[strng * 16 + col]
    result = '{0:b}'.format(result)
    result = '{:0>4}'.format(result)
    return (result)


def func_f(b, key):
    EpB = b[31] + b[0] + b[1] + b[2] + b[3] + b[4] + b[3] + b[4] + b[5] + b[6] + b[7] + b[8] + b[7] + b[8] + b[9] + b[
        10] + b[11] + b[12] + b[11] + b[12] + b[13] + b[14] + b[15] + b[16] + b[15] + b[16] + b[17] + b[18] + b[19] + b[
              20] + b[19] + b[20] + b[21] + b[22] + b[23] + b[24] + b[23] + b[24] + b[25] + b[26] + b[27] + b[28] + b[
              27] + b[28] + b[29] + b[30] + b[31] + b[0]
    i = 0
    xorResult = ''
    while i < 48:
        if key[i] == EpB[i]:
            xorResult += '0'
        else:
            xorResult += '1'
        i += 1
    replaceS = funcOfReolace(xorResult[0:6], s1) + funcOfReolace(xorResult[6:12], s2) + funcOfReolace(xorResult[12:18],
                                                                                                      s3) + funcOfReolace(
        xorResult[18:24], s4) + funcOfReolace(xorResult[24:30], s5) + funcOfReolace(xorResult[30:36],
                                                                                    s6) + funcOfReolace(
        xorResult[36:42], s7) + funcOfReolace(xorResult[42:48], s8)
    j = 0
    result = ''
    while j < 32:
        result += replaceS[transF[j] - 1]
        j += 1
    return (result)


def algoritm64(text, keyMas):
    i = 0
    initial = ''
    while i < 64:
        initial += text[transOrig[i] - 1]
        i += 1
    a = initial[0:32]
    b = initial[32:64]
    iter = 1
    while iter <= 15:
        tmp_key = keyMas[iter - 1]
        a1 = a
        b1 = b
        a, b = iround(a1, b1, keyMas[iter - 1])
        if (tmp_key[0] == '1') and (iter > 1):
            a2 = a
            a = b
            b = a2
        iter += 1
    a1 = a
    b1 = b
    b, a = iround(a1, b1, keyMas[15])
    res64 = a + b
    i = 0
    final = ''
    while i < 64:
        final += res64[transFinal[i] - 1]
        i += 1
    return (final)


def iround(a, b, key):
    ai = b
    funcB = func_f(b, key)
    i = 0
    bi = ''
    while i < 32:
        if a[i] == funcB[i]:
            bi += '0'
        else:
            bi += '1'
        i += 1
    return (ai, bi)


def algorithm(text, key):
    masKey = keyExp(key)
    j = 0
    result_text = ''
    while j < (len(text) / 64):
        text64 = text[j * 64:64 * (j + 1)]
        result_text += algoritm64(text64, masKey)
        j += 1
    print("result_text=", result_text)
    return (result_text)


def un_algorithm64(cr2, keyMas):
    print('test:', cr2)
    i = 0
    initial = ''
    while i < 64:
        initial += cr2[un_final_d[i]]
        i += 1
    a = initial[0:32]
    b = initial[32:64]
    iter = 1
    while iter <= 15:
        tmp_key = keyMas[16 - iter]
        a1 = a
        b1 = b
        if (tmp_key[0] == '1') and (iter > 1):
            a2 = a1
            a1 = b1
            b1 = a2
        a, b = iround(a1, b1, keyMas[16 - iter])
        iter += 1
    a1 = a
    b1 = b
    b, a = iround(a1, b1, keyMas[0])
    res64 = a + b
    i = 0
    final = ''
    while i < 64:
        final += res64[un_initial_d[i]]
        i += 1
    return (final)
    print(final)


def un_algorithm(cr2, key):
    masKey = keyExp(key)
    j = 0
    result_text = ''
    while j < (len(cr2) / 64):
        text64 = cr2[j * 64:64 * (j + 1)]
        result_text += un_algorithm64(text64, masKey)
        j += 1

    return (result_text)
    # print('un: ', result_text)


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


if __name__ == "__main__":
    main()