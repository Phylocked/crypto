# coding=utf-8
'''
Created on 2017年5月24日
@author: xxx
'''
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


def bin2hex(string_num):
    return dec2hex(bin2dec(string_num)).zfill(16)


def dec2bin(num):
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


def bin2dec(string_num):
    return int(string_num, 2)


def hex2bin(string_num):
    a = []
    for i in range(int(len(string_num) / 16)):
        a.append(dec2bin(hex2dec(string_num[16 * i:16 * (i + 1) - 1].upper())).zfill(64))
    #    return dec2bin(hex2dec(string_num.upper())).zfill(64)
    return a


def str2asc_bin(string):
    a, c = [], ''
    for i in string:
        a.append(ord(i))
    for i in a:
        c += str(dec2bin(i).zfill(8))
    return c


def asc_bin2str(string):
    a = ''
    for i in range(len(string) / 8):
        a += str(chr(bin2dec(string[8 * i:8 * i + 8])))
    return a