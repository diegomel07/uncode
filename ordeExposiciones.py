from dataclasses import dataclass
from typing import *


@dataclass
class Node:
    data: str = None
    next: 'Node' = None

@dataclass
class LinkedList:
    head: 'Node' = None
    tail: 'Node' = None
    size: int = 0

    def pushBack(self, data: str):
        new_node: Type[Node] = Node(data=data, next=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pushFront(self, data: str):
        new_node: Type[Node] = Node(data=data, next=self.head)

        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def popFront(self) -> str:
        deletedVal: Type[str] = ''

        if not self.head:
            raise ValueError("Empty List!")
        
        deletedVal = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        
        self.size -= 1
        return deletedVal

    def popBack(self) -> str:
        deletedVal: Type[str] = ''

        if not self.head:
            raise ValueError("Empty List!")
        
        if self.head == self.tail:
            deletedVal = self.head.data
            self.head = None
            self.tail = None

        else:
            ref: Type[Node] = self.head
            while ref.next != self.tail:
                ref = ref.next

            deletedVal = self.tail.data
            ref.next = None
            self.tail = ref
        
        self.size -= 1
        return deletedVal
    
    def printList(self):
        ref = self.head
        while ref:
            print(ref.data, end='')
            ref = ref.next
            if ref:
                print(" ", end="")

if __name__ == "__main__":

    lisitaNombres = LinkedList()
   
    for e in input().split():
        lisitaNombres.pushBack(e)

    lisitaNombresOrganizados = LinkedList()
    
    while lisitaNombres.size:
        lisitaNombresOrganizados.printList()
        lisitaNombresOrganizados.pushBack(lisitaNombres.popFront())
        if lisitaNombres.size:
            lisitaNombresOrganizados.pushBack(lisitaNombres.popBack())

    lisitaNombresOrganizados.printList()