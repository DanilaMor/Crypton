import os
import math
import secrets
import decimal
from random import randint

from bitstring import BitArray
from numpy import byte, unicode
import numpy as numpy
import sys
# sys.setdefaultencoding() does not exist, here!
# reload(sys)  # Reload does the trick!


# print("heloo")
# b = b'\x63'
# b = BitArray(b).int
# b = b >> 1
# # sdvig = BitArray(1)
# # b = b.bin << sdvig.bin
# print(b)
# b = BitArray(b)
# print(b)


def getSTable():
    S0 = ["63", "ec", "59", "aa", "db", "8e", "66", "c0", "37", "3c", "14", "ff", "13", "44", "a9", "91",
          "3b", "78", "8d", "ef", "c2", "2a", "f0", "d7", "61", "9e", "a5", "bc", "48", "15", "12", "47",
          "ed", "42", "1a", "33", "38", "c8", "17", "90", "a6", "d5", "5d", "65", "6a", "fe", "8f", "a1",
          "93", "c2", "2f", "0c", "68", "58", "df", "f4", "45", "11", "a0", "a7", "22", "96", "fb", "7d",
          "1d", "b4", "84", "e0", "bf", "57", "e9", "0a", "4e", "83", "cc", "7a", "71", "39", "c7", "32",
          "74", "3d", "de", "50", "85", "06", "6f", "53", "e8", "ad", "82", "19", "e1", "ba", "36", "cb",
          "0e", "28", "f3", "9b", "4a", "62", "94", "1f", "bd", "f6", "67", "41", "d8", "d1", "2d", "a4",
          "86", "b7", "01", "c5", "b0", "75", "02", "f9", "2c", "29", "6e", "d2", "f5", "8b", "fc", "5a",
          "e4", "7f", "dd", "07", "55", "b1", "2b", "89", "72", "18", "3a", "4c", "b6", "e3", "80", "ce",
          "49", "cf", "6b", "b9", "f2", "0d", "dc", "64", "95", "46", "f7", "10", "9a", "20", "a2", "3f",
          "d6", "87", "70", "3e", "21", "fd", "4d", "7b", "3c", "ae", "09", "8a", "04", "b3", "54", "f8",
          "30", "00", "56", "d4", "e7", "25", "bb", "ac", "98", "73", "ea", "c9", "9d", "4f", "7e", "03",
          "ab", "92", "a8", "43", "0f", "fa", "24", "5c", "1e", "60", "31", "97", "cd", "c6", "79", "f5",
          "5e", "e5", "34", "76", "1c", "81", "b2", "af", "0b", "5d", "d9", "e2", "27", "6d", "d0", "88",
          "c1", "51", "e6", "9c", "77", "be", "99", "23", "da", "eb", "52", "2e", "b5", "08", "05", "6c",
          "b8", "1b", "a3", "69", "8c", "d3", "40", "26", "f1", "c4", "9f", "35", "ee", "7c", "4b", "16"]

    S1 = ["8d", "b3", "65", "aa", "6f", "3a", "99", "03", "dc", "f0", "50", "ff", "4c", "11", "a6", "46",
          "ec", "e1", "36", "bf", "0b", "a8", "c3", "5f", "85", "7a", "96", "f2", "21", "54", "48", "1d",
          "b7", "09", "68", "cc", "e0", "23", "5c", "42", "9a", "57", "75", "95", "a9", "fb", "3e", "86",
          "4e", "2b", "bc", "30", "a1", "61", "7f", "d3", "15", "44", "82", "9e", "88", "5a", "Ef", "f5",
          "74", "d2", "12", "83", "fe", "5d", "a7", "28", "39", "0e", "33", "e9", "c5", "e4", "1f", "c8",
          "d1", "f4", "7b", "41", "16", "18", "bd", "4d", "a3", "b6", "0a", "64", "87", "ea", "d8", "2f",
          "38", "a0", "cf", "6e", "29", "89", "52", "7c", "f6", "db", "9d", "05", "63", "47", "b4", "92",
          "1a", "de", "04", "17", "c2", "d5", "08", "e7", "b0", "a4", "b9", "4b", "7d", "2e", "f3", "69",
          "93", "fd", "77", "1c", "55", "c6", "ac", "26", "c9", "60", "e8", "31", "da", "8f", "02", "3b",
          "25", "3f", "ad", "e6", "cb", "34", "73", "91", "56", "19", "df", "40", "6a", "80", "8a", "fc",
          "5b", "1e", "c1", "f8", "84", "f7", "35", "ed", "0f", "ba", "24", "2a", "10", "ce", "51", "e3",
          "c0", "00", "59", "53", "9f", "94", "ee", "b2", "62", "cd", "ab", "27", "76", "3d", "f9", "0c",
          "ae", "4a", "a2", "0d", "3c", "eb", "90", "71", "78", "81", "c4", "5e", "37", "1b", "e5", "d7",
          "79", "97", "d0", "d9", "70", "06", "ca", "be", "2c", "6d", "67", "8b", "9c", "b5", "43", "22",
          "07", "45", "9b", "72", "dd", "fa", "66", "8c", "6b", "af", "49", "b8", "d6", "20", "14", "b1",
          "e2", "6c", "8e", "a5", "32", "4f", "01", "98", "c7", "13", "7e", "d4", "bb", "f1", "2d", "58"]

    S2 = ["b1", "72", "76", "bf", "ac", "ee", "55", "83", "ed", "aa", "47", "d8", "33", "95", "60", "c4",
          "9b", "39", "1e", "0c", "0a", "1d", "ff", "26", "89", "5b", "22", "f1", "d4", "40", "c8", "67",
          "9d", "a4", "3c", "e7", "c6", "b5", "f7", "dc", "61", "79", "15", "86", "78", "6e", "eb", "32",
          "b0", "ca", "4f", "23", "d2", "fb", "5e", "08", "24", "4d", "8a", "10", "09", "51", "a3", "9f",
          "f6", "6b", "21", "c3", "0d", "38", "99", "1f", "1c", "90", "64", "fe", "8b", "a6", "48", "bd",
          "53", "e1", "ea", "57", "ae", "84", "b2", "45", "35", "02", "7f", "d9", "c7", "2a", "d0", "7c",
          "c9", "18", "65", "00", "97", "2b", "06", "6a", "34", "f3", "2c", "92", "ef", "dd", "7a", "56",
          "a2", "c4", "88", "b9", "50", "75", "d3", "e4", "11", "ce", "4b", "a7", "fd", "3f", "be", "81",
          "8e", "d5", "5a", "49", "42", "54", "70", "a1", "df", "87", "ab", "7d", "f4", "12", "05", "2e",
          "27", "0f", "c1", "30", "66", "98", "3d", "cb", "b8", "e6", "9c", "63", "e3", "bc", "19", "fa",
          "3a", "2f", "9e", "f2", "6f", "1a", "28", "3b", "c2", "0e", "03", "c0", "b7", "59", "a9", "d7",
          "74", "85", "d6", "ad", "41", "ec", "8c", "71", "f0", "93", "5d", "b6", "1b", "68", "e5", "44",
          "07", "e0", "14", "8a", "f9", "73", "cd", "4e", "25", "bb", "31", "5f", "4a", "cc", "8f", "91",
          "de", "6d", "7b", "f5", "b3", "29", "a0", "17", "6c", "da", "e8", "04", "96", "82", "52", "36",
          "43", "5c", "db", "8d", "80", "d1", "e2", "b4", "58", "46", "ba", "e9", "01", "20", "fc", "13",
          "16", "f8", "94", "62", "37", "cf", "69", "9a", "af", "77", "c5", "3e", "7e", "a5", "2d", "0b"]

    S3 = ["b1", "f6", "8e", "07", "72", "6b", "d5", "e0", "76", "21", "5a", "14", "bf", "c3", "49", "a8", "ac", "0d",
          "42", "f9", "ee", "38", "54", "73", "55", "99", "70", "cd", "83", "1f", "a1", "4e", "ed", "1c", "df", "25",
          "aa", "90", "87", "bb", "47", "64", "ab", "31", "d8", "fe", "7d", "5f", "33", "8b", "f4", "4a", "95", "a6",
          "12", "cc", "60", "48", "05", "8f", "c4", "bd", "2e", "91", "9b", "53", "27", "de", "39", "e1", "0f", "6d",
          "1e", "ea", "c1", "7b", "0c", "57", "30", "f5", "0a", "ae", "66", "b3", "1d", "84", "98", "29", "ff", "b2",
          "3d", "a0", "26", "45", "cb", "17", "89", "35", "b8", "6c", "5b", "02", "e6", "da", "22", "7f", "9c", "e8",
          "f1", "d9", "63", "04", "d4", "c7", "e3", "96", "40", "2a", "bc", "82", "c8", "d0", "19", "52", "67", "7c",
          "fa", "36", "9d", "c9", "3a", "43", "a4", "18", "2f", "5c", "3c", "65", "9e", "db", "e7", "00", "f2", "8d",
          "c6", "97", "6f", "80", "b5", "2b", "1a", "d1", "f7", "06", "28", "e2", "dc", "6a", "3b", "b4", "61", "34",
          "c2", "58", "79", "f3", "0e", "46", "15", "2c", "03", "ba", "86", "92", "c0", "e9", "78", "ef", "b7", "01",
          "6e", "dd", "59", "20", "eb", "7a", "a9", "fc", "32", "56", "d7", "13", "b0", "a2", "74", "16", "ca", "4c",
          "85", "f8", "4f", "88", "d6", "94", "23", "b9", "ad", "62", "d2", "50", "41", "37", "fb", "75", "ec", "cf",
          "5e", "d3", "8c", "69", "08", "e4", "71", "9a", "24", "11", "f0", "af", "4d", "ce", "93", "77", "8a", "4b",
          "5d", "c5", "10", "a7", "b6", "3e", "09", "fd", "1b", "7e", "51", "3f", "68", "a5", "a3", "be", "e5", "2d",
          "9f", "81", "44", "0b", ]
    SS = [S0, S1, S2, S3]
    return SS


