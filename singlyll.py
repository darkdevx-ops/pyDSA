# Node class represents a single node in the linked list
class Node :
  # Constructor to initialize node with data and next pointer
  def __init__(self, data, next = None):
    self.data = data  # Stores the data value of the node
    self.next = next  # Pointer to the next node in the list


# SinglyLinkedList class implements a singly linked list data structure
class SinglyLinkedList :
  # Constructor to initialize the linked list with an optional head node
  def  __init__(self, head= None):
    self.head = head  # Points to the first node in the list

  # Method to insert a new node at the beginning of the list
  def insertionAtBeg(self, value):
    temp = Node(value)  # Create a new node with the given value
    if(self.head == None):  # If list is empty
      self.head = temp  # Set the new node as head
    else :  # If list is not empty
      temp.next = self.head  # Point new node to current head
      self.head = temp  # Update head to new node

  # Method to insert a new node at the end of the list
  def insertionAtEnd(self, value):
    temp = Node(value)  # Create a new node with the given value
    if(self.head != None):  # If list is not empty
      t1 = self.head  # Start from the head
      while(t1.next != None):  # Traverse to the last node
        t1= t1.next
      t1.next = temp  # Link the last node to the new node
    else :  # If list is empty
      self.head = temp  # Set the new node as head

  # Method to insert a new node after a given value (x) in the list
  def insertionAtMid(self, value, x):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    
    while(t1.next != None):  # Traverse the list to find the node with value x
      if(t1.data == x):  # If current node's data matches x
        temp.next = t1.next  # Point new node to the next node
        t1.next = temp  # Link current node to the new node
        return
      t1 = t1.next
    t1.next = temp  # If x not found, insert at end

  # Method to delete a node with a given value from the list
  def deleteNode(self, value):
    t1 = self.head  # Pointer to traverse the list
    t0 = self.head  # Pointer to keep track of previous node
    if(t1 == None):  # If list is empty
      # print("Linked list is empty.")
      return
    else:

      if(t1.data == value):  # If head node contains the value to delete
        t1 = t1.next  # Move head to next node
        self.head = t1
        return
    
    while(t1.next != None):  # Traverse to find the node to delete
      if(t1.data == value):  # If current node's data matches value
        t0.next = t1.next  # Link previous node to next node
        return
      else :
        t0 = t1  # Update previous node
        t1 = t1.next  # Move to next node
    
    if(t1.data == value):  # If the last node contains the value
      t0.next = None  # Set previous node's next to None
      t1 = t0
    else :
      print("No node exist for delete.")

  # Method to print all nodes in the linked list
  def printNode(self):
    temp = self.head  # Start from the head
    if(temp == None):  # If list is empty
      print("Linked list is empty.")
      return
    else:
      while(temp.next != None):  # Traverse and print each node
        print(temp.data, end= " --> ")
        temp = temp.next
      print(temp.data)  # Print the last node

    



# Test code to demonstrate the singly linked list operations
obj1 = SinglyLinkedList()
obj1.insertionAtBeg(10)  # Insert 10 at beginning
obj1.insertionAtBeg(30)  # Insert 30 at beginning
obj1.insertionAtBeg(50)  # Insert 50 at beginning
obj1.insertionAtEnd(5)   # Insert 5 at end
obj1.insertionAtEnd(15)  # Insert 15 at end
obj1.insertionAtMid(35,10)  # Insert 35 after node with data 10
obj1.insertionAtMid(45,15)  # Insert 45 after node with data 15
obj1.insertionAtMid(25,50)  # Insert 25 after node with data 50
obj1.deleteNode(10)  # Delete node with data 10
obj1.deleteNode(50)  # Delete node with data 50
obj1.deleteNode(45)  # Delete node with data 45
obj1.deleteNode(25)  # Delete node with data 25
obj1.deleteNode(5)   # Delete node with data 5
obj1.deleteNode(15)  # Delete node with data 15
obj1.deleteNode(35)  # Delete node with data 35
obj1.deleteNode(30)  # Delete node with data 30
obj1.deleteNode(42)  # Try to delete node with data 42 (doesn't exist)



# Print the final linked list
obj1.printNode()