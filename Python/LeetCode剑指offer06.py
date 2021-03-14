# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head):
        if head == None:
            return []
        if head.next == None:
            return [head.val]
        
        p = None
        q = head
        while q!=None:
            r = q.next
            
            q.next = p
            
            p = q
            q = r
            
        ans = list()
        while p!=None:
            ans.append(p.val)
            p = p.next
        return ans

if __name__ == "__main__":
    node_list = [1,3,2]
    virtualHead = ListNode(0)
    q = virtualHead
    for i in node_list:
        p = ListNode(i)
        q.next = p
        q = p
    head = virtualHead.next

    solution = Solution()
    print(solution.reversePrint(head))
    