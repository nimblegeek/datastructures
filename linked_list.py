# Step 1: Define the Node class

class Node:
    def __init__(self, data):
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
        if not self.head: # If list is empty, do nothing
            return
        current = self.head 
        while current.next: # Traverse to find the node
            if current.next.data == data:
                current.next = current.next.next # Skip the node to delete
                return
            current = current.next

    # Display the linked list
    def display(self):
        elements = []
        current = self.head
        while current: # Traverse the list
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")
        
# Step 3: Test the LinkedList
if __name__ == "__main__":
    # Create a new linked list
    llist = LinkedList()

    # Add some elements
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(0)

    # Display the list
    print("Linked List:")
    llist.display() # Output: 0 -> 1 -> 2 -> 3

    # Delete an element
    llist.delete(2)
    print("After deleting 2:")
    llist.display() # Output: 0 -> 1 -> 3