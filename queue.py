class Node: #Doubly linked list.
    def __init__(self, val=0, next=None, back=None):
        self.val = val
        self.next = next
        self.back = back
        
class Queue:
    def __init__(self, contents, first=None, last=None):
        if type(contents) == list:
            if len(contents) > 0:
                head = Node(contents[0])
                l = head
                for i in range(1,len(contents)):
                    x = Node(contents[i])
                    x.val = contents[i]
                    x.back = l
                    l.next = x
                    l = x
                    if i == len(contents)-1:
                        self.last = x
                self.first = head
                return
            raise Exception("Length of contents must be larger than 0!")
        raise TypeError("Contents must be a List")
    
    def enqueue(self, v):
        if self.first:
            k = Node(v,self.first)
            self.first = k
    
    def dequeue(self):
        if self.last:
            k = self.last.back
            b = self.last
            self.last = k
            b.back = None
            k.next = None
            
    def list_items(self):
        if self.first and self.last:
            k = self.first
            while k:
                print(k.val)
                k = k.next
                
    def find(self, val):
        if self.first and self.last:
            k = self.first
            while k:
                if k.val == val:
                    return k
                k = k.next
            return None
