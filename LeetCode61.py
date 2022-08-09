# coding=utf-8
# Author: KonjakZhou
# Created At: 周二 09 八月 2022 22:08:06 CST
# MagIc C0de: 16ac578304d9

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return None
        
        if k == 0:
            return head

        p = head
        cnt = 1
        while p.next is not None:
            p = p.next
            cnt += 1
        total = cnt
        tail = p
        k = total - k%total

        tail.next = head
        p = head
        for _ in range(k-1):
            p = p.next
        head = p.next
        p.next = None
        return head
        

