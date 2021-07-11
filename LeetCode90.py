class Solution:
    def subsetsWithDup(self, nums):
        def dfs(k):
            if k==maxLen :
                result.append(ans[:])
                return 
            
            for _ in range(num_dict[keys[k]]):
                ans.append(keys[k])
                dfs(k+1)
            for _ in range(num_dict[keys[k]]):
                ans.pop()
            dfs(k+1)
            return 
                

        if len(nums)==0:
            return [[]]
        
        num_dict = {}
        for number in nums:
            if number not in num_dict:
                num_dict[number] = 1
            else:
                num_dict[number] += 1
        
        keys = list(num_dict.keys())
        maxLen = len(keys)
        ans = list()
        result = list()

        dfs(0)
        return result