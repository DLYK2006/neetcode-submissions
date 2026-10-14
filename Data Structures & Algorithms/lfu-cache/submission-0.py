class Node:
    def __init__(self, key, val):
        self.key = key
        self.count = 1
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        nxt = self.head.next
        node.prev = self.head
        node.next = nxt
        self.head.next = node
        nxt.prev = node
        self.size += 1

    def remove(self, node):
        behind = node.prev
        nxt = node.next
        behind.next = nxt
        nxt.prev = behind
        self.size -= 1

    def pop_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.freqtolist = defaultdict(DoublyLinkedList)
        self.keytonode = {}

    def update_freq(self, node):
        freq = node.count
        curr = self.freqtolist[freq]
        curr.remove(node)
        if freq == self.min_freq and curr.size == 0:
            self.min_freq += 1
        node.count += 1
        self.freqtolist[node.count].add_to_head(node)

    def get(self, key: int) -> int:
        if key in self.keytonode:
            node = self.keytonode[key]
            self.update_freq(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.keytonode:
            node = self.keytonode[key]
            node.val = value
            self.update_freq(node)
            return
        if len(self.keytonode) >= self.capacity:
            lru = self.freqtolist[self.min_freq]
            evicted = lru.pop_tail()
            if evicted:
                del self.keytonode[evicted.key]

        # Insert new node
        new_node = Node(key, value)
        self.keytonode[key] = new_node
        self.min_freq = 1
        self.freqtolist[1].add_to_head(new_node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
