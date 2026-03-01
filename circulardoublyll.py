# Node class represents a single node in the circular doubly linked list
class Node :
  # Constructor to initialize node with data, next and previous pointers
  def __init__(self, data, next= None, prev= None):
    self.data = data  # Stores the data value of the node
    self.next = next  # Pointer to the next node in the list
    self.prev = prev  # Pointer to the previous node in the list

# CircularDoubleLinkedList class implements a circular doubly linked list data structure
class CircularDoubleLinkedList :
  # Constructor to initialize the circular doubly linked list with an optional head node
  def __init__(self, head = None):
    self.head = head  # Points to the first node in the list

  # Method to insert a new node at the beginning of the circular doubly list
  def insertionAtBeg(self, value):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    if(t1 == None):  # If list is empty
      t1 = temp
      t1.next = temp  # Point to itself
      t1.prev = temp  # Point to itself
      self.head = t1
    else:
      t1.prev = temp  # Set current head's prev to new node
      temp.next = t1  # Point new node to current head
      while(t1.next != self.head):  # Traverse to find the last node
        t1 = t1.next
      temp.prev = t1  # Set new node's prev to last node
      t1.next = temp  # Link last node to new node
      self.head = temp  # Update head to new node

  # Method to insert a new node at the end of the circular doubly list
  def insertionAtEnd(self, value):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    if(t1 != None):  # If list is not empty
      t1.prev = temp  # Set current head's prev to new node
      temp.next = t1  # Point new node to head
      while(t1.next != self.head):  # Traverse to find the last node
        t1= t1.next
      t1.next = temp  # Link last node to new node
      temp.prev = t1  # Set new node's prev to last node
    else :  # If list is empty
      t1 = temp
      t1.next = temp  # Point to itself
      t1.prev = temp  # Point to itself
      self.head = t1

  # Method to insert a new node after a given value (x) in the circular doubly list
  def insertionAtMid(self, value, x):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    
    while(t1.next != self.head):  # Traverse the list to find the node with value x
      if(t1.data == x):  # If current node's data matches x
        temp.next = t1.next  # Point new node to the next node
        t1.next.prev = temp  # Set next node's prev to new node
        t1.next = temp  # Link current node to the new node
        temp.prev = t1  # Set new node's prev to current node
        return
      t1 = t1.next
    t1.next = temp  # If x not found, insert at end
    temp.prev = t1  # Set new node's prev to last node
    temp.next = self.head  # Point new node to head (circular)
    self.head.prev = temp  # Set head's prev to new node

  # Method to delete a node with a given value from the circular doubly list
  def deleteNode(self, value):
    t1 = self.head  # Pointer to traverse the list
    if(t1 == None):  # If list is empty
      # print("Linked list is empty.")
      return
    else:
      if(t1.data == value):  # If head node contains the value
        if(t1.next == self.head):  # If only one node exists
          t1 = None
          self.head = t1
        else:
          t1 = t1.next  # Move to next node
          t1.prev = t1  # Update prev pointer
          t1.next = t1  # Update next pointer
          self.head = t1  # Update head
        return
      
    while(t1.next != self.head):  # Traverse to find the node to delete
      if(t1.data == value):  # If current node's data matches value
        t1.prev.next = t1.next  # Link previous node to next node
        t1.next.prev = t1.prev  # Link next node to previous node
        return
      else :
        t1 = t1.next  # Move to next node

    if(t1.data == value):  # If the last node contains the value
      t1.prev.next = self.head  # Link previous node to head
      self.head.prev = t1.prev  # Update head's prev pointer
    else :
      print("No node exist for delete.")

  # Method to print all nodes in the circular doubly linked list
  def printNode(self):
    t1 = self.head  # Start from the head
    if(t1 == None):  # If list is empty
      print("Linked list is empty.")
      return
    else:
      while(t1.next != self.head):  # Traverse and print each node
        print(t1.data, end= " <<-->> ")
        t1 = t1.next
      print(t1.data)  # Print the last node




# Test code to demonstrate the circular doubly linked list operations
obj1 = CircularDoubleLinkedList()
obj1.insertionAtBeg(10)  # Insert 10 at beginning
obj1.insertionAtBeg(20)  # Insert 20 at beginning
obj1.insertionAtBeg(30)  # Insert 30 at beginning
obj1.insertionAtEnd(5)   # Insert 5 at end
obj1.insertionAtEnd(15)  # Insert 15 at end
obj1.insertionAtMid(25, 5)  # Insert 25 after node with data 5
obj1.deleteNode(25)  # Delete node with data 25
obj1.deleteNode(5)   # Delete node with data 5
obj1.deleteNode(15)  # Delete node with data 15
obj1.deleteNode(20)  # Delete node with data 20
obj1.deleteNode(30)  # Delete node with data 30
obj1.deleteNode(10)  # Delete node with data 10

obj1.printNode()
