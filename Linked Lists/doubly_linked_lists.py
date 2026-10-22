import random


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data, end="<->")
            current=current.next
        print("None")

    def delete_head_node(self):
        if self.head is None:
            return
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        else:
            self.tail = None

    def delete_tail_node(self):
        if self.tail is None:
            return
        self.tail=self.tail.prev
        if self.tail:
            self.tail.next=None
        else:
            self.head=None

    def delete_kth_node(self,k):
        if k<=0:
            return
        current=self.head
        count=1
        while current and count<k:
            current=current.next
            count+=1
        if current is None:
            return
        if current.prev:
            current.prev.next=current.next
        if current.next:
            current.next.prev=current.prev
        if current==self.head:
            self.head=current.next
        if current==self.tail:
            self.tail=current.prev

    def insert_kth_node(self, k, data):
        if k<0:
            return
        if k==0:
            new_node=Node(data)
            if self.head:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            else:
                self.head=new_node
                self.tail=new_node
        else:
            current=self.head
            count=1
            while current and count<k:
                current=current.next
                count+=1
            if current is None:
                return
            new_node=Node(data)
            new_node.next=current.next
            new_node.prev=current
            if current.next:
                current.next.prev=new_node
            current.next=new_node
            if new_node.next is None:
                self.tail=new_node

    def insert_before_tail(self, data):
        if self.tail is None:
            return
        new_node=Node(data)
        previous=self.tail.prev
        new_node.next=self.tail
        new_node.prev=previous
        if previous:
            previous.next=new_node
        self.tail.prev=new_node
        if self.tail == self.head:
            self.head = new_node


if __name__ == "__main__":
    dll=DoublyLinkedList()
    for _ in range(random.randint(1,10)):
        dll.append(random.randint(1, 100))
    dll.display()

    dll.delete_head_node()
    dll.display()

    dll.insert_kth_node(2, 50)
    dll.display()
    
    dll.delete_tail_node()
    dll.display()

    dll.delete_kth_node(3)
    dll.display()

    dll.insert_before_tail(75)
    dll.display()