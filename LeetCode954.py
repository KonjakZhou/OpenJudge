import random

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """ 
        if (len(arr)==0):
            return True
        ans = arr[:]
        ans.sort(key=lambda x: abs(x))
        
        flag_neg = [0 for _ in range(int(2e5+1))]
        flag_pos = [0 for _ in range(int(2e5+1))]

        for i in arr:
            if i < 0:
                flag_neg[-i] += 1
            else:
                flag_pos[i] += 1
        
        for i in range(len(ans)):
            if ans[i] < 0:
                if flag_neg[-ans[i]] == 0:
                    continue
                if flag_neg[-ans[i]*2] < flag_neg[-ans[i]]:
                    return False
                flag_neg[-ans[i]*2] -= flag_neg[-ans[i]]
                flag_neg[-ans[i]] = 0 
            else:
                if flag_pos[ans[i]] == 0:
                    continue
                if flag_pos[ans[i]*2] < flag_pos[ans[i]]:
                    return False
                flag_pos[ans[i]*2] -= flag_pos[ans[i]]
                flag_pos[ans[i]] = 0 

        return True

