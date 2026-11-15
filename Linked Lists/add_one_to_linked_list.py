class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def linked_list_to_number(self):
        num=0
        current=self.head
        while current:
            num = num * 10 + current.data
            current = current.next
        return num

    def add_one(self):
        num = self.linked_list_to_number()
        num += 1
        self.head = None
        for digit in str(num):
            new_node = Node(int(digit))
            if not self.head:
                self.head = new_node
                current = self.head
            else:
                current.next = new_node
                current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(9)
    ll.head.next = Node(9)
    ll.head.next.next = Node(9)
    current = ll.head
    while current:
        print(current.data)
        current = current.next

    print()
    print("Linked list after adding one:")
    ll.add_one()
    current = ll.head
    while current:
        print(current.data)
        current = current.next
