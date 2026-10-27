class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def split_odd_even(self, ll):
        if ll.head is None:
            return ll
        odd = LinkedList()
        even = LinkedList()
        current = ll.head

        while current:
            next_node = current.next
            current.next = None
            if current.data % 2 == 0:
                if even.head is None:
                    even.head = current
                else:
                    temp = even.head
                    while temp.next:
                        temp = temp.next
                    temp.next = current
            else:
                if odd.head is None:
                    odd.head = current
                else:
                    temp = odd.head
                    while temp.next:
                        temp = temp.next
                    temp.next = current
            current = next_node

        if odd.head is None:
            ll.head = even.head
        else:
            ll.head = odd.head
            temp = odd.head
            while temp.next:
                temp = temp.next
            temp.next = even.head
        return ll
        

if __name__ == "__main__":
    ll=LinkedList()
    ll.head=Node(1)
    ll.head.next=Node(2)
    ll.head.next.next=Node(3)
    ll.head.next.next.next=Node(4)
    ll.head.next.next.next.next=Node(5)

    ll=ll.split_odd_even(ll)
    current = ll.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")