# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head, k):
        virtualHead = ListNode(0)
        virtualHead.next = head
        p = virtualHead

        ans = list()
        while p.next!=None:
            p = p.next
            ans.append(p)
        return ans[-k]
