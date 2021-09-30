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

    while head:
        if head.data not in hash_map:
            hash_map.add(head.data)
            head = head.next
        else:
            if head.next:
                head.data = head.next.data
                head.next = head.next.next
            else:
                break
remove_duplicates(ll_instance.head)
print('After removing duplicates')

ll_instance.display()
