# seria crear la lista principal

# para cada elemento
# guardar el node actual
# empezar a revisar(con otro nodo) la lista hasta que el node.data sea mayor la data del nodo actual o null


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

    def pushBack(self, data: int):
        new_node: Type[Node] = Node(data=data, next=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


def chekForThatDay(actualNode: Node) -> int:

    if not actualNode.next:
        return 0

    ref: Type[Node] = actualNode.next
    count: Type[int] = 1

    while ref:
        if ref and ref.data > actualNode.data:
            break
        ref = ref.next
        count += 1
        
            
    if not ref:
        return 0

    return count


if __name__ == "__main__":

    lisitaPrecios = LinkedList()
   
    for e in input().split():
        lisitaPrecios.pushBack(int(e))

    dias: List[int] = list()
    ref: Type[Node] = lisitaPrecios.head
    while ref:
        dias.append(chekForThatDay(ref))
        ref = ref.next
    
    print(*dias, end='')

        