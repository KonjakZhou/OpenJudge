class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = [0 for _ in range(m+n)]
        t = 0
        l = 0
        r = 0
        while t<(m+n):
            if(l<m) and ((r>=n) or nums1[l]<nums2[r]):
                tmp[t] = nums1[l]
                l += 1
            else:
                tmp[t] = nums2[r]
                r += 1
            t += 1
        for t in range(m+n):
            nums1[t] = tmp[t]
        return
            