import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current=self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def search_an_element(self,key):
        current=self.head
        position=0
        while current:
            if current.data== key:
                print(f"Element {key} found at position {position}")
                return
            current=current.next
            position+=1
        print(f"Element {key} not found")

    def length(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count

    def delete_an_element(self,key):
        current=self.head
        prev=None
        if key==self.head.data:
            self.head=self.head.next
            return
        while current:
            if current.data==key:
                prev.next=current.next
                return
            prev=current
            current=current.next
        print(f"Element {key} not found")

    def insert_at_position(self, data, position):
        new_node=Node(data)
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        count=0
        while current and count<position-1:
            current=current.next
            count+=1
            if current is None:
                print(f"Position {position} out of bounds")
                return
        new_node.next=current.next
        current.next=new_node

    def insert_before_value(self, data, value):
        new_node=Node(data)
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        while current.next and current.next.data != value:
            current=current.next
        if current.next is None:
            print(f"Value {value} not found")
            return
        new_node.next=current.next
        current.next=new_node
        


if __name__ == "__main__":
    ll=LinkedList()
    for _ in range(random.randint(0,25)):
        ll.append(random.randint(1, 100))
    ll.print_list()
    
    print(f"Length of the linked list: {ll.length()}")
    
    key=int(input("Enter the element to search: "))
    ll.search_an_element(key)
    
    delete_key=int(input("Enter the element to delete: "))
    ll.delete_an_element(delete_key)
    ll.print_list()

    insert_data=int(input("Enter an element to insert: "))
    insert_position=int(input("Enter the position to insert the element at: "))
    ll.insert_at_position(insert_data, insert_position)
    ll.print_list()

    insert_before_data=int(input("Enter an element to insert before a value: "))
    insert_before_value=int(input("Enter the value to insert the element before: "))
    ll.insert_before_value(insert_before_data, insert_before_value)
    ll.print_list()



