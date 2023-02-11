# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        acc = 0
        aux = head
        while aux != None:
            acc += 1
            aux = aux.next
        acc2 = 0
        aux2 = head
        while aux2 != None:
            acc2 += 1
            if acc2 == acc//2 + 1:
                return aux2
            aux2 = aux2.next
        
