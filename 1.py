#!/usr/bin/env python
# coding: utf-8
def judge_list_baohan(a,b):
    # a = [1, 2, 3, 4, 5]
    # b = [3, 4, 5]
    d = [False for c in b if c not in a]
    if d:
      print("a不包含b的所有元素")
    else:
      print("a包含b的所有元素")

