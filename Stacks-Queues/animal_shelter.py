# An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based
# on arrival time) of all animals at the shelter, or they can select whether
# they would prefer dog or a cat (and will receive the oldest animal of that
# type). They cannot select which specific animal tehy would ike. create the
# data structure to maintain this system and implement operations such as
# enqueue, dequeueAny, dequeueDog, dequeueCat. You may use built-in LinkedList
#  data structure.


class Node:
    def __init__(self, data, position) -> None:
        self.data = data
        self.next = None
        self.position = position


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def dequeue(self):
        if self.head:
            temp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return temp
        else:
            raise Exception("Empty Stack")

    def enqueue(self, element, position):
        node = Node(data=element, position=position)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def display(self):
        node = self.head
        while node:
            print((node.data, node.position), end="->")
            node = node.next
        print()


class AnimalShelter:
    def __init__(self) -> None:
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.position = 1

    def dequeue_cat(self):
        return self.cats.dequeue()

    def dequeue_dog(self):
        return self.dogs.dequeue()

    def dequeue_any(self):
        if self.cats.size > 0 and self.dogs.size > 0:
            if self.cats.head.position < self.dogs.head.position:
                return self.cats.dequeue()
            else:
                return self.dogs.dequeue()

    def enqueue(self, data):
        if data == "dog":
            self.dogs.enqueue(element=data, position=self.position)
        else:
            self.cats.enqueue(element=data, position=self.position)
        self.position += 1


animal_shelter = AnimalShelter()

animal_shelter.enqueue("dog")
animal_shelter.enqueue("cat")
animal_shelter.enqueue("cat")
animal_shelter.enqueue("cat")
animal_shelter.enqueue("dog")
animal_shelter.enqueue("dog")
animal_shelter.enqueue("cat")

animal_shelter.dogs.display()
animal_shelter.cats.display()

print(animal_shelter.dequeue_any())
print(animal_shelter.dequeue_cat())
print(animal_shelter.dequeue_any())

animal_shelter.dogs.display()
animal_shelter.cats.display()
