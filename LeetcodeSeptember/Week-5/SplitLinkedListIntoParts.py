# https://leetcode.com/problems/split-linked-list-in-parts/
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        self.l = []

        while head:
            self.l.append(head.val)
            head = head.next

        len_l = len(self.l)   
        
        if len_l == 0:
            return [ None for i in range(0,k)]
                
                
        
        
        
        res = []
        
        if len_l % k == 0:
            for i in range(0,len_l,len_l//k):
                res.append(self.l[i:i+ (len_l//k)])
        else:
            if len_l // k == 0:
                for i in range(0,len_l):
                    res.append(self.l[i:i+1])
                for i in range(k-len_l):
                    res.append([])
            else:
                m = len_l%k
                n = len_l//k
                i = 0 
                while i < len_l:
                    if m > 0:
                        res.append(self.l[i:i+n+1])
                        m-=1
                        i+= n+1
                    else:
                        res.append(self.l[i:i+n])
                        i+= n
                    
                
                
                
               
        res1 = []
        for i in range(len(res)):
            m = n =  ListNode(0)
            for j in res[i]:
                n.next = ListNode(j)
                n  = n.next
            res1.append(m.next)
        return res1
            
                