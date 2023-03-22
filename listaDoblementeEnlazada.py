from dataclasses import dataclass
from typing import *


@dataclass
class Node:
    prev: 'Node' = None
    data: str = None
    next: 'Node' = None

@dataclass
class DoublyLinkedList:
    head: 'Node' = None
    tail: 'Node' = None
    size: int = 0

    def pushBack(self, data: str):
        new_node: Type['Node'] = Node(data=data)
        
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def popBack(self) -> str:
        deletedValue: Type[str] = ''

        if not self.head:
            raise ValueError('Empty list!')
        
        if self.head == self.tail:
            deletedValue = self.head.data
            self.tail = None
            self.head = None
        else:
            deletedValue = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return deletedValue 
        
    def popFront(self) -> str:
        deletedValue: Type[str] = ''

        if not self.head:
            raise ValueError("Empty List!")
        
        deletedValue = self.head.data

        if self.head.next:
            self.head.next.prev = None

        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        
        self.size -= 1

        return deletedValue

    
    def printList(self):
        ref = self.head
        while ref:
            print(ref.data, end='')
            ref = ref.next
            if ref:
                print(" ", end="")


if __name__ == "__main__":

    lisitaNombres = DoublyLinkedList()
   
    for e in input().split():
        lisitaNombres.pushBack(e)

    lisitaNombresOrganizados = DoublyLinkedList()
    
    while lisitaNombres.size:
        lisitaNombresOrganizados.pushBack(lisitaNombres.popFront())
        if lisitaNombres.size:
            lisitaNombresOrganizados.pushBack(lisitaNombres.popBack())

    lisitaNombresOrganizados.printList()
