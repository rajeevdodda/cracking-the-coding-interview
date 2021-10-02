# Given two singly linked list, determine if the two lists intersect.
# Return the intersecting Node. Note that the intersection is based on the
# reference, not the value. That is, if the kth node of the first linked is the
#  exact same node by (reference) as the jth node of the second linked list,
# then they are intersecting.


from linked_list import LinkedList, Node

ll_1 = LinkedList()
ll_2 = LinkedList()

for i in range(5):
    ll_2.add(i)


for i in range(3,5):
    ll_1.add(i)
intersection_node = Node(5)

ll_2.tail.next = intersection_node
ll_2.tail = intersection_node

ll_1.tail.next = intersection_node
ll_1.tail = intersection_node


print(ll_2.tail == ll_1.tail)


for i in range(6,10):
    ll_1.add(i)

ll_1.display()
ll_2.display()




def intersection_node(first_ll, second_ll):
    first_length = first_ll.length()
    second_length = second_ll.length()

    first_node = first_ll.head
    second_node = second_ll.head

    diff = first_length - second_length

    if diff > 0:
        while diff > 0:
            first_node = first_node.next
            diff -= 1
    else:
        diff = second_length - first_length
        while diff > 0:
            second_node  = second_node.next
            diff -= 1

    while first_node and second_node:
        if first_node == second_node:
            return first_node.data
        first_node = first_node.next
        second_node = second_node.next
    
    return None


print(intersection_node(ll_1, ll_2))

ll_3 = LinkedList()
ll_3.add(10)


print(intersection_node(ll_1, ll_3))

