class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

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

    def writeTengah(self, index, data):
        size = self.hitungSize()
        newNode = Node(data)
        if (index < 0 or index > size):
            print("index out of bounds")

        elif (index == 0):
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
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode

        elif (index == size):
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

        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            newNode.next = temp
            newNode.prev = temp.prev
            temp.prev.next = newNode
            temp.prev = newNode

    def update(self, index, data):
        newNode = Node(data)
        if (index > self.size):
            print("Double linked list is empty")
            return False
        if (index == 0):
            newNode.next = self.head.next
            self.head = newNode
            self.tail.next = newNode
            self.head.prev = self.tail
            return True
        if (index == (self.size-1)):
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
            return True
        iter = self.head
        for i in range(0, index):
            prev = iter
            iter = iter.next
        prev.next = newNode
        newNode.prev = prev
        newNode.next = iter.next
        iter.next.prev = newNode
        iter = None
        return True

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

    def readSeluruh(self):
        temp = self.head
        if self.head is None:
            print("Circular Double Linked List is empty")

        else:
            while (temp.next is not self.head):
                print(temp.data, end=" ")
                temp = temp.next
            print(temp.data)

    def read(self, index):
        size = self.hitungSize()
        if (self.head is None):
            print("Circular Double Linked List is empty")

        else:
            if (index < 0 or index >= size):
                print("Index out of bounds")

            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                print(temp.data)

    def hitungSize(self):
        temp = self.head
        counter = 0

        if (temp is None):
            return counter

        else:
            while (temp.next is not self.head):
                counter = counter + 1
                temp = temp.next
            counter = counter + 1
            return counter

    def nextChapter(self, index):
        size = self.hitungSize()
        if (index == size):
            return self.head.data
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.next.data

    def prevChapter(self, index):
        if (index == 0):
            return self.tail.data
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.prev.data


choice = 0
choice11 = 0
judulNovel = "laskar pelangi"
llistChapter = CircularDoubleLinkedList()
while (True):
    if choice == 0:
        print("Status")
        print("1. Writer")
        print("2. Reader")
        print("3. Exit")
        choice = int(input("Status: "))
        print()
    if (choice == 1):
        print("Writer Menu:")
        print("1. Write")
        print("2. Update Chapter")
        print("3. Delete")
        print("4. Ganti status")
        print("5. Exit")
        print("6. Write Chapter di tengah")
        choice1 = int(input("Menu Writer: "))
        print()
        if (choice1 == 1):
            print("Write : ")
            print("1. New Chapter")
            print("2. Exit")
            choice11 = int(input("Add (int): "))
            if (choice11 == 1):
                chapter = str(input("Isi Chapter: "))
                llistChapter.write(chapter)
            elif (choice11 == 2):
                choice = 0
                continue
            print()
        elif (choice1 == 2):
            indexUpdate = int(input("Index chapter yang mau diupdate: "))
            chapterUpdate = str(input("Isi Chapter: "))
            llistChapter.update(indexUpdate, chapterUpdate)
        elif (choice1 == 3):
            print("1. Delete buku")
            print("2. Delete chapter")
            choice12 = int(input("Delete buku/ chapter: "))
            if (choice12 == 1):  # kehapus semua chapter
                size = llistChapter.hitungSize()
                while (size != 0):
                    size = size - 1
                    llistChapter.delete(size)
            elif (choice12 == 2):
                indexChapter = int(input("Index chapter yang akan didelete: "))
                llistChapter.delete(indexChapter)
        elif (choice1 == 4):
            choice = 2
        elif (choice1 == 5):
            choice = 0
            continue
        elif (choice1 == 6):
            indexChapter = int(input("Index Chapter: "))
            isiChapter = str(input("Isi chapter: "))
            llistChapter.writeTengah(indexChapter, isiChapter)
        print()
    elif (choice == 2):
        print("Reader Menu:")
        print("1. Read")
        print("2. Ganti status")
        print("3. Exit")
        print("4. Read seluruh")
        choice2 = int(input("Menu Reader: "))
        print()
        if (choice2 == 1):
            print("Judul novel : ", judulNovel)
            print("List Chapter : ")
            indexChapter = int(input("Index Chapter: "))
            llistChapter.read(indexChapter)
            print()
            print("1. Next Chapter")
            print("2. Prev Chapter")
            print("3. Ganti Status")
            print("4. Exit")
            choice21 = int(input("Read(int): "))
            if (choice21 == 1):
                nextChapter = llistChapter.nextChapter(indexChapter)
                print(nextChapter)
            elif (choice21 == 2):
                prevChapter = llistChapter.prevChapter(indexChapter)
                print(prevChapter)
            elif (choice21 == 3):
                choice = 1
            elif (choice21 == 4):
                choice = 0
                continue

        elif (choice2 == 2):
            choice = 1
        elif (choice2 == 3):
            chioce = 0
            continue
        elif (choice2 == 4):
            print("List Chapter : ")
            llistChapter.readSeluruh()
        print()
    elif (choice == 3):
        break
