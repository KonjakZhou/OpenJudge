class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for _ in range(num+1)]
        if num>=1:
            result[1] = 1

        max = 1
        for i in range(2, num+1):
            res = i - max
            if res < max:
                result[i] = result[res] + 1
            else:
                max = i
                result[i] = 1
        return result
