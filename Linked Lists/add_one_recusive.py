class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_one_recursive(self, node):
        if node is None:
            return 1
        carry=self.add_one_recursive(node.next)
        total = node.data + carry
        node.data = total % 10
        return total // 10

    def add_one(self):
        carry = self.add_one_recursive(self.head)
        if carry:
            new_node = Node(carry)
            new_node.next = self.head
            self.head = new_node

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