def funcYe(a, i, j):
    # print("a -> " + str(a))
    indexS = (j + i + 2) % 4
    SS = getSTable()
    tableS = SS[indexS]
    print("a")
    print(a)
    print(chr(a))
    b = int(tableS[a], 16)
    return b


def funcY0(a, i, j):
    # print("a -> " + str(a))
    indexS = (j + i) % 4
    SS = getSTable()
    tableS = SS[indexS]
    b = int(tableS[a], 16)
    return b


#
# a = 0
# b = funcYe(a, 0, 0)
# print("b -> " + str(funcY0(b, 0, 0)))


def getAandM(A, M, iA, iM):
    list = []
    for j in range(4):
        list.append(A[iA][j] & M[iM][j])
    return list


def getXor(A, B, C, D):
    list = []
    for i in range(4):
        list.append(A[i] ^ B[i] ^ C[i] ^ D[i])
    return list


def getXorFor2(A, B):
    list = []
    for i in range(4):
        list.append(A[i] ^ B[i])
    return list


def linePi0(A):
    B = []
    BB = []
    m0 = BitArray(b'\xFC').hex
    m1 = BitArray(b'\xF3').hex
    m2 = BitArray(b'\xCF').hex
    m3 = BitArray(b'\x3f').hex

    M0 = int(m3 + m2 + m1 + m0, 16)
    M1 = int(m0 + m3 + m2 + m1, 16)
    M2 = int(m1 + m0 + m3 + m2, 16)
    M3 = int(m2 + m1 + m0 + m3, 16)

    print("M0")
    print(M0)
    print("M1")
    print(M1)
    print("M2")
    print(M2)
    print("M3")
    print(M3)
    AA = []
    for i in range(4):
        s = ""
        for a in A[i]:
            # print("a.hex")
            # print(a)
            s += BitArray(hex(a)).hex
        AA.append(int(s, 16))
    # print((A[3] & M3) ^ (A[2] & M2) ^ (A[1] & M1) ^ (A[0] & M0))
    BB.append((AA[3] & M3) ^ (AA[2] & M2) ^ (AA[1] & M1) ^ (AA[0] & M0))
    BB.append((AA[3] & M0) ^ (AA[2] & M3) ^ (AA[1] & M2) ^ (AA[0] & M1))
    BB.append((AA[3] & M1) ^ (AA[2] & M0) ^ (AA[1] & M3) ^ (AA[0] & M2))
    BB.append((AA[3] & M2) ^ (AA[2] & M1) ^ (AA[1] & M0) ^ (AA[0] & M3))

    for i in range(4):
        s = BitArray(hex(BB[i])).hex
        b = []
        for j in range(4):
            ss = s[j * 2:j * 2 + 2]
            b.append(int(ss, 16))
        B.append(b)
    return B


