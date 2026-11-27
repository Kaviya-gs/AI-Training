
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = newnode

    def delete(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head = self.head.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


l = LinkedList()

l.insert(10)
l.insert(20)
l.insert(30)

l.display()

l.delete()

l.display()
