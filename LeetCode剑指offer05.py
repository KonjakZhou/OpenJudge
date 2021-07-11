class Solution:
    def replaceSpace(self, s):
        ans = list()
        for i in s:
            if i==" ":
                ans.append("%")
                ans.append("20")
            else:
                ans.append(i)
        return "".join(ans)