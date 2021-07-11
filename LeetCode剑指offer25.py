# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        p1 = l1
        p2 = l2
        
        virtualHead = ListNode(0)
        t = virtualHead
        
        while t!=None:
            if p2==None or (p1!=None and p1.val<=p2.val):
                t.next = p1
                p1 = p1.next
            else:
                t.next = p2
                p2 = p2.next
        return virtualHead.next