# coding=utf-8
# Author: KonjakZhou
# Created At: 周四 04 八月 2022 00:09:54 CST
# MagIc C0de: a0fb5282c4a1

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])