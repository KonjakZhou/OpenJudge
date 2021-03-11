class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = list()        
        n = len(nums)

        heap_big = [-2147483648 for _ in range(k+1)]
        numIndexInHeap = [0 for _ in range(n)]
        for i in range(k):
            heap_big[i+1] = i
            tmp = i+1
            numIndexInHeap[i] = tmp
            while tmp > 1 and nums[heap_big[tmp]] > nums[heap_big[tmp >> 1]]:
                numIndexInHeap[heap_big[tmp>>1]] = tmp
                numIndexInHeap[heap_big[tmp]] = tmp >> 1
                t = heap_big[tmp]     
                heap_big[tmp] = heap_big[tmp >> 1]
                heap_big[tmp >> 1] = t
                tmp = tmp >> 1
        
        for i in range(k, n):
            ans.append(nums[heap_big[1]])
            tmp = numIndexInHeap[i-k]
            heap_big[tmp] = i
            numIndexInHeap[i] = tmp

            while tmp > 1 and nums[heap_big[tmp]] > nums[heap_big[tmp >> 1]]: # upper update
                numIndexInHeap[heap_big[tmp>>1]] = tmp
                numIndexInHeap[heap_big[tmp]] = tmp >> 1
                t = heap_big[tmp]     
                heap_big[tmp] = heap_big[tmp >> 1]
                heap_big[tmp >> 1] = t
                tmp = tmp >> 1
            
            while (((tmp << 1) + 1) < k+1 and nums[heap_big[(tmp<<1)+1]] > nums[heap_big[tmp]]) \
                or ((tmp << 1) < k+1 and nums[heap_big[tmp<<1]] > nums[heap_big[tmp]]):
                swap = tmp
                max = nums[heap_big[tmp]]
                if ((tmp << 1) + 1) < k+1 and nums[heap_big[(tmp<<1)+1]] > max:
                    swap = (tmp<<1) + 1
                    max = nums[heap_big[(tmp<<1)+1]]
                if (tmp << 1) < k+1 and nums[heap_big[tmp<<1]] > max:
                    swap = (tmp<<1) 
                    max = nums[heap_big[tmp<<1]]
                
                numIndexInHeap[heap_big[tmp]] = swap
                numIndexInHeap[heap_big[swap]] = tmp
                t = heap_big[tmp]
                heap_big[tmp] = heap_big[swap]
                heap_big[swap] = t
                tmp = swap
            
        ans.append(nums[heap_big[1]])
        return ans 

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    nums = [1]
    k = 1
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))