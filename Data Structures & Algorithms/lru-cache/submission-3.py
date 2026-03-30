class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node()
        self.tail = self.head

    def append(self, val:int):
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.size+=1
    
    def remove(self):
        if self.isEmpty():
            return
        if self.head.next == self.tail:
            res = self.tail.val
            self.tail = self.head
            return res
        res = self.head.next.val
        self.head.next = self.head.next.next
        self.size -= 1
        return res
        

    def removeAppend(self, val: int):
        cur = self.head
        while (cur.next != None) and (cur.next.val != val):
            cur = cur.next
        if cur.next == self.tail:
            self.tail = cur
        cur.next = cur.next.next
        self.size-=1
        self.append(val)

    def isEmpty(self):
        return self.head == self.tail


class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.cap = capacity
        self.q = LinkedList()

    def get(self, key: int) -> int:
        if self.q.size < 2 and key in self.hm:
            return self.hm.get(key)
        if key in self.hm:
            self.q.removeAppend(key)
            return self.hm.get(key)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key] = value
            self.q.removeAppend(key)
            return
        if self.q.size >= self.cap:
            k = self.q.remove()
            del self.hm[k]
        self.q.append(key)
        self.hm[key] = value


