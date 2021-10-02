# Given a linked list, implement  an algorithm that returns the node at the
# begining of the loop

from linked_list import LinkedList

ll = LinkedList()

for i in range(1, 10):
    ll.add(i)

ll.tail.next = ll.head.next.next.next


def detect_loop(head: LinkedList):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if fast is None or fast.next is None:
        return None
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.data
    


print(detect_loop(ll.head))