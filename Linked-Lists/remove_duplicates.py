# write code to remove duplicates from an unsorted linked list

from linked_list import LinkedList

ll_instance = LinkedList()

ll_instance.add(1)
ll_instance.add(2)
ll_instance.add(1)
ll_instance.add(3)
ll_instance.add(1)
ll_instance.add(2)
ll_instance.add(3)
ll_instance.add(3)

ll_instance.display()


def remove_duplicates(head: LinkedList):
    hash_map = set()
    prevoius = None
    while head:
        if head.data in hash_map:
            prevoius.next = head.next
        else:
            hash_map.add(head.data)
            prevoius = head
        head = head.next


remove_duplicates(ll_instance.head)
print("After removing duplicates")

ll_instance.display()


ll_instance2 = LinkedList()

ll_instance2.add(1)
ll_instance2.add(2)
ll_instance2.add(1)
ll_instance2.add(3)
ll_instance2.add(1)
ll_instance2.add(2)
ll_instance2.add(3)
ll_instance2.add(3)

ll_instance2.display()

def remove_duplicates_no_buffer_allowed(head: LinkedList):
    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
remove_duplicates_no_buffer_allowed(ll_instance2.head)
print("After removing duplicates")

ll_instance2.display()

