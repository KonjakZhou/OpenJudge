# coding=utf-8
# Author: KonjakZhou
# Created At: 周三 03 八月 2022 22:17:15 CST
# MagIc C0de: 956ee4e22609

class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]

        ans = list()
        if_left = False
        if_recored = False
        ans_left = newInterval[0]
        ans_right = newInterval[1]
        for interval in intervals:
            if if_recored:
                ans.append(interval)
                continue

            if not if_left:
                if newInterval[0] < interval[0]:
                    ans_left = newInterval[0]
                    if_left = True
                elif newInterval[0] <= interval[1]:
                    ans_left = interval[0]
                    if_left = True
                else:
                    ans.append(interval)
                    continue
            
            if newInterval[1] < interval[0]:
                ans_right = newInterval[1]
                ans.append([ans_left, ans_right])
                if_recored = True
                ans.append(interval)
            elif newInterval[1] <= interval[1]:
                ans_right = interval[1]
                ans.append([ans_left, ans_right])
                if_recored = True
        
        if not if_recored:
            ans.append([ans_left, ans_right])

        return ans