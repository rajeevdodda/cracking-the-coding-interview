# Implement an algorithm to delete a node in the middle (i.e./ any node but the
# first and last node, not necessarily the exact middle node) of a sinly linked 
# list, given only access to that code

from linked_list import LinkedList

ll_instance = LinkedList()

for i in range(1, 10):
    ll_instance.add(i)


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


ll_instance.display()

node = ll_instance.head.next.next

print("after deleteing")

delete_middle_node(node)

ll_instance.display()