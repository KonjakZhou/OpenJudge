class Solution:
    def minArray(self, numbers):
        n = len(numbers)
        if n == 1:
            return numbers[0]

        l = 0
        r = len(numbers) - 1
        while (l<r):
            mid = (l+r) >> 1
            if numbers[mid] > numbers[r]:
                l = mid + 1
                continue
            if numbers[mid] < numbers[r]:
                r = mid
                continue
            if numbers[mid] == numbers[r]:
                r -= 1
                continue
        return numbers[l]
