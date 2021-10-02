# Implement a function to check if a linked list is palindrome

from os import PRIO_PGRP
from linked_list import LinkedList, Node


ll = LinkedList()

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)


def is_palindrome_using_stack(head: LinkedList) -> bool:
    stack = []

    node = head

    while node:
        stack.append(node.data)
        node = node.next

    node = head
    while node:
        if stack.pop() != node.data:
            return False
        node = node.next
    return True


print("Using Stack")
print(is_palindrome_using_stack(ll.head))


def is_palindrome_using_reversed_list(head: LinkedList):
    new_list_head = None
    old_node = head
    while old_node:
        node = Node(old_node.data)
        node.next = new_list_head
        new_list_head = node
        old_node = old_node.next
    while new_list_head and head:
        if new_list_head.data != head.data:
            return False
        new_list_head = new_list_head.next
        head = head.next
    return True


print("Using reversed linked list")
print(is_palindrome_using_reversed_list(head=ll.head))


def is_palindrome_using_stack_two_pointer(head: LinkedList) -> bool:
    slow_pointer = head
    fast_pointer = head

    stack = []

    while fast_pointer and fast_pointer.next:
        stack.append(slow_pointer.data)
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    if fast_pointer:
        slow_pointer = slow_pointer.next

    while slow_pointer:
        if slow_pointer.data != stack.pop():
            return False
        slow_pointer = slow_pointer.next

    return True


print("Using Stack with 2 pointers")
print(is_palindrome_using_stack_two_pointer(head=ll.head))



def is_palindrome_using_recursive(head: LinkedList):
    pass


