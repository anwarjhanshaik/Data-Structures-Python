class Stack:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return self.items == []

  def push(self, data):
    self.items.append(data)

  def pop(self):
    if self.is_empty():
      raise IndexError("Stack is empty")
    return self.items.pop()

  def peek(self):
    if self.is_empty():
      raise IndexError("Stack is empty")
    return self.items[-1]

  def size(self):
    return len(self.items)
    
