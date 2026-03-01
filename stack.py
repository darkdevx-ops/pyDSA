# Stack class implements a stack data structure (LIFO - Last In First Out)
class Stack :
  # Constructor to initialize an empty stack
  def __init__(self):
    self.stack = []  # Internal list to store stack elements

  # Method to get the number of elements in the stack
  def length(self):
    return len(self.stack)
  
  # Method to check if the stack is empty
  def isEmpty(self):
    return self.length() == 0
  
  # Method to insert (add) a value onto the top of the stack
  def insert(self, value):
    self.stack.append(value)  # Add value to the end of the list
  
  # Method to delete (remove) the top element from the stack
  def delete(self):
    if(self.isEmpty()):  # Check if stack is empty
      raise Exception("Stack is Empty")  # Raise exception if empty
    else :
      return self.stack.pop()  # Remove and return the last element
    
  # Method to view the top element without removing it
  def peek(self):
    if(self.isEmpty()):  # Check if stack is empty
      print("Stack is empty.")  # Print message if empty
    else :
      print(self.stack[self.length() - 1 ])  # Print the top element
      

# Test code to demonstrate stack operations
obj1 = Stack()
obj1.insert(10)  # Insert 10 onto the stack
obj1.insert(20)  # Insert 20 onto the stack

print(obj1.delete())  # Delete and print the top element (20)
obj1.peek()  # Peek at the current top element (10)
