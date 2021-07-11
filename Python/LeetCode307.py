from math import ceil, log

class Node(object):
    def __init__(self,l,r):
        self.l = l
        self.r = r
        self.val = 0

class NumArray:

    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.tree = [None for _ in range(2**(ceil(log(n)/log(2))+1))]
        self.build(1, 0, n-1)

    def build(self, x, l, r):
        self.tree[x] = Node(l,r)

        if l != r:
            mid = (l+r)>>1
            self.build(x*2, l, mid)
            self.build(x*2+1, mid+1, r)
            self.tree[x].val = self.tree[x*2].val + self.tree[x*2+1].val
        else:
            self.tree[x].val = self.nums[l]
        return

    def modify(self, x, index, val):
        if self.tree[x].l==self.tree[x].r:
            self.tree[x].val = val
            return 

        mid = (self.tree[x].l + self.tree[x].r) >> 1
        if index <= mid:
            self.modify(x*2, index, val)
            self.tree[x].val = self.tree[x*2].val + self.tree[x*2+1].val
        else:
            self.modify(x*2+1, index, val)
            self.tree[x].val = self.tree[x*2].val + self.tree[x*2+1].val
        return 
        
    def update(self, index: int, val: int) -> None:
        self.modify(1, index, val)
        return 

    def query(self, x, left, right):
        if self.tree[x].l == left and self.tree[x].r == right:
            return self.tree[x].val
        
        mid = (self.tree[x].l + self.tree[x].r) >> 1
        if left>mid:
            return self.query(x*2 + 1, left, right)
        if right<=mid:
            return self.query(x*2, left, right)
        
        return self.query(x*2, left, mid) + self.query(x*2+1, mid+1, right)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, left, right)


# Your NumArray object will be instantiated and called as such:
if __name__ == "__main__":
    nums = [1,3,5]    
    numArray = NumArray(nums)
    print(numArray.sumRange(0, 2)) # 返回 9 ，sum([1,3,5]) = 9
    numArray.update(1, 2)  # nums = [1,2,5]
    print(numArray.sumRange(0, 2)) # 返回 8 ，sum([1,2,5]) = 8


