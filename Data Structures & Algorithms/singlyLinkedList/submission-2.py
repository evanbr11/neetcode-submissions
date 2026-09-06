class LinkedList:
    
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.data
            cur = cur.next
            i += 1
        return -1 # index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            # if list was empty before insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            # Move cur to node before target node
            i += 1
            cur = cur.next

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        temp = []
        cur = self.head.next
        while cur:
            temp.append(cur.data)
            cur = cur.next
        return temp
        
class Node:

    def __init__(self, data: int, next_node = None):
        self.data = data
        self.next = next_node