class Solution:
    def decode(self, encoded, first: int):
        ans = [first]
        for num in encoded:
            ans.append(ans[-1] ^ num)
        return ans