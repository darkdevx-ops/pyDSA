class Node :
  def __init__(self, data, next= None, prev= None):
    self.data = data
    self.next = next
    self.prev = prev


class DoubleLinkedList :
  def __init__(self, head = None):
    self.head = head

  def insertionAtBeg(self, value):
    temp = Node(value)
    t1 = self.head
    if(t1 == None):
      self.head = temp
    else:
      t1.prev = temp
      temp.next = t1
      self.head = temp

  def insertionAtEnd(self, value):
    temp = Node(value)
    if(self.head != None):
      t1 = self.head
      while(t1.next != None):
        t1= t1.next
      t1.next = temp
      temp.prev = t1
    else :
      self.head = temp

  def insertionAtMid(self, value, x):
    temp = Node(value)
    t1 = self.head
    
    while(t1.next != None):
      if(t1.data == x):
        temp.next = t1.next
        t1.next.prev = temp
        t1.next = temp
        temp.prev = t1
        return
      t1 = t1.next
    t1.next = temp
    temp.prev = t1

  def deleteNode(self, value):
    t1 = self.head
    if(t1 == None):
      # print("Linked list is empty.")
      return
    else:
      if(t1.next == None or t1.data == value):
        t1 = t1.next
        self.head = t1
        return
    
    while(t1.next != None):
      if(t1.data == value):
        t1.prev.next = t1.next
        t1.next.prev = t1.prev
        return
      else :
        t1 = t1.next
    
    if(t1.data == value):
      t1.prev.next = None
    else :
      print("No node exist for delete.")

  def printNode(self):
    t1 = self.head
    if(t1 == None):
      print("Linked list is empty.")
      return
    else:
      while(t1.next != None):
        print(t1.data, end= " <--> ")
        t1 = t1.next
      print(t1.data)


obj1 = DoubleLinkedList()
obj1.insertionAtBeg(10)
obj1.insertionAtBeg(20)
obj1.insertionAtBeg(30)
obj1.insertionAtEnd(5)
obj1.insertionAtEnd(15)
obj1.insertionAtMid(25, 10)
obj1.insertionAtMid(35, 30)
obj1.insertionAtMid(45, 20)
obj1.deleteNode(10)
obj1.deleteNode(45)
obj1.deleteNode(20)
obj1.deleteNode(30)
obj1.deleteNode(35)
obj1.deleteNode(5)
obj1.deleteNode(15)
obj1.deleteNode(25)
obj1.deleteNode(42)










obj1.printNode()
    