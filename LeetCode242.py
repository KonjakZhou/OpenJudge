class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = dict()
        for c in s:
            try:
                check[c] += 1
            except KeyError:
                check[c] = 1

        for c in t:
            try:
                check[c] -= 1
            except KeyError:
                check[c] = -1

        for f in check.values():
            if f!=0:
                return False
        return True

if __name__=="__main__":
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))
