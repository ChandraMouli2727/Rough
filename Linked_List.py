class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("LL is Empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
            
        print(llstr)
        
    def insert_at_end(self,data):
      if self.head is None:
          self.head = Node(data,None)
          return
      
      itr = self.head
      while itr.next:
          itr = itr.next
      
      itr.next = Node(data,None)
      
    def insert_Values(self,data_list):
        self.head = None
        for d in data_list:
            self.insert_at_end(d)
        
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid")
            
        if index == 0:
            self.head = self.head.next
            return
        
        cc = 0
        itr = self.head
        while itr:
            if cc == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            cc += 1
    
    
    def insert_at(self,index,data):
        if index<0 or index >= self.get_length():
            raise Exception("Invalid")
            
        if index == 0:
            self.insert_at_begin(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count +=1
        
        
l1 = LL()
l1.insert_at_begin(2)
l1.insert_at_begin(33)
l1.print()
l1.insert_at_end(4)
l1.print()
l2 = LL()
l2.insert_Values(["A","B","C","D","E"])
l2.print()
print(l2.get_length())
l3 = LL()
l3.insert_Values(["A","B","C","D","E"])
l3.remove_at(1)
l3.print()
l4 = LL()
l4.insert_Values(["A","B","D","E"])
l4.print()
l4.insert_at(2,"C")
l4.print()
