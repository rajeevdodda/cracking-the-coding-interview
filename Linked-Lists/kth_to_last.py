# Implement an algorithm to find the kth to last element of a singly linked list

from linked_list import LinkedList

ll_instance = LinkedList()

for i in range(1, 10):
    ll_instance.add(i)



def kth_to_last_element(l_list: LinkedList, k: int):
    
    k_from_front = l_list.length() - k 
    node = l_list.head

    while k_from_front > 0:
        node = node.next
        k_from_front -= 1
    return node.data

print("Using linear")
print(kth_to_last_element(ll_instance, 6))
print(kth_to_last_element(ll_instance, 1))
print(kth_to_last_element(ll_instance, 9))



def kth_to_last_element_using_recursion(node, k):
    if node is None:
        return 0
    count = kth_to_last_element_using_recursion(node.next, k) + 1
    if count == k:
        print(node.data)
    return count
            
print("Using recursion")
kth_to_last_element_using_recursion(ll_instance.head, 6)
kth_to_last_element_using_recursion(ll_instance.head, 1)
kth_to_last_element_using_recursion(ll_instance.head, 9)



def kth_to_last_element_using_two_pointers(l_list: LinkedList, k):
    slow_p = l_list.head
    fast_p = l_list.head
    i = 0

    while i < k and fast_p:
        fast_p  = fast_p.next            
        i += 1

    while fast_p:
        fast_p = fast_p.next
        slow_p = slow_p.next
    print(slow_p.data)
    
print("Using 2 pointers")
kth_to_last_element_using_two_pointers(ll_instance, 6)
kth_to_last_element_using_two_pointers(ll_instance, 1)
kth_to_last_element_using_two_pointers(ll_instance, 9)