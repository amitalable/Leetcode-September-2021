# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.prev = None
        while head:
            temp = head
            head = head.next
            temp.next = self.prev
            self.prev = temp
        return self.prev
