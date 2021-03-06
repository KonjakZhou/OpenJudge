class Solution:
    def lengthOfLongestSubstring(self, s):
        
        last = [-2 for _ in range(256)]
        maxLength  = 0
        n = len(s)

        lastIndex = -1
        for i in range(n):
            if last[ord(s[i])] < lastIndex:
                length = i - lastIndex
                if maxLength < length:
                    maxLength = length
            else:
                lastIndex = last[ord(s[i])]
            last[ord(s[i])] = i
        
        return maxLength


if __name__ == "__main__":
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))