from dataclasses import dataclass
from typing import *


@dataclass
class Node:
    data: int = None
    next: 'Node' = None

@dataclass
class LinkedList:
    head: 'Node' = None
    tail: 'Node' = None
    size: int = 0

    def erase(self, index):
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            ref = self.head
            for _ in range(index - 1):
                ref = ref.next
            if ref.next.next is None:
                self.tail = ref
            ref.next = ref.next.next
        self.size -= 1

    def pushBack(self, data):
        new_node = Node(data=data, next=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pushFront(self, data):
        new_node = Node(data=data, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def printList(self):
        ref = self.head
        while ref != None:
            print(ref.data, end='')
            ref = ref.next
            if ref != None:
                print(" ", end="")

    def compare(self, otraLista):
        refOtra = otraLista.head
        refOri = self.head
        index = 0
        while refOtra is not None:
            if refOtra.data == refOri.data:
                self.erase(index)
                otraLista.erase(index)
                index -= 1
            refOtra = refOtra.next
            refOri = refOri.next
            index += 1

if __name__ == "__main__":
    
    lisita1 = LinkedList()
    for i in input().split():
        lisita1.pushBack(int(i))

    lisita2 = LinkedList()
    for i in input().split():
        lisita2.pushFront(int(i))

    lisita1.compare(lisita2)

    lisita3 = LinkedList()
    ref = lisita2.head
    while ref is not None:
        lisita3.pushFront(ref.data)
        ref = ref.next

    lisita1.printList()
    print()
    lisita3.printList()
