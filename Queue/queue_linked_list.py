class QueueUnderFlowError(Exception):
  pass
class QueueOverFlowError(Exception):
  pass

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
    
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.capacity = 4
    self.size = 0

  def __len__(self):
    return self.size

  def __str__(self):
    if self.is_empty():
      return "List is empty"
    result = [str(node) for node in self]
    return f"=== QUEUE ITEMS ===\n[FRONT] {' -> '.join(result)} [REAR]"

  def __iter__(self):
    current = self.front
    while current:
      yield current.data
      current = current.next

  def __repr__(self):
    return f"Queue(size={len(self)})"

  def is_empty(self):
    return self.front is None

  def is_full(self):
    if self.capacity is None:
      return False
    return len(self) >= self.capacity

  def enqueue(self, item):
    if self.is_full():
      raise QueueOverFlowError("Cannot enqueue; 'Queue' is full.")
    node = Node(item)
    if self.is_empty():
      self.front = node
    else:
      self.rear.next = node
    self.rear = node
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      raise QueueUnderFlowError("Cannot dequeue; 'Queue' is empty.")
    del_node = self.front.data
    if not self.front.next:
      self.front = self.rear = None
    else:
      self.front = self.front.next
    self.size -= 1
    return del_node

  def get_front(self):
    if self.is_empty():
      raise QueueUnderFlowError("Cannot peek front; 'Queue' is empty.")
    return self.front.data

  def get_rear(self):
    if self.is_empty():
      raise QueueUnderFlowError("Cannot peek rear; 'Queue' is empty.")
    return self.rear.data

  def clear(self):
    self.front = self.rear = None
    self.size = 0
  
