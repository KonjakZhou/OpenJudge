
def update_up(heap_big, tmp, nums_index_in_heap):
    while tmp > 1 and ((heap_big[tmp][0] > heap_big[tmp >> 1][0]) or  ((heap_big[tmp][0] == heap_big[tmp >> 1][0]) and (heap_big[tmp][1] < heap_big[tmp >> 1][1]))):
        nums_index_in_heap[tmp >> 1] = tmp
        nums_index_in_heap[tmp] = tmp >> 1

        t = heap_big[tmp]     
        heap_big[tmp] = heap_big[tmp >> 1]
        heap_big[tmp >> 1] = t
        tmp = tmp >> 1
    return 

def update_down(heap_big, tmp, nums_index_in_heap, k):
    while (   ((tmp << 1) + 1) < k+1 and ((heap_big[(tmp<<1)+1][0] > heap_big[tmp][0]) or ((heap_big[(tmp<<1)+1][0] == heap_big[tmp][0]) and  (heap_big[(tmp<<1)+1][1] < heap_big[tmp][1]) ))) \
        or ((tmp << 1) < k+1 and ((heap_big[tmp<<1][0] > heap_big[tmp][0]) or ( (heap_big[tmp<<1][0] == heap_big[tmp][0]) and (heap_big[tmp<<1][1] < heap_big[tmp][1])   ))):
        swap = tmp
        max = heap_big[tmp]
        if ((tmp << 1) + 1) < k+1 and ((heap_big[(tmp<<1)+1][0] > max[0]) or ((heap_big[(tmp<<1)+1][0] == max[0]) and  (heap_big[(tmp<<1)+1][1] < max[1]) )):
            swap = (tmp<<1) + 1
            max = heap_big[(tmp<<1)+1]
        if ((tmp << 1) < k+1) and ((heap_big[tmp<<1][0] > max[0]) or ( (heap_big[tmp<<1][0] == max[0]) and (heap_big[tmp<<1][1] < max[1])  )):
            swap = (tmp<<1) 
            max = heap_big[tmp<<1]

        nums_index_in_heap[tmp] = swap
        nums_index_in_heap[swap] = tmp

        t = heap_big[tmp]
        heap_big[tmp] = heap_big[swap]
        heap_big[swap] = t
        tmp = swap

def max_sliding_window(nums, n, k):
    ans = list()        
    nums_frequency = dict()
    nums_index_in_heap = dict()
    total = 0
    # 前 k 个数字的众数统计
    for i in range(k):
        if nums[i] not in nums_frequency:
            nums_frequency[nums[i]] = 1
        else:
            nums_frequency[nums[i]] += 1
        
    # 建立大根堆 (频数，数字)
    # 堆中最多有k个数字， 下标从1到k
    heap_big = [(-2147483648, -2147483648) for _ in range(k+1)]
    
    for i in range(k):
        if nums[i] not in nums_index_in_heap:
            total += 1
            nums_index_in_heap[nums[i]] = total
            heap_big[total] = (nums_frequency[nums[i]], nums[i])
            tmp = total
            nums_index_in_heap[nums[i]] = tmp

            # 向上更新
            update_up(heap_big, tmp, nums_index_in_heap)
    
    for i in range(k, n):
        ans.append(heap_big[1][0])  # 添加答案

        # 去除窗口外的（第 i-k 个数字）
        nums_frequency[nums[i-k]] -= 1
        heap_big[nums_index_in_heap[nums[i-k]]] = (nums_frequency[nums[i-k]], nums[i-k])
        # 向下更新
        update_down(heap_big, tmp, nums_index_in_heap, total)
        if nums_frequency[nums[i-k]] == 0:
            total -= 1

        # 添加当前的 （第 i 个数字）
        if nums[i] not in nums_frequency:
            nums_frequency[nums[i]] = 1
            total += 1

            heap_big[total] = (nums_frequency[nums[i]], nums[i])
            tmp = total
            nums_index_in_heap[nums[i]] = tmp

            # 向上更新
            update_up(heap_big, tmp, nums_index_in_heap)
        else:
            nums_frequency[nums[i]] += 1
            tmp = nums_index_in_heap[nums[i]]

            heap_big[tmp] = (nums_frequency[nums[i]], nums[i])
            # 向上更新
            update_up(heap_big, tmp, nums_index_in_heap)
            

    ans.append(heap_big[1][0])
    return ans

if __name__ == "__main__":
    n = 3
    k = 2
    nums = [2,1,1]
    print(max_sliding_window(nums, n, k ))