def linePi0V1(A):
    B = []
    BB = []
    m0 = BitArray(b'\xFC').hex
    m1 = BitArray(b'\xF3').hex
    m2 = BitArray(b'\xCF').hex
    m3 = BitArray(b'\x3F').hex

    M = []
    M.append([int(m3, 16), int(m2, 16), int(m1, 16), int(m0, 16)])
    M.append([int(m0, 16), int(m3, 16), int(m2, 16), int(m1, 16)])
    M.append([int(m1, 16), int(m0, 16), int(m3, 16), int(m2, 16)])
    M.append([int(m2, 16), int(m1, 16), int(m0, 16), int(m3, 16)])

    print("M0")
    print(M)
    # print("M1")
    # print(M1)
    # print("M2")
    # print(M2)
    # print("M3")
    # print(M3)
    # AA = []
    # for i in range(4):
    #     s = ""
    #     for a in A[i]:
    #         # print("a.hex")
    #         # print(a)
    #         s += BitArray(hex(a)).hex
    #     AA.append(int(s, 16))
    # # print((A[3] & M3) ^ (A[2] & M2) ^ (A[1] & M1) ^ (A[0] & M0))
    BB.append(getXor(getAandM(A, M, 3, 3), getAandM(A, M, 2, 2), getAandM(A, M, 1, 1), getAandM(A, M, 0, 0)))
    BB.append(getXor(getAandM(A, M, 3, 0), getAandM(A, M, 2, 3), getAandM(A, M, 1, 2), getAandM(A, M, 0, 1)))
    BB.append(getXor(getAandM(A, M, 3, 1), getAandM(A, M, 2, 0), getAandM(A, M, 1, 3), getAandM(A, M, 0, 2)))
    BB.append(getXor(getAandM(A, M, 3, 2), getAandM(A, M, 2, 1), getAandM(A, M, 1, 0), getAandM(A, M, 0, 3)))

    # for i in range(4):
    #     s = BitArray(hex(BB[i])).hex
    #     b = []
    #     for j in range(4):
    #         ss = s[j * 2:j * 2 + 2]
    #         b.append(int(ss, 16))
    #     B.append(b)
    return BB


