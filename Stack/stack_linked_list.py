class EmptyStackError(Exception):
  pass
class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.start = None
    self._size = 0

  def is_empty(self):
    return self.start is None

  def push(self, item):
    node = Node(item, self.start)
    self.start = node
    self._size += 1

  def pop(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty cannot pop an item")
    deleted_item = self.start.data
    self.start = self.start.next
    self._size -= 1
    return deleted_item

  def peek(self):
    if self.is_empty():
      raise EmptyStackError("'Stack' is empty")
    return self.start.data

  def size(self):
    return self._size
    
