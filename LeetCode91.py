class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        nums = [ord(ch) - 48 for ch in s]
        if n == 0:
            return 0
        
        if nums[0] == 0:
            return 0
        
        if n == 1:
            return 1

        f_2 = 1
        f_1 = 1
        for i in range(1, n):
            if nums[i]!=0:
                if ( nums[i-1] != 0 ) and (nums[i-1]*10 + nums[i] <= 26):
                    f_2, f_1 = f_1, f_2+f_1
                else:
                    f_2 = f_1
            else:
                if 0< nums[i-1] <3:
                    f_2, f_1 = f_1, f_2
                else:
                    return 0
        return f_1

if __name__ == "__main__":
    str = "12"
    solution = Solution()
    print(solution.numDecodings(str))