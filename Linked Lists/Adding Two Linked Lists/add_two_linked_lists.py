class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ll_to_number(self,ll):
        num=0
        current=ll.head
        while current:
            num = num * 10 + current.data
            current = current.next
        return int(str(num)[::-1])

    def number_to_ll(self,number):
        number=str(number)[::-1]
        ll=LinkedList()
        current=None
        for digit in number:
            node=Node(int(digit))
            if not ll.head:
                ll.head=node
                current=node
            else:
                current.next=node
                current=current.next
        return ll

    def add_two_linked_lists(self,ll1,ll2):
        num1=self.ll_to_number(ll1)
        num2=self.ll_to_number(ll2)
        total=num1+num2
        return self.number_to_ll(total)

if __name__ == "__main__":
    ll1=LinkedList()
    ll1.head=Node(5)
    ll1.head.next=Node(4)

    ll2=LinkedList()
    ll2.head=Node(4)

    result=ll1.add_two_linked_lists(ll1,ll2)
    current=result.head
    while current:
        print(current.data,end="->")
        current=current.next
    print("None")

    print()

    ll1=LinkedList()
    ll1.head=Node(4)
    ll1.head.next=Node(5)
    ll1.head.next.next=Node(6)

    ll2=LinkedList()
    ll2.head=Node(1)
    ll2.head.next=Node(2)
    ll2.head.next.next=Node(3)

    result=ll1.add_two_linked_lists(ll1,ll2)
    current=result.head
    while current:
        print(current.data,end="->")
        current=current.next
    print("None")
