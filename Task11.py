class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))
          
      #IMPORTANT BIT HERE
      def delete(self,node_value):
            
            current_node = self.head
            while current_node is not None:#Checks if the node exists
              if current_node.value == node_value:
                if current_node.prev is not None:
                  try:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                  except AttributeError:#Hits the end of the lists produces attriute error
                    pass
                else:
                  self.head = current_node.next
                  current_node.next.prev = None
              current_node = current_node.next
            

                  
         
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))#Insert adds a new node to the list
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.display()
      l.delete(6)#This line calls for node 6 to be removed
      l.display()
      
