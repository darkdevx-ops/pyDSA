class Node :
  def __init__(self, data, next = None):
    self.data = data
    self.next = next


class CircularSinglyLinkedList :
  def  __init__(self, head= None):
    self.head = head

  def insertionAtBeg(self, value):
    temp = Node(value)
    t1 = self.head
    if(t1 == None):
      t1 = temp
      t1.next = t1
      self.head = t1
    else :
      temp.next = t1
      while(t1.next != self.head):
        t1 = t1.next
      t1.next = temp
      t1 = temp
      self.head = t1

  def insertionAtEnd(self, value):
    temp = Node(value)
    t1 = self.head
    if(t1 != None):
      while(t1.next != self.head):
        t1= t1.next
      t1.next = temp
      temp.next = self.head
    else :
      t1 = temp
      t1.next = t1
      self.head = t1

  def insertionAtMid(self, value, x):
    temp = Node(value)
    t1 = self.head
    
    while(t1.next != self.head):
      if(t1.data == x):
        temp.next = t1.next
        t1.next = temp
        return
      t1 = t1.next
    t1.next = temp
    temp.next = self.head

  def deleteNode(self, value):
    t1 = self.head
    t0 = self.head
    if(t1 == None):
      # print("Linked list is empty.")
      return
    else:
      if(t1.next == self.head):
        if(t1.data == value):
          t1 = None
          self.head = t1
          return
      else:
          if(t1.data == value):
            temp = self.head
            while(temp.next != self.head):
              temp = temp.next
            temp.next = t1.next
            self.head = t1.next
            return
      
    while(t1.next != self.head):
      if(t1.data == value):
        t0.next = t1.next
        return
      else :
        t0 = t1
        t1 = t1.next
    
    if(t1.data == value):
      t0.next = self.head
      t1 = t0
    else :
      print("No node exist for delete.")


  def printNode(self):
    temp = self.head
    if(temp == None):
      print("Linked list is empty.")
      return
    else:
      while(temp.next != self.head):
        print(temp.data, end= " -->> ")
        temp = temp.next
      print(temp.data)

  
      



obj1 = CircularSinglyLinkedList()
obj1.insertionAtBeg(10)
obj1.insertionAtBeg(20)
obj1.insertionAtBeg(30)
obj1.insertionAtBeg(40)
obj1.insertionAtEnd(50)
obj1.insertionAtEnd(60)
obj1.insertionAtEnd(70)
obj1.insertionAtEnd(80)
obj1.insertionAtMid(5,50)
obj1.deleteNode(10)






obj1.printNode()
