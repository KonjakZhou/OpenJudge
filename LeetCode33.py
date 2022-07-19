class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1 
        while l < r :
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[l]:
                if nums[l] <= target <= nums[mid-1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid+1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1