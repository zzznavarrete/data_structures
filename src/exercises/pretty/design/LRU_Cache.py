"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. 
        - Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # Remove from node dll
    def remove(self, node):
        prev, nxt = node.prev, node.next
        nxt.prev, prev.next = prev, nxt

    # Insert at right prev
    def insert(self, node):
        temp = self.right.prev
        node.next = self.right
        node.prev = temp
        temp.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        # If there is no key in the cache
        if key not in self.cache:
            return -1  
        # Remove and insert from the DLL
        # This represents the key being recently used
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # Update the value of the key if the key exists.
        if key in self.cache:
            self.remove(self.cache[key])
        # add the key-value pair to the cache and DLL
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # If the number of keys exceeds the capacity
        # from this operation, 
        # evict the least recently used key.
        if len(self.cache) > self.cap:
            # The least recently used key is the node immediately
            # next to the left dummy node
            lru = self.left.next
            # Evict the node from the DLL
            self.remove(lru)
            # Evict the node from the cache
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)








