# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return None 
        virtualHead = ListNode(0)
        virtualHead.next = head
        
        p = virtualHead
        t = head
        
        while t!=None:
            q = t
            t = t.next
            q.next = p
            p = q 
        virtualHead.next.next = None
        return p