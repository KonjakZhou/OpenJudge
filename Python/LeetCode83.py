# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head 
        while p is not None and p.next is not None:
            if p.next.val == p.val:
                p.next = p.next.next
            p = p.next
        return head