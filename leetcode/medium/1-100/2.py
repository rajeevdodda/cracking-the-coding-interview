# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp = 0

        list_a = l1
        list_b = l2
        head = None
        tail = None
        while list_a and list_b:
            temp = temp + list_a.val + list_b.val
            node = ListNode(temp % 10)
            temp = temp // 10
            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
            list_a = list_a.next
            list_b = list_b.next

        while list_a:
            temp = temp + list_a.val
            node = ListNode(temp % 10)
            temp = temp // 10
            tail.next = node
            tail = node
            list_a = list_a.next
        while list_b:
            temp = temp + list_b.val
            node = ListNode(temp % 10)
            temp = temp // 10
            tail.next = node
            tail = node
            list_b = list_b.next
        if temp:
            tail.next = ListNode(temp)

        return head
