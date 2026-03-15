class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self, front=None, back=None):
        self.front = None
        self.back = None
        self.size = 0


    def show(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    def get_front(self):
        return self.front


    def get_back(self):
        return self.back


    def insert_front(self, data):

        new_node = Node(data)

        if self.front is None:
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

        self.size += 1


    def insert_back(self, data):

        new_node = Node(data)

        if self.back is None:
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node

        self.size += 1


    def insert(self, data):

        new_node = Node(data)

        if self.front is None:
            self.front = self.back = new_node
            self.size += 1
            return

        current = self.front

        while current and current.data < data:
            current = current.next

        if current == self.front:
            self.insert_front(data)
            return

        if current is None:
            self.insert_back(data)
            return

        prev_node = current.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = current
        current.prev = new_node

        self.size += 1


    def remove(self, data):

        current = self.front

        while current:

            if current.data == data:

                if current.prev:
                    current.prev.next = current.next
                else:
                    self.front = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.back = current.prev

                self.size -= 1
                return True

            current = current.next

        return False


    def is_present(self, data):

        current = self.front

        while current:
            if current.data == data:
                return True
            current = current.next

        return False


    def __len__(self):
        return self.size


        

        

if __name__ == "__main__":

    lst = LinkedList()

    lst.insert(5)
    lst.insert(2)
    lst.insert(8)
    lst.insert(4)

    lst.show()

    print(lst.is_present(4))
    print(lst.is_present(10))

    lst.remove(4)

    lst.show()

    print(len(lst))