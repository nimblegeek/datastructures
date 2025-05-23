# Step 1: Define the Node class

class __init__(self, data):
    self.data = data #Store data
    self.next = None #Store reference (or pointer) to next node

# Step 2: Define the LinkedList class
class LinkedList: 
    def __init__(self):
        self.head = None #Initialize the head of the list as None

    # Append a new node to the end of the list
    def append(self, data):
        new_node = Node(data) # Create a new node
        if not self.head: # If the list is empty, set the new node as head
            self.head = new_node
            return
        current = self.head 
        while current.next: #Traverse to the last node
            current = current.next
        current.next = new_node # Link the new node at the end

    # Prepend a new node to the beginning of the list
    def prepend(self, data): 
        new_node = Node(data)
        new_node.next = self.head # Link a new node to current head
        self.head = new_node # Update head to the new node
    
    # Delete a node with specific data
    def delete(self, data):
        if not self.head: 