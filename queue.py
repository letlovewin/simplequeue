class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Queue:
    def __init__(self, contents, h=None):
        if len(contents) > 0:
            head = Node(contents[0])
            l = head
            for i in range(1,len(contents)):
                x = Node(contents[i])
                x.val = contents[i]
                l.next = x
                l = x
            self.h = head
    
    def enqueue(v):
        if h:
            l = h
            while h.
