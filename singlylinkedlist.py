class Node:

    def _init_(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def _init_(self):
        self.head = None

    def create(self, values):
       
        for value in values:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            else:
                current = self.head

                while current.next is not None:
                    current = current.next

            
                current.next = new_node

    def traverse(self):
        
        current = self.head

        if current is None:
            print("Linked list is empty")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
