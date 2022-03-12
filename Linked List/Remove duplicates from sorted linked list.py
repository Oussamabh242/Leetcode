# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None : 
            return head
        v = []
        occ = []
        temp = head 
        while temp : 
            v.append(temp.val)
            temp = temp.next
        for i in v :
            if(v.count(i))==1 :
                occ.append(i)
        if len(occ)==len(v):
            return head
        if len(occ) == 0 :
            tmp = ListNode
            tmp =None
            return temp
        temp = head
        for i in range(len(occ)-1) :
            temp.val =occ[i]
            temp=temp.next
        temp.next = None
        temp.val=occ[len(occ)-1]
        return head
        
        
