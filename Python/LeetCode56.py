import random

class Solution:
    def merge(self, intervals):

        if len(intervals)==0: 
            return []
        
        self.quickSort(intervals, 0, len(intervals) - 1)

        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            next = intervals[i]
            last = stack.pop()
            if last[-1]>=next[0]:
                stack.append([last[0], max(last[-1], next[-1])])
            else:
                stack.append(last)
                stack.append(next)
        return stack

    @staticmethod
    def quickSort(arr, l, r):
        def comp(s,t):
            if s[0] < t[0]:
                return -1
            if s[0] == t[0] and s[1] < t[1]:
                return -1
            if s[0] == t[0] and s[1] == t[1]:
                return 0
            return 1
        
        def swap(arr, i, j):
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

        index = random.randint(l,r)
        swap(arr, index, l)

        j = l 
        for i in range(l+1,r+1):
            if comp(arr[i], arr[l]) < 0:
                j += 1
                swap(arr, i, j)
        swap(arr, l, j)

        if r - j > 1:
            Solution.quickSort(arr, j+1, r)
        if j - l > 1:
            Solution.quickSort(arr, l, j-1)
        return

if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    Solution.quickSort(intervals, 0, len(intervals)-1)
    print(intervals)