# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        c = d
        res = []
        a1=[]
        a2=[]
        while l1 :
            a1.append(l1.val)
            l1 = l1.next if l1 else None
        while l2 :
            a2.append(l2.val)
            l2 = l2.next if l2 else None

        s1 = len(a1)
        s2 = len(a2)
        ext_sum = 0

        # determine size for longest arrray
        # run in cicle for range in length array
        for inx in range (max(s1,s2)):
            app_val = ext_sum;
            if s1 >inx :
                app_val = app_val + a1[inx]
            if s2 > inx :
                app_val = app_val + a2[inx]
            ext_sum = app_val//10
            app_val = app_val%10
            c.next =  ListNode(app_val)
            c=c.next
            #res.append( app_val )

        if ext_sum > 0: 
            c.next =  ListNode(ext_sum) #res.append( ext_sum )
            c=c.next


        return(d.next)