# b = linePi0([0,1,2,3])
# print(b)
def linePieV1(A):
    B = []
    BB = []
    m0 = BitArray(b'\xFC').hex
    m1 = BitArray(b'\xF3').hex
    m2 = BitArray(b'\xCF').hex
    m3 = BitArray(b'\x3f').hex

    # M0 = int(m3 + m2 + m1 + m0, 16)
    # M1 = int(m0 + m3 + m2 + m1, 16)
    # M2 = int(m1 + m0 + m3 + m2, 16)
    # M3 = int(m2 + m1 + m0 + m3, 16)
    M = []
    M.append([int(m3, 16), int(m2, 16), int(m1, 16), int(m0, 16)])
    M.append([int(m0, 16), int(m3, 16), int(m2, 16), int(m1, 16)])
    M.append([int(m1, 16), int(m0, 16), int(m3, 16), int(m2, 16)])
    M.append([int(m2, 16), int(m1, 16), int(m0, 16), int(m3, 16)])
    # AA = []
    # for i in range(4):
    #     s = ""
    #     for a in A[i]:
    #         # print("a.hex")
    #         # print(a)
    #         s += BitArray(hex(a)).hex
    #     AA.append(int(s, 16))
    #
    # print(AA)
    # for i in range(4):
    #     print(BitArray(hex(AA[i])).bin)
    # BB.append((AA[3] & M1) ^ (AA[2] & M0) ^ (AA[1] & M3) ^ (AA[0] & M2))
    # BB.append((AA[3] & M2) ^ (AA[2] & M1) ^ (AA[1] & M0) ^ (AA[0] & M3))
    # BB.append((AA[3] & M3) ^ (AA[2] & M2) ^ (AA[1] & M1) ^ (AA[0] & M0))
    # BB.append((AA[3] & M0) ^ (AA[2] & M3) ^ (AA[1] & M2) ^ (AA[0] & M1))
    BB.append(getXor(getAandM(A, M, 3, 1), getAandM(A, M, 2, 0), getAandM(A, M, 1, 3), getAandM(A, M, 0, 2)))
    BB.append(getXor(getAandM(A, M, 3, 2), getAandM(A, M, 2, 1), getAandM(A, M, 1, 0), getAandM(A, M, 0, 3)))
    BB.append(getXor(getAandM(A, M, 3, 3), getAandM(A, M, 2, 2), getAandM(A, M, 1, 1), getAandM(A, M, 0, 0)))
    BB.append(getXor(getAandM(A, M, 3, 0), getAandM(A, M, 2, 3), getAandM(A, M, 1, 2), getAandM(A, M, 0, 1)))
    # for i in range(4):
    #     s = BitArray(hex(BB[i])).hex
    #     b = []
    #     for j in range(4):
    #         ss = s[j * 2:j * 2 + 2]
    #         b.append(int(ss, 16))
    #     B.append(b)
    return BB


def linePie(A):
    B = []
    BB = []
    m0 = BitArray(b'\xFC').hex
    m1 = BitArray(b'\xF3').hex
    m2 = BitArray(b'\xCF').hex
    m3 = BitArray(b'\x3f').hex

    M0 = int(m3 + m2 + m1 + m0, 16)
    M1 = int(m0 + m3 + m2 + m1, 16)
    M2 = int(m1 + m0 + m3 + m2, 16)
    M3 = int(m2 + m1 + m0 + m3, 16)

    AA = []
    for i in range(4):
        s = ""
        for a in A[i]:
            # print("a.hex")
            # print(a)
            s += BitArray(hex(a)).hex
        AA.append(int(s, 16))

    print(AA)
    for i in range(4):
        print(BitArray(hex(AA[i])).bin)
    BB.append((AA[3] & M1) ^ (AA[2] & M0) ^ (AA[1] & M3) ^ (AA[0] & M2))
    BB.append((AA[3] & M2) ^ (AA[2] & M1) ^ (AA[1] & M0) ^ (AA[0] & M3))
    BB.append((AA[3] & M3) ^ (AA[2] & M2) ^ (AA[1] & M1) ^ (AA[0] & M0))
    BB.append((AA[3] & M0) ^ (AA[2] & M3) ^ (AA[1] & M2) ^ (AA[0] & M1))

    for i in range(4):
        s = BitArray(hex(BB[i])).hex
        b = []
        for j in range(4):
            ss = s[j * 2:j * 2 + 2]
            b.append(int(ss, 16))
        B.append(b)
    return B


def tau(A):
    A = numpy.array(A)
    return A.transpose().tolist()


def sigma(A, K):
    for i in range(4):
        for j in range(4):
            A[i][j] = A[i][j] ^ K[i][j]
    return A


# linePi0()

def isProstoeNumber(n):
    # n = int(input())
    print("Number -> " + str(n))
    flag = False
    if n < 2:
        print("A number must be 2 and more")
        return flag
    elif n == 2:
        print("It's prime number")
        return flag

    i = 2
    try:
        limit = int(math.sqrt(n))
    except(Exception):
        d = decimal.Decimal(n)
        d.sqrt()
        # limit = int(n // 2)
        limit = int(str(d))
    while i <= limit:
        if n % i == 0:
            print("This is composite number")
            return flag
        i += 1

    print("It's prime number")
    flag = True
    return flag


