class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 基于快排
        def quick(begin, end):
            if begin > end:
                return
            s, e = begin, end
            while begin <end:
                pivot = nums[begin]
                while begin < end and nums[end] > pivot:
                    end -= 1
                nums[begin], nums[end] = nums[end], nums[begin]
                while begin < end and nums[begin] <= pivot:
                    begin += 1
                nums[begin], nums[end] = nums[end], nums[begin]

            if begin<e:
                quick()
            elif begin > len(nums) // 2:
                return quick(s, begin-1)
            elif begin < len(nums) // 2:
                return quick(begin+1, e)
        
        if not nums: return
        if len(nums)==1:
            return nums[0]
        return quick(0, len(nums)-1)