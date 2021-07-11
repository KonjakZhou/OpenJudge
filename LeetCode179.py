import functools

class Solution:
    def largestNumber(self, nums):
        def cmp(str1, str2):
            a = str1 + str2
            b = str2 + str1
            if a<b:
                return -1
            if a>b:
                return 1
            return 0
            
        strs = [str(num) for num in nums]
        maxlen = 0
        for string in strs:
            if maxlen<len(string):
                maxlen = len(string)

        strs.sort(key=functools.cmp_to_key(cmp), reverse=True)
        ans = "".join(strs)
        cnt = 0
        while cnt<len(ans)-1 and ans[cnt]=='0':
            cnt+=1
        return ans[cnt:] 