def expmod(base, exp, m):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return (expmod(base, exp // 2, m)) ** 2 % m
    else:
        return (base * expmod(base, exp - 1, m)) % m


def isProstoeNumberV1(n):
    a = randint(2, n - 1)
    return expmod(a, n - 1, n) == 1

def isProstoeNumberV2(n):
    for i in range(100):
        if (not isProstoeNumberV1(n)):
            return False
    return True


def generate(n):
    # print(secrets.randbits(n))
    # return os.urandom(n)
    return secrets.randbits(n)


def getProstoeNumber(n):
    num = generate(n)
    while not isProstoeNumberV1(num):
        num = generate(n)
    print("result -> " + str(num))
    return num


def printIntAsHex(num):
    # if str(num.__class__) == str(list.__class__):
    if isinstance(num, list):
        for i in num:
            printIntAsHex(i)
        print("---")
    if isinstance(num, int):
        print(str(hex(num)))


def raund(mat, key, numRaund):
    # text = bytes("lol_lol_lol_lol_l", "utf8")
    # mat = []
    # list0 = []
    # for i in range(4):
    #     for j in range(4):
    #         list0.append(text[i * 4 + j])
    #     mat.append(list0)
    #     list0 = []
    # print(mat)

    #### preobrazovanie
    # mat = num.array(mat)
    flag = numRaund % 2 == 1
    print("mat -> ")
    print(mat)
    mat = Sij(mat, flag)
    print("mat1 -> ")
    print(mat)
    if (flag):
        mat = linePi0V1(mat)
    else:
        mat = linePieV1(mat)
    print("mat2 -> ")
    print(mat)
    mat = tau(mat)
    print("mat3 -> ")
    print(mat)
    mat = sigma(mat, key)
    print("mat4 -> ")
    print(mat)
    return mat


def raundDecode(mat, key, numRaund):
    flag = numRaund % 2 == 1
    print("mat4s -> ")
    print(mat)
    mat = sigma(mat, key)

    print("mat3d -> ")
    print(mat)

    mat = tau(mat)
    print("mat2d -> ")
    print(mat)
    if flag:
        mat = linePi0V1(mat)
    else:
        mat = linePieV1(mat)
    print("mat1d -> ")
    print(mat)
    mat = Sij(mat, not flag)
    print("matd -> ")
    print(mat)
    return mat


def generationKe(K):
    U = []
    V = []
    Ke = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(4):
        str0 = BitArray(K[8 * i + 6]).hex + BitArray(K[8 * i + 4]).hex + BitArray(K[8 * i + 2]).hex + BitArray(
            K[8 * i]).hex
        U.append(int(str0, 16))
        str1 = BitArray(K[8 * i + 7]).hex + BitArray(K[8 * i + 5]).hex + BitArray(K[8 * i + 3]).hex + BitArray(
            K[8 * i + 1]).hex
        V.append(int(str1, 16))

    print("U - >")
    print(U)
    print("V - >")
    print(V)
    T0 = U[0] ^ U[1] ^ U[2] ^ U[3]
    T1 = V[0] ^ V[1] ^ V[2] ^ V[3]
    print("T0 -> " + str(hex(T0)))
    print("T0 -> " + str(hex(T1)))
    for i in range(4):
        print(i)
        Ke[i] = U[i] ^ T1
        Ke[i + 4] = V[i] ^ T0
    return Ke


def generationKeV1(K):
    U = []
    V = []
    Ke = [0, 0, 0, 0, 0, 0, 0, 0]
    # UU = []
    # VV = []
    for i in range(4):
        UU = []
        VV = []
        # str0 = BitArray(K[8 * i + 6]).hex + BitArray(K[8 * i + 4]).hex + BitArray(K[8 * i + 2]).hex + BitArray(
        #     K[8 * i]).hex
        # UU.append(int(BitArray(K[8 * i + 6]).hex, 16))
        # UU.append(int(BitArray(K[8 * i + 4]).hex, 16))
        # UU.append(int(BitArray(K[8 * i + 2]).hex, 16))
        # UU.append(int(BitArray(K[8 * i]).hex, 16))

        UU.append(int(K[8 * i + 6], 16))
        UU.append(int(K[8 * i + 4], 16))
        UU.append(int(K[8 * i + 2], 16))
        UU.append(int(K[8 * i], 16))
        # U.append(int(str0, 16))
        U.append(UU)

        # str1 = BitArray(K[8 * i + 7]).hex + BitArray(K[8 * i + 5]).hex + BitArray(K[8 * i + 3]).hex + BitArray(
        #     K[8 * i + 1]).hex
        # VV.append(int(BitArray(K[8 * i + 7]).hex, 16))
        # VV.append(int(BitArray(K[8 * i + 5]).hex, 16))
        # VV.append(int(BitArray(K[8 * i + 3]).hex, 16))
        # VV.append(int(BitArray(K[8 * i + 1]).hex, 16))

        VV.append(int(K[8 * i + 7], 16))
        VV.append(int(K[8 * i + 5], 16))
        VV.append(int(K[8 * i + 3], 16))
        VV.append(int(K[8 * i + 1], 16))
        # V.append(int(str1, 16))
        V.append(VV)

    print("U - >")
    print(U)
    print("V - >")
    print(V)

    k = []
    for i in range(4):
        kk = []
        for j in range(4):
            kk.append(0)
        k.append(kk)
    print("raund U")
    UU = raund(U, k, 1)
    VV = raund(V, k, 0)

    print("UU")
    print(UU)
    # UUU = raundDecode(UU, k, 1)
    # print("UU1")
    # print(UUU)

    # for i in range(4):
    #     for j in range(4):
    #         V[i][j] = funcYe(V[i][j],i,j)
    #         U[i][j] = funcY0(U[i][j],i,j)

    # print("U1 - >")
    # print(U)
    # print("V1 - >")
    # print(V)

    # U = linePi0(U)
    # V = linePie(V)
    # print("U2 - >")
    # print(U)
    # print("V2 - >")
    # print(V)

    # U = tau(U)
    # V = tau(V)

    # print("U3 - >")
    # print(U)
    # print("V3 - >")
    # print(V)

    # UU = sigma(U,k)
    # VV = sigma(V,k)
    # print("U4 - >")
    # print(U)
    # print("V4 - >")
    # print(V)
    # UU = sigma(UU,k)

    T0 = getXor(UU[0], UU[1], UU[2], UU[3])
    T1 = getXor(VV[0], VV[1], VV[2], VV[3])
    print("T0 -> " + str(hex(genNumForStr(T0))))
    print("T1 -> " + str(hex(genNumForStr(T1))))
    for i in range(4):
        print(i)
        Ke[i] = genNumForStr(getXorFor2(UU[i], T1))
        Ke[i + 4] = genNumForStr(getXorFor2(VV[i], T0))
    return Ke


print("BitAA")
print(BitArray(hex(23)).hex)


def Sij(A, flag):
    for i in range(4):
        for j in range(4):
            if (flag):
                A[i][j] = funcY0(A[i][j], i, j)
            else:
                A[i][j] = funcYe(A[i][j], i, j)
    return A


def genNumForStr(list):
    s = ""
    for n in list:
        if (n < 16):
            s += "0"+BitArray(hex(n)).hex
        else:
            s += BitArray(hex(n)).hex
    return int(s, 16)


def sdvig3(A, n):
    result = ""
    str0 = BitArray(hex(A)).hex
    for i in range(4):
        s = str0[i * 2:i * 2 + 2]
        result += BitArray(hex(int(s, 16) << n)).hex
    return int(result, 16)


def generationKr(numRaund, Ke):
    C0 = 0xA54FF53A
    D = 0x3C6EF372 % 2 ** 32
    # Mc0 = 0xACACACAC
    Mcc0 = [int("AC", 16), int("AC", 16), int("AC", 16), int("AC", 16)]
    # Krk = []
    Kr = []

    for i in range(numRaund):
        C0 = C0 + D
        for j in range(4):
            # print("Mcc0")
            # print(Mcc0[j])
            Mcc0[j] = Mcc0[j] << 1
    st = ""
    for j in range(4):
        if (Mcc0[j] < 16):
            st += "0"+str(BitArray(hex(Mcc0[j])).hex)
        else:
            st += BitArray(hex(Mcc0[j])).hex

    Mc0 = int(st, 16)

    print("ke")
    print(Ke)
    ke = Ke
    if (numRaund % 2 == 0):
        Ke[3] = sdvig3(ke[0], 6)
        Ke[2] = sdvig3(ke[3], 6)
        Ke[1] = ke[2] << 16
        Ke[0] = ke[1] << 24
        for i in range(4):
            Krk = []
            str0 = BitArray(hex(Ke[i] ^ C0 ^ Mc0)).hex
            for i in range(4):
                s = str0[i * 2:i * 2 + 2]
                # Krk.append(BitArray(hex(int(s, 16))).hex)
                Krk.append(int(s, 16))
            Kr.append(Krk)
    else:
        Ke[7] = ke[6] << 16
        Ke[6] = ke[5] << 8
        Ke[5] = sdvig3(ke[4], 2)
        Ke[4] = sdvig3(ke[7], 2)
        for i in range(4):
            Krk = []
            str0 = BitArray(hex(Ke[i] ^ C0 ^ Mc0)).hex
            for i in range(4):
                s = str0[i * 2:i * 2 + 2]
                # Krk.append(BitArray(hex(int(s, 16))).hex)
                Krk.append(int(s, 16))
            Kr.append(Krk)
    # print(Kr)
    # Kr.append(Krk)
    print("Ke")
    print(Ke)
    print("Kr")
    print(Kr)
    return Kr
    # printIntAsHex(Kr)


# def generateTable():
#     text = "b1	f6	8e	07	72	6b	d5	e0	76	21	5a	14	bf	c3	49	a8	ac	0d	42	f9	ee	38	54	73	55	99	70	cd	83	1f	a1	4e	ed	1c	df	25	aa	90	87	bb	47	64	ab	31	d8	fe	7d	5f	33	8b	f4	4a	95	a6	12	cc	60	48	05	8f	c4	bd	2e	91	9b	53	27	de	39	e1	0f	6d	1e	ea	c1	7b	0c	57	30	f5	0a	ae	66	b3	1d	84	98	29	ff	b2	3d	a0	26	45	cb	17	89	35	b8	6c	5b	02	e6	da	22	7f	9c	e8	f1	d9	63	04	d4	c7	e3	96	40	2a	bc	82	c8	d0	19	52	67	7c	fa	36	9d	c9	3a	43	a4	18	2f	5c	3c	65	9e	db	e7	00	f2	8d	c6	97	6f	80	b5	2b	1a	d1	f7	06	28	e2	dc	6a	3b	b4	61	34	c2	58	79	f3	0e	46	15	2c	03	ba	86	92	c0	e9	78	ef	b7	01	6e	dd	59	20	eb	7a	a9	fc	32	56	d7	13	b0	a2	74	16	ca	4c	85	f8	4f	88	d6	94	23	b9	ad	62	d2	50	41	37	fb	75	ec	cf	5e	d3	8c	69	08	e4	71	9a	24	11	f0	af	4d	ce	93	77	8a	4b	5d	c5	10	a7	b6	3e	09	fd	1b	7e	51	3f	68	a5	a3	be	e5	2d	9f	81	44	0b"
#     # f = open("1.txt", "w")
#     text = text.replace("	", ",")
#     text1 = ""
#     for num in text.split(","):
#         text1 += "\"" + num + "\","
#     f.write(text1)


def getTextForBlocks(blocks):
    text = ""
    for bloc in blocks:
        for line in bloc:
            for st in line:
                text += chr(st)
    return text


def getBlocksForText(text):
    listBloc = []
    listChar = []
    bloc = []
    countListChar = 0
    print("text size")

    for ch in text:
        # print("ch")
        # print(ch.decode('ascii'))
        # listChar.append(int(BitArray().hex,16))
        listChar.append(ord(ch))
        countListChar += 1
    print("countListChar")
    print(countListChar)
    ostatok = countListChar % 16
    print("ok")
    indexCh = 0
    indexLine = 0
    line = []
    for ch in listChar:
        line.append(ch)
        indexCh += 1
        if indexCh == 4:
            bloc.append(line)
            line = []
            indexCh = 0
            indexLine = indexLine + 1
        if indexLine == 4:
            indexLine = 0
            listBloc.append(bloc)
            bloc = []
    if ostatok != 0:
        listOstatok = []
        for i in range(countListChar - ostatok, countListChar):
            listOstatok.append(listChar[i])
        print("list ostatok")
        print(listOstatok)
        for i in range(ostatok, 16):
            listOstatok.append(ord(" "))

        indexCh = 0
        indexLine = 0
        line = []
        bloc = []
        for ch in listOstatok:
            line.append(ch)
            indexCh += 1
            if indexCh == 4:
                bloc.append(line)
                line = []
                indexCh = 0
                indexLine = indexLine + 1
            if indexLine == 4:
                indexLine = 0
                listBloc.append(bloc)
                bloc = []
    return listBloc


def fe(A):
    A = tau(A)
    A = linePieV1(A)
    A = tau(A)
    return A


def f0(A):
    A = tau(A)
    A = linePi0V1(A)
    A = tau(A)
    return A


def _EXIT_():
    print('?????..')
    exit(0)


def _return_():
    print(
        '"0" : ??????? ??? ??????' + '\n' + '"1" : start' + '\n')
    flag = input()
    if flag == '1':
        _start_()
    elif flag == '0':
        _EXIT_()
    else:
        print('?????? ?????!' + '\n' + '?????????, ??????????:')
        _return_()


def generatorChisla():
    C = 3
    A = 5
    M = 2 ** 256
    t0 = generate(256) % M
    print(t0)
    print(isProstoeNumberV2(t0))
    while ((not isProstoeNumberV2(t0))):
        t0 = (A * t0 + C) % M
        print(t0)
    if (t0 < 2**255) and (t0 > 2**256):
        return generatorChisla()
    return t0


def test(text, K, countRaund=1):
    blocks = getBlocksForText(text)
    map = code(blocks, countRaund, K)
    blocksDecode = decode(map['blocksCode'], countRaund, map['KR'])
    print(blocksDecode)
    print(getBlocksForText(text))
    return blocksDecode == getBlocksForText(text)


def code(blocks, countRaund, K):
    Ke = generationKeV1(K)

    print("ke")
    print(Ke)
    print("bloks")

    print(blocks)
    KR = []

    indexBloc = 1
    blocksCode = []
    for blok in blocks:
        for numRaund in range(countRaund):
            if (indexBloc == 1):
                KR.append(generationKr(numRaund, Ke))
                # KR.append(generationKr(1, Ke))
                print("KR")
                print(KR)
            blok = raund(blok, KR[numRaund], numRaund)
        if ((countRaund - 1) % 2 == 0):
            blok = fe(blok)
        else:
            blok = f0(blok)
        print("blok")
        print(blok)
        blocksCode.append(blok)
        indexBloc += 1
    print(getTextForBlocks(blocksCode))
    return {'blocksCode': blocksCode, 'KR': KR}


def decode(blocksCode, countRaund, KR):
    blocksDecode = []
    for blok in blocksCode:
        if ((countRaund - 1) % 2 == 0):
            blok = fe(blok)
        else:
            blok = f0(blok)
        for numRaund in range(countRaund):
            blok = raundDecode(blok, KR[countRaund - 1 - numRaund], countRaund - 1 - numRaund)
        print("blok decode ")
        print(blok)
        blocksDecode.append(blok)
        # indexBloc += 1
    print(getTextForBlocks(blocksCode))
    print(getTextForBlocks(blocksDecode))
    return blocksDecode


def _start_():
    # text = "mama myla ramy and "
    text = "I, Morin Danila Sergeevich, date of birth 04/03/1998, place of birth Nizhny Novgorod, live at Nizhny Novgorod, Delovaya Street d6"
    # text = "?, ????? ?????? ?????????, ???? ???????? 03.04.1997, ????? ???????? ?. ?????? ????????, ?????? ??, ??????????? ?? ???????: ????? ?????? ????????, ??. ???????, ?. 6. ???? ????? ?? ????????????"
    countRaund = 2
    key = generatorChisla()
    print("key -> " + str(hex(key)))
    b = BitArray(hex(key)).hex
    print(b)
    K = []
    str0 = b
    # print(str0[0:2])
    for i in range(32):
        s = str0[i * 2:i * 2 + 2]
        if (int(s, 16) < 16):
            K.append("0"+BitArray(hex(int(s, 16))).hex)
        else:
            K.append(BitArray(hex(int(s, 16))).hex)
    print("key fun")
    print(K)
    while not test(text, K, countRaund):
        key = generatorChisla()
        # key = getProstoeNumber(256)
        # print("key -> " + str(hex(key)))
        b = BitArray(hex(key)).hex
        # print(b)
        K = []
        str0 = b
        # print(str0[0:2])
        for i in range(32):
            s = str0[i * 2:i * 2 + 2]
            K.append(hex(int(s, 16)))

    print("result k")
    print(K)

    # countRaund = 1
    blocks = getBlocksForText(text)
    # blocksTest = blocks.copy()
    map = code(blocks, countRaund, K)
    blocksDecode = decode(map['blocksCode'], countRaund, map['KR'])
    print(blocksDecode)
    print(getBlocksForText(text))

    # K = ['0x7b', '0x87', '0x54', '0x4e', '0xa2', '0xe8', '0x50', '0xf4', '0xe9', '0x94', '0x14', '0x65', '0x1d', '0xff',
    #      '0x30', '0x3d', '0x83', '0xf0', '0x4', '0x63', '0xd1', '0x17', '0xb4', '0x62', '0xdf', '0x8', '0x85', '0xa',
    #      '0xb8', '0x1', '0x96', '0x2d']

    # text = "lolololololololoLL"
    # print("bloks")
    # blocks = getBlocksForText(text)
    # print(blocks)
    # # blok = [[111, 111, 111, 111],
    # #         [111, 111, 111, 111],
    # #         [111, 111, 111, 111],
    # #         [111, 111, 111, 111]]
    # KR = []
    # # n = generate(36)
    # # isProstoeNumber(n)
    #
    # # key = getProstoeNumber(256 * 8)
    # # key = generate(256)
    # # key = isProstoeNumber(key)
    # key = generatorChisla()
    # print("key -> " + str(hex(key)))
    # b = BitArray(hex(key)).hex
    # print(b)
    # K = []
    # str0 = b
    # # print(str0[0:2])
    # for i in range(32):
    #     s = str0[i * 2:i * 2 + 2]
    #     K.append(hex(int(s, 16)))
    # print("key fun")
    # print(K)
    #
    # # K = ['0x7b', '0x87', '0x54', '0x4e', '0xa2', '0xe8', '0x50', '0xf4', '0xe9', '0x94', '0x14', '0x65', '0x1d', '0xff',
    # #      '0x30', '0x3d', '0x83', '0xf0', '0x4', '0x63', '0xd1', '0x17', '0xb4', '0x62', '0xdf', '0x8', '0x85', '0xa',
    # #      '0xb8', '0x1', '0x96', '0x2d']
    # Ke = generationKeV1(K)
    #
    # print("ke")
    # print(Ke)
    # countRaund = 2
    # indexBloc = 1
    # blocksCode = []
    # blocksDecode = []
    # for blok in blocks:
    #
    #     for numRaund in range(countRaund):
    #         if (indexBloc == 1):
    #             KR.append(generationKr(numRaund, Ke))
    #             # KR.append(generationKr(1, Ke))
    #             print("KR")
    #             print(KR)
    #         blok = raund(blok, KR[numRaund], numRaund)
    #     if ((countRaund - 1) % 2 == 0):
    #         blok = fe(blok)
    #     else:
    #         blok = f0(blok)
    #     print("blok")
    #     print(blok)
    #     blocksCode.append(blok)
    #     indexBloc += 1
    # for blok in blocksCode:
    #     if ((countRaund - 1) % 2 == 0):
    #         blok = fe(blok)
    #     else:
    #         blok = f0(blok)
    #     for numRaund in range(countRaund):
    #         blok = raundDecode(blok, KR[countRaund - 1 - numRaund], countRaund - 1 - numRaund)
    #     print("blok decode ")
    #     print(blok)
    #     blocksDecode.append(blok)
    #     # indexBloc += 1
    # print(getTextForBlocks(blocksCode))
    # print(getTextForBlocks(blocksDecode))

    # print(str(isProstoeNumber(100035251562572620774571597670303635288341430950703705415663222088429988138119)))


if __name__ == "__main__":
    print("------Start-------")
    _return_()

# generateTable()

# mat1 = [[80, 162, 84, 123], [48, 29, 20, 233], [180, 209, 4, 131], [150, 184, 133, 223]]
# mat1 = linePi0V1(mat1)
# print("mat1")
# print(mat1)
#
# mat2 = linePi0V1(mat1)
# print("mat2")
# print(mat2)
