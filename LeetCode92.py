# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if head==None or head.next==None:
            return head 
        if left == right:
            return head
        
        virtualNode = ListNode(0)
        virtualNode.next = head
        p = virtualNode
        t = head
        cur_head = p
        cnt = 0
        while t!=None:
            cnt += 1
            if cnt == left:
                cur_head = p
            if left <= cnt <= right:    
                q = t
                t = t.next
                q.next = p
                p = q
            else:
                p = t
                t = t.next
            if cnt == right:
                cur_head.next.next = t
                cur_head.next = p
        return virtualNode.next

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    left = 2
    right = 4
    vh = ListNode(0)
    p = vh
    for i in nums:
        tmp = ListNode(i)
        p.next = tmp
        p = tmp
    head = vh.next

    solution = Solution()
    ans_head = solution.reverseBetween(head, left, right)
    p = ans_head
    ans = []
    while p!=None:
        ans.append(p.val)
        p = p.next
    print(ans)