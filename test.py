
# Defining the class to store data

class Node:
    def __init__(self, data):
        self.data = data
        self.data.next = None # Store reference for next node (pointer)

# The class to store logic for adding and deleting nodes
class LinkedList: 
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # delete node with specific data
    def delete(self, data):
        if not self.head:
            return
        current = self.head
        while current.next == 
