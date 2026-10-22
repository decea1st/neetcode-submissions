class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def add(self, key, val):
        new = ListNode(key, val, self.head, self.head.prev)
        self.head.prev.next = new
        self.head.prev = new
        self.nodeMap[key] = new
        return

    def update(self, key, val):
        curr = self.nodeMap[key]
        curr.val = val
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.prev = self.head.prev
        curr.next = self.head
        self.head.prev.next = curr
        self.head.prev = curr
        return

    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.maxLen = capacity
        self.tail = ListNode()
        self.head = ListNode(0, 0, None, self.tail)
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if key in self.nodeMap:
            self.update(key, self.nodeMap[key].val)
            return self.nodeMap[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.update(key, value)
            return

        if len(self.nodeMap) < self.maxLen:
            self.add(key, value)
            return
        
        else:
            del self.nodeMap[self.tail.next.key]
            self.tail.next = self.tail.next.next
            self.tail.next.prev = self.tail
            self.add(key, value)
            return