# Queue class implements a queue data structure (FIFO - First In First Out)
class Queue :
  # Constructor to initialize an empty queue
  def __init__(self):
    self.queue = []  # Internal list to store queue elements

  # Method to get the number of elements in the queue
  def length(self):
    return len(self.queue)
  
  # Method to check if the queue is empty
  def isEmpty(self):
    return self.length() == 0

  # Method to insert (enqueue) a value at the rear of the queue
  def insert(self, value):
    self.queue.append(value)  # Add value to the end of the list

  # Method to delete (dequeue) a value from the front of the queue
  def delete(self):
    if(self.isEmpty()):  # Check if queue is empty
      raise Exception("Queue is empty.")  # Raise exception if empty
    else :
      return self.queue.pop(0)  # Remove and return the first element
    
# Test code to demonstrate queue operations
obj1 = Queue()
obj1.insert(10)  # Insert 10 at the rear of the queue
obj1.insert(20)  # Insert 20 at the rear of the queue
print(obj1.delete())  # Delete and print from front (10)
obj1.insert(30)  # Insert 30 at the rear of the queue
