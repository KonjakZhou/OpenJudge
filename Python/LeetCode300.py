class Solution:
    def lengthOfLIS(self, nums):
        def biSearch(arr, l, r, target):
            if l == r:
                if arr[l] < target:
                    return l+1
                return l

            mid = (l+r) >> 1
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                return biSearch(arr, l, mid, target)
            if arr[mid] < target:
                return biSearch(arr, mid+1, r, target)

        n = len(nums)
        if n <= 1:
            return n
        stack = [nums[0]]
        for i in range(1, n):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                index = biSearch(stack, 0, len(stack)-1, nums[i])
                stack[index] = nums[i]
        return len(stack)

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    solution = Solution()
    print(solution.lengthOfLIS(nums))