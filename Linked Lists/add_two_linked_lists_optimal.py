class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_two_linked_lists(self,l1,l2):
        dummy=Node(0)
        current=dummy
        carry=0
        while l1 or l2 or carry:
            val=l1.data if l1 else 0
            val+=l2.data if l2 else 0
            val+=carry
            carry=val//10
            current.next=Node(val%10)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next

if __name__=="__main__":
    l1=LinkedList()
    l1.head=Node(2)
    l1.head.next=Node(4)
    l1.head.next.next=Node(3)

    l2=LinkedList()
    l2.head=Node(5)
    l2.head.next=Node(6)
    l2.head.next.next=Node(4)

    result=l1.add_two_linked_lists(l1.head,l2.head)
    while result:
        print(result.data,end=" ")
        result=result.next