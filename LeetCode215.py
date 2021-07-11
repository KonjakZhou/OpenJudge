import random
class Solution:
    def findKthLargest(self, nums, k):
        def quick_sort(nums, k, l, r):
            index = random.randint(l,r)

            t = nums[index]
            nums[index] = nums[l]
            nums[l] = t

            j = l 
            for i in range(l+1, r+1):
                if nums[i]>nums[l]:
                    j += 1
                    t = nums[i]
                    nums[i] = nums[j]
                    nums[j] = t
            
            t = nums[j]
            nums[j] = nums[l]
            nums[l] = t
            if j == k-1 :
                return nums[j]
            if j > k-1 :
                return quick_sort(nums, k, l, j-1)
            if j < k-1 :
                return quick_sort(nums, k, j+1, r)
        
        return quick_sort(nums, k, 0, len(nums)-1)
