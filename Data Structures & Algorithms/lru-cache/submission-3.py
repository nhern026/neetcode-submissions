# Session 1, attempt 1
class Node:
    def __init__(self, key, value, nxt=None, prev=None):
        self.key = key
        self.value = value
        self.nxt = nxt
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}
        self.length = 0

        self.least = Node(None, None)
        self.most = Node(None, None, prev=self.least)
        self.most.nxt = self.least

    def add_LRU(self, node) -> None:
        node.prev = self.most.prev
        self.most.prev.nxt = node
        self.most.prev = node
        node.nxt = self.most

    def remove_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def remove_LRU(self) -> None:
        temp = self.least.nxt
        self.least.nxt = self.least.nxt.nxt  
        temp.nxt.prev = self.least
        self.length -= 1

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        else:
            self.remove_node(self.key2node[key])
            self.add_LRU(self.key2node[key])

            return self.key2node[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            # remove from DLL
            self.remove_node(self.key2node[key])

            new_node = Node(key, value)
            self.key2node[key] = new_node

            self.add_LRU(new_node)

        else: # key is NOT in key2node
            self.length += 1
            
            if self.length > self.capacity:
                # remove LRU from map and DLL
                print(self.least.nxt.key)
                del self.key2node[self.least.nxt.key]
                self.remove_LRU()

            # add new key to map and as MRU
            new_node = Node(key, value)
            self.key2node[key] = new_node
            self.add_LRU(new_node)

          

        




        
