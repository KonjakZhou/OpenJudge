class Solution:
    def smallestK(self, arr, k):
        def quick(arr, l, r, k):
            j = l
            for i in range(l+1, r):
                if arr[i] < arr[l]:
                    j += 1
                    t = arr[i]
                    arr[i] = arr[j]
                    arr[j] = t
            
            t = arr[j]
            arr[j] = arr[l]
            arr[l] = t

            if j == k-1 :
                return arr[:k]
            if j > k-1 :
                return quick(arr, l, j, k)
            if j < k-1 :
                return quick(arr, j+1, r, k)
            
        if k == 0:
            return []
        return quick(arr, 0, len(arr), k)


if __name__ == "__main__":
    arr = [1,3,5,7,2,4,6,8]
    k = 0
    solution = Solution()
    print(solution.smallestK(arr, k ))