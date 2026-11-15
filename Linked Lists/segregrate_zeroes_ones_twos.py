class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def segregate(self, ll):
        zeroes = Node(0)
        ones = Node(0)
        twos = Node(0)

        zero_tail = zeroes
        ones_tail = ones
        twos_tail = twos

        current = ll.head
        while current:
            next_node = current.next
            current.next = None
            if current.data == 0:
                zero_tail.next = current
                zero_tail = zero_tail.next
            elif current.data == 1:
                ones_tail.next = current
                ones_tail = ones_tail.next
            else:
                twos_tail.next = current
                twos_tail = twos_tail.next
            current = next_node

        zero_tail.next = ones.next
        ones_tail.next = twos.next
        ll.head = zeroes.next
        ll.tail = (
            twos_tail
            if twos_tail != twos
            else (ones_tail if ones_tail != ones else zero_tail)
        )


if __name__ == "__main__":
    ll = LinkedList()
    for value in [2, 1, 0, 2, 1, 0]:
        node = Node(value)
        if ll.head is None:
            ll.head = node
        else:
            ll.tail.next = node
        ll.tail = node

    ll.segregate(ll)
    # Print the segregated linked list
    current = ll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
