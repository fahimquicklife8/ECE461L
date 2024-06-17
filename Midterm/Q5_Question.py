class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   
   def __init__(self):
      self.headval = None
   
   def AtBegining(self, newdata):
      new_node = Node(newdata)
      new_node.nextval = self.headval
      self.headval = new_node
   
   def listprint(self):
      n = self.headval
      while n is not None:
         print(n.dataval)
         n = n.nextval

   # Insert at a particular index, Indexing starts from 0.
   # Enter your code here

   
