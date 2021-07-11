class Solution:
    def findMin(self, nums):
        def bisearch(l,r):
            if l==r:
                return nums[l]
            mid = (l+r)>>1
            if nums[mid]>nums[r]:
                return bisearch(mid+1, r)
            return min(bisearch(l, mid), bisearch(mid+1, r))
        
        return bisearch(0, len(nums)-1)