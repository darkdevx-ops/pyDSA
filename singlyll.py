class Node :
  def __init__(self, data, next = None):
    self.data = data
    self.next = next


class SinglyLinkedList :
  def  __init__(self, head= None):
    self.head = head

  def insertionAtBeg(self, value):
    temp = Node(value)
    if(self.head == None):
      self.head = temp
        
    else :
      temp.next = self.head
      self.head = temp

  def insertionAtEnd(self, value):
    temp = Node(value)
    if(self.head != None):
      t1 = self.head
      while(t1.next != None):
        t1= t1.next
      t1.next = temp
    else :
      self.head = temp

  def insertAtMid(self, value, x):
    temp = Node(value)
    t1 = self.head
    
    while(t1.next != None):
      if(t1.data == x):
        temp.next = t1.next
        t1.next = temp
        return
      t1 = t1.next
    t1.next = temp
    
  def deleteNode(self, value):
    t1 = self.head
    t0 = self.head
    if(t1.data == value):
      t1 = t1.next
      self.head = t1
      return
    
    while(t1.next != None):
      if(t1.data == value):
        t0.next = t1.next
        return
      else :
        t0 = t1
        t1 = t1.next
    
    if(t1.data == value):
      t0.next = None
      t1 = t0
    else :
      print("No node exist for delete.")

  def printNode(self):
    temp = self.head
    if(temp == None):
      print("Linked list is empty.")
      return
    else:
      while(temp.next != None):
        print(temp.data, end= " --> ")
        temp = temp.next
      print(temp.data)

    



obj1 = SinglyLinkedList()
obj1.insertionAtBeg(10)
obj1.insertionAtBeg(30)
obj1.insertionAtBeg(50)
obj1.insertionAtEnd(5)
obj1.insertionAtEnd(15)
obj1.insertAtMid(35,10)
obj1.insertAtMid(45,15)
obj1.insertAtMid(25,50)
obj1.deleteNode(10)
obj1.deleteNode(50)
obj1.deleteNode(45)
obj1.deleteNode(20)
obj1.printNode()




