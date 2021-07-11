# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        virtualHead = ListNode()
        virtualHead.next = head
        last = virtualHead
        start = head
        p = start
        cnt = 0
        while p != None:
            p = p.next
            cnt += 1
            if cnt == k:
                end = p 

                t = start.next
                l = start
                start.next = end

                while (t!=end):
                    t_next = t.next
                    t.next = l
                    l = t
                    t = t_next
                
                last.next = l
                last = start
                start = end 

                cnt = 0 
                    

        return virtualHead.next

def printList(head):
    p = head
    while (p!=None):
        print(p.val)
        p = p.next

def buildList(List):
    last = ListNode
    q = last
    for i in List:
        p = ListNode(i)
        q.next = p 
        q = p
    return last.next 


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 6
    head = buildList(arr)

    solution = Solution()
    ansHead = solution.reverseKGroup(head, k)
    printList(ansHead)
