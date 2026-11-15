class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_nth_node(self, ll, n):
        current=ll.head
        length=0
        while current:
            length += 1
            current = current.next

        if n>length:
            return

        if n==length:
            ll.head = ll.head.next
            return

        current=ll.head
        for _ in range(length-n-1):
            current=current.next
        current.next = current.next.next
        if ll.tail == current.next:
            ll.tail = current
        return ll


if __name__ == "__main__":
    ll=LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll = ll.remove_nth_node(ll,2)

    current = ll.head
    while current:
        print(current.data)
        current = current.next
    