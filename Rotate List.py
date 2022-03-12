# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None : 
            return head
        last = head 
        n = 1
        while last.next :
            n+=1
            last=last.next
        k%=n
        if k == 0 : 
            return head
        kth = head
        for i in range(n-k) :
            kth = kth.next
        before = head 
        for i in range(n-k-1) :
            before = before.next
        before.next = None
        last.next = head
        head = kth
        return head
        
            
        
