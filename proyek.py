class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def write(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.tail
            self.head.prev = self.tail
            self.tail.next = self.head
            self.tail.prev = self.head

        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.tail.next = newNode
            self.head.prev = newNode
            self.tail = newNode

    def update(self, index, data):
        size = self.hitungSize()
        if (self.head is None):
            print("There is no chapter available")

        else:
            if (index < 0 or index >= size):
                print("Index out of bounds")

            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                temp.data = data

    def delete(self, index):
        size = self.hitungSize()
        if (index < 0 or index >= size):
            print("index out of bounds")

        elif (index == 0):
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail

        elif (index == size - 1):
            self.tail = self.tail.prev
            self.head.prev = self.tail
            self.tail.next = self.head

        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

# write di tengah blm
    def readSeluruh(self):
        temp = self.head
        print("List dari depan : ")
        if self.head is None:
            print("There is no chapter available")

        else:
            while (temp.next is not self.head):
                print(temp.data, end=" ")
                temp = temp.next
            print(temp.data)

    def read(self, index):
        size = self.hitungSize()
        if (self.head is None):
            print("There is no chapter available")

        else:
            if (index < 0 or index >= size):
                print("Index out of bounds")

            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                return temp.data
            
    def prev(self, iter):
        iter = iter.prev
        print(iter.data)
        return None
    
    def next(self, iter):
        iter = iter.next
        print(iter.data)
        return None
        


choice = 0
llist = CircularDoubleLinkedList()
while (choice != 5):
    print("Status")
    print("1. Writer")
    print("2. Reader")
    print("3. Exit")
    choice = int(input("Status: "))
    if (choice == 1):
        print("Writer Menu:")
        print("1. Write")
        print("2. Update Chapter")
        print("3. Delete")
        print("4. Ganti status")
        print("5. Exit")
        print("6. Write di tengah")
        choice1 = int(input("Menu Writer: "))
        if (choice1 == 1):
            llist.write()
        elif (choice1 == 2):
            llist.update()
        elif (choice1 == 3):
            llist.delete()
        elif (choice1 == 4):
            choice = 2
        elif (choice1 == 5):
            break
        elif (choice1 == 6):
            # llist.writeTengah()
            llist.delete()

    elif (choice == 2):
        print("Reader Menu:")
        print("1. Read")
        print("2. Ganti status")
        print("3. Exit")
        print("4. Read seluruh")
        choice2 = int(input("Menu Reader: "))
        if (choice2 == 1):
            llist.read()

        elif (choice2 == 2):
            choice = 1
        elif (choice2 == 3):
            break
        elif (choice2 == 4):
            llist.readSeluruh()

    elif (choice == 3):
        break
