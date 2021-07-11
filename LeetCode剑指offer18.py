# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head, val):
        virtualHead = ListNode(0)
        virtualHead.next = head
        p = virtualHead
        while p != None:
            t = p.next
            if t == None:
                return virtualHead.next
            if t.val == val:
                p.next = t.next
                return virtualHead.next
            p = p.next