# Node class represents a single node in the circular linked list
class Node :
  # Constructor to initialize node with data and next pointer
  def __init__(self, data, next = None):
    self.data = data  # Stores the data value of the node
    self.next = next  # Pointer to the next node in the list


# CircularSinglyLinkedList class implements a circular singly linked list data structure
class CircularSinglyLinkedList :
  # Constructor to initialize the circular linked list with an optional head node
  def  __init__(self, head= None):
    self.head = head  # Points to the first node in the list

  # Method to insert a new node at the beginning of the circular list
  def insertionAtBeg(self, value):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    if(t1 == None):  # If list is empty
      t1 = temp
      t1.next = t1  # Point to itself (circular)
      self.head = t1
    else :  # If list is not empty
      temp.next = t1  # Point new node to current head
      while(t1.next != self.head):  # Traverse to find the last node
        t1 = t1.next
      t1.next = temp  # Link last node to new node
      t1 = temp  # Update head to new node
      self.head = t1

  # Method to insert a new node at the end of the circular list
  def insertionAtEnd(self, value):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    if(t1 != None):  # If list is not empty
      while(t1.next != self.head):  # Traverse to the last node
        t1= t1.next
      t1.next = temp  # Link last node to new node
      temp.next = self.head  # Point new node to head (circular)
    else :  # If list is empty
      t1 = temp
      t1.next = t1  # Point to itself (circular)
      self.head = t1

  # Method to insert a new node after a given value (x) in the circular list
  def insertionAtMid(self, value, x):
    temp = Node(value)  # Create a new node with the given value
    t1 = self.head
    
    while(t1.next != self.head):  # Traverse the list to find the node with value x
      if(t1.data == x):  # If current node's data matches x
        temp.next = t1.next  # Point new node to the next node
        t1.next = temp  # Link current node to the new node
        return
      t1 = t1.next
    t1.next = temp  # If x not found, insert at end
    temp.next = self.head  # Point to head (circular)

  # Method to delete a node with a given value from the circular list
  def deleteNode(self, value):
    t1 = self.head  # Pointer to traverse the list
    t0 = self.head  # Pointer to keep track of previous node
    if(t1 == None):  # If list is empty
      # print("Linked list is empty.")
      return
    else:
      if(t1.next == self.head):  # If only one node exists
        if(t1.data == value):  # If head node contains the value
          t1 = None
          self.head = t1
          return
      else:
          if(t1.data == value):  # If head node contains the value
            temp = self.head
            while(temp.next != self.head):  # Find the last node
              temp = temp.next
            temp.next = t1.next  # Link last node to next of head
            self.head = t1.next  # Update head
            return
      
    while(t1.next != self.head):  # Traverse to find the node to delete
      if(t1.data == value):  # If current node's data matches value
        t0.next = t1.next  # Link previous node to next node
        return
      else :
        t0 = t1  # Update previous node
        t1 = t1.next  # Move to next node
    
    if(t1.data == value):  # If the last node contains the value
      t0.next = self.head  # Link previous node to head (circular)
      t1 = t0
    else :
      print("No node exist for delete.")


  # Method to print all nodes in the circular linked list
  def printNode(self):
    temp = self.head  # Start from the head
    if(temp == None):  # If list is empty
      print("Linked list is empty.")
      return
    else:
      while(temp.next != self.head):  # Traverse and print each node
        print(temp.data, end= " -->> ")
        temp = temp.next
      print(temp.data)  # Print the last node

  
      



# Test code to demonstrate the circular singly linked list operations
obj1 = CircularSinglyLinkedList()
obj1.insertionAtBeg(10)  # Insert 10 at beginning
obj1.insertionAtBeg(20)  # Insert 20 at beginning
obj1.insertionAtBeg(30)  # Insert 30 at beginning
obj1.insertionAtBeg(40)  # Insert 40 at beginning
obj1.insertionAtEnd(50)   # Insert 50 at end
obj1.insertionAtEnd(60)   # Insert 60 at end
obj1.insertionAtEnd(70)   # Insert 70 at end
obj1.insertionAtEnd(80)   # Insert 80 at end
obj1.insertionAtMid(5,50)  # Insert 5 after node with data 50
obj1.deleteNode(10)  # Delete node with data 10




obj1.printNode()
