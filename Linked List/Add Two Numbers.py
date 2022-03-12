# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        r = 0 
        while(l1 or l2) : 
            if l1 : 
                r+=l1.val
                l1=l1.next
            if l2 : 
                r+=l2.val 
                l2=l2.next
            a.append(r%10)
            r/=10 
        if(int(r)>0) : 
            a.append(r)
        
        head = ListNode(int(a[0]))
        if len(a)>1 :
            new = ListNode (int(a[1]))
            head.next = new

            for i in range (2,len(a)) :
                temp = ListNode(int(a[i]))
                new.next = temp
                new = temp
        return head
