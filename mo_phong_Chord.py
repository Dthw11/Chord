import hashlib

class Node:
    def __init__(self, id):
        self.id = id
        self.finger_table = []

    def set_finger_table(self, nodes, m):
        self.finger_table = [(self.id + 2**i) % (2**m) for i in range(m)]
        self.finger_table = [min([node for node in nodes if node >= entry], default=min(nodes)) for entry in self.finger_table]

    def find_successor(self, key, nodes):
        if key == self.id or (key > self.id and key <= self.finger_table[0]):
            return self.finger_table[0]
        for i in range(len(self.finger_table) - 1, -1, -1):
            if self.finger_table[i] < key:
                return self.finger_table[i]
        return min(nodes)

# Thực nghiệm
nodes = [0, 1, 3, 5, 6]
m = 3
nodes_objects = [Node(id) for id in nodes]
for node in nodes_objects:
    node.set_finger_table(nodes, m)

# Tìm kiếm
start_node = nodes_objects[0]
key_to_find = 5
current_node = start_node
while True:
    successor = current_node.find_successor(key_to_find, nodes)
    if successor == key_to_find:
        print(f"Key {key_to_find} found at node {successor}")
        break
    current_node = nodes_objects[nodes.index(successor)]
