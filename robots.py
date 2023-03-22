from dataclasses import dataclass
from time import sleep
from typing import *


@dataclass
class Node:
    prev: 'Node' = None
    data: int = None
    next: 'Node' = None

@dataclass
class DoublyLinkedList:
    head: 'Node' = None
    tail: 'Node' = None
    size: int = 0

    def pushBack(self, data: int):
        new_node: Type['Node'] = Node(data=data)
        
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def pushFront(self, data: int):
        new_node: Type[Node] = Node(data=data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1


    def popBack(self) -> int:
        deletedValue: Type[int] = 0

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
        
    def popFront(self) -> int:
        deletedValue: Type[int] = 0

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
    
    def isEmpty(self) -> bool:
        return not self.head
    
    def printList(self):
        ref = self.head
        while ref:
            print(ref.data, end='')
            ref = ref.next
            if ref:
                print(" ", end="")




def openFile() -> List[int]:
    with open('input11.in', 'r') as file:
        data = file.read().replace('\n', '')

    cadena: List[int] = [int(i) for i in data.split(' ')]
    return cadena


# 2 7 -3
# despues del pushback
# right --> -3
# left --> 2 7



def fight(powersLeft: DoublyLinkedList, powersRight: DoublyLinkedList) -> DoublyLinkedList:

    # pelear mientras alguno de los dos queda vacio
    while not powersLeft.isEmpty() and not powersRight.isEmpty():

        # sacar los dos que hay que enfrentar
        right: Type[int] = (powersRight.popFront()) * -1
        left: Type[int] = powersLeft.popBack()

        # si gana la derecha
        if right > left:
            powersRight.pushFront(right*-1)
        #si gana la izquierda
        elif left > right:
            powersLeft.pushBack(left)

    if powersLeft.isEmpty() and powersRight.isEmpty():
        return None
    elif powersRight.isEmpty():
        return powersLeft
    return powersRight



if __name__ == '__main__':
    
    powersLeft = DoublyLinkedList()
    powersRight = DoublyLinkedList()
    
    for e in openFile():
        if int(e) > 0:
            powersLeft.pushBack(int(e))
        else:
            powersRight.pushBack(int(e))

    result = fight(powersLeft, powersRight)

    if result:
        result.printList()
    else:
        print('No quedaron robots!', end='')

    
