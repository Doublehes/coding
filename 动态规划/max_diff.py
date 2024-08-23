#!/usr/bin/env python3
# -*-coding:utf-8-*-
'''
@File    :   max_diff.py
@Time    :   2024/08/22 19:37:47
@Author  :   shuang.he 
@Version :   1.0
@Contact :   shuang.he@momenta.ai
@License :   (C)Copyright 2022-2023, Momenta/shuang.he
@Desc    :   在一个乱序数组中，找出前面的数相比于他后面的所有数的差的最大值。
'''


import random



def get_diff(arr):
    max_diff = -1e5
    calc_count = 0
    last_min = 1e5
    for j in range(len(arr)-1, 0, -1):
        last_min = min(arr[j], last_min)
        max_diff = max(max_diff, arr[j-1]-last_min)
        calc_count += 1
    
    return max_diff,calc_count


def get_diff_force(arr):
    max_diff = -1e5
    calc_count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            calc_count += 1
            max_diff = max(arr[i] - arr[j], max_diff)
    return max_diff, calc_count


if __name__ == "__main__":
    arr = list(range(50))
    random.shuffle(arr)
    print(arr)
    m_diff, c_count = get_diff_force(arr)
    print(m_diff, c_count)

    m_diff, c_count = get_diff(arr)
    print(m_diff, c_count)
