class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_linked_list(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    current = ll.head
    while current:
        print(current.data)
        current = current.next

    print()
    print("Reversed linked list:")
    
    ll.reverse_linked_list()
    current = ll.head
    
    while current:
        print(current.data)
        current = current.next