class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def arraya_to_linked_list(self, arr):
        if not arr:
            return
        if len(arr) == 0:
            return
        self.head=Node(arr[0])
        current=self.head
        for item in arr[1:]:
            new_node = Node(item)
            current.next = new_node
            new_node.prev = current
            current = current.next

    def display(self):
        current=self.head
        while current:
            print(current.data, end="<->")
            current=current.next
        print("None")

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ll = LinkedList()
    ll.arraya_to_linked_list(arr)
    ll.display()