class Solution:
    def xorQueries(self, arr, queries):
        n = len(arr)
        prefix = [0 for _ in range(n+1)]
        
        for i in range(n):
            prefix[i+1] = prefix[i] ^ arr[i]
        
        ans = list()
        for l, r in queries:
            ans.append(prefix[l] ^ prefix[r+1])
        return ans 