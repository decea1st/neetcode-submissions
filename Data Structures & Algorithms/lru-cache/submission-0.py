class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def add(self, key):
        new = ListNode(key, self.head, self.head.prev)
        self.head.prev.next = new
        self.head.prev = new
        self.nodeMap[key] = new
        return
    # t 1 2 h  ->  t 2 1 h
    # t   2 h
    #      1 
    def update(self, key):
        curr = self.nodeMap[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.prev = self.head.prev
        curr.next = self.head
        self.head.prev.next = curr
        self.head.prev = curr
        return

    def __init__(self, capacity: int):
        self.maxLen = capacity
        self.currLen = 0
        self.lru = {}
        self.tail = ListNode()
        self.head = ListNode(0, None, self.tail)
        self.tail.next = self.head
        self.nodeMap = {}

    def get(self, key: int) -> int:
        if key in self.lru:
            self.update(key)
            return self.lru[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            # Update old entry
            self.update(key)
            return

        if self.currLen < self.maxLen:
            self.lru[key] = value
            self.currLen += 1
            # Add new entry
            self.add(key)
            return
        
        else:
            print(key)
            print(self.lru)
            print(self.maxLen)
            print(self.tail.next.val)
            del self.lru[self.tail.next.val]
            self.lru[key] = value
            self.tail.next = self.tail.next.next
            self.tail.next.prev = self.tail
            self.add(key)
            return
