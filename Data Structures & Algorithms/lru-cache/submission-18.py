# Session 2, attempt 1

"""
So a key is MRU if its called in get or put. So update on both occassions

We want the fastest access for get so we need some sort of hashamp with the keys as keys and the values as values (this may change)

we need put to run in O(1) time, this changes how we shuold do this because we need some sort of way to keep track of MRU and LRU. in order for us to do that, we need some sort of doubly linked list, so then the values in the hashmap shoudl be the nodes in the DLL so that we can get immediate access for updating them. 

to delete LRU as it says when we go over capacity, we would udpate the LRU node to skip wtvr is next of it. 
to set a node to MRU we set it as the previous to the MRU node. wheter new or already in there (if its already in there we have to remove it from its current position first)

capacity will alwyas be bigger than 0. 
keys and vals can be >= 0

okay so here is the final idea:
hashamp (key: node in DLL)
DLL: LRU node as tail, MRU node as head. 

get: will retrieve value in node from the hasmap using our key. update that node as MRU
put: if key is already there we will update val and make that node as MRU. if not then we add new node as MRU

each call is O(1) since its constant amount of operations for each operation.
space complexity is O(capacity) where capacity is the amount of keys we can hodl at once, as long as each val is jjust an integer. 
"""

class Node:
    def __init__(self, key=None, val=None, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = {}
        
        self.LRU_node = Node()
        self.MRU_node = Node(prev=self.LRU_node)
        self.LRU_node.nxt = self.MRU_node

    def make_MRU(self, node): # fresh node not in DLL
        self.key2val[node.key] = node
        """

        A-> <- Z -> <- M

        """

        node.prev = self.MRU_node.prev
        node.prev.nxt = node

        self.MRU_node.prev = node
        node.nxt = self.MRU_node

    
    def remove_node(self, node):
        key = node.key

        # deleting from our map
        del self.key2val[key]

        # deleting DLL node
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        

    def get(self, key: int) -> int:
        if key in self.key2val:
            node = self.key2val[key]
            self.remove_node(node)

            self.make_MRU(node)

            return self.key2val[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key2val:
            self.remove_node(self.key2val[key])
            
        new_node = Node(key=key, val=value)

        self.make_MRU(new_node)
            
        if len(self.key2val) > self.capacity:
            self.remove_node(self.LRU_node.nxt)
        
"""
LRUCache 2      {}      L-> <- M
key, val
1    10         {1:10}  L-> <- 1 -> <- M
2    20      {1:10, 2:20}   L-> <- 1 -> <- 2 -> <- M
3    30      {2:20, 3:30}     L-> <- 2 -> <- 3 -> <- M
get   2      {3:30, 2:20}     L-> <- 3 -> <- 2 -> <- M
get   1      -1


doing the tracing let me catch two bugs
1.  i forgot to pass in the LRU.nxt node in the remove if statement.
2.  i forgot to put key-node pair after removing node before makign it the MRU in get. so then i realized i can just put it in make_MRU


a few issues:
- forgot to put self in the helper functions i created
- kept putting self.key2vals[key] in the if key in self.key2vals (because i was copy and pasting)

"""








