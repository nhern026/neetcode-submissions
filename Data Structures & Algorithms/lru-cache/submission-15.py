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

        self.least = Node(None, None)
        self.most = Node(None, None)
        self.most.prev = self.least
        self.least.nxt = self.most

    def add_MRU(self, node) -> None:
        node.prev = self.most.prev
        self.most.prev.nxt = node
        self.most.prev = node
        node.nxt = self.most

    def remove_node(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def remove_LRU(self) -> None:
        self.remove_node(self.least.nxt)

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        else:
            self.remove_node(self.key2node[key])
            self.add_MRU(self.key2node[key])

            return self.key2node[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            self.remove_node(self.key2node[key])
            self.key2node[key].value = value
        else:  
            if len(self.key2node) == self.capacity:
                del self.key2node[self.least.nxt.key]
                self.remove_LRU()
            new_node = Node(key, value)
            self.key2node[key] = new_node


        self.add_MRU(self.key2node[key])

    # def put(self, key: int, value: int) -> None:
    #     if key in self.key2node:
    #         # remove from DLL
    #         self.remove_node(self.key2node[key])

    #         self.key2node[key].value = value

    #         self.add_MRU(self.key2node[key])

    #     else: # key is NOT in key2node            
    #         if len(self.key2node) == self.capacity:
    #             # remove LRU from map and DLL
    #             del self.key2node[self.least.nxt.key]
    #             self.remove_LRU()

    #         # add new key to map and as MRU
    #         new_node = Node(key, value)
    #         self.key2node[key] = new_node
    #         self.add_MRU(new_node)