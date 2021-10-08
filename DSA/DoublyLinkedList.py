#class to create Node
class Node:
    def __init__(self, v = None):
        self.data = v
        self.next = self.prev = None

#class to create the Doubly Linked List
class DoublyLinkedList:

    #constructor to initialise the doubly linked list, head and tail initialised to 'None'
    def __init__(self):
        self.head = self.tail = None

    #method to check if the doubly linked list is empty or not
    def isEmpty(self):
        if self.head == self.tail == None:
            return True
        return False

    #method to add an element in front the list i.e. head
    def addFront(self, x):
        new_node = Node(x)
        if (self.isEmpty()):
            self.head = self.tail = new_node
            new_node.prev = None
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    #method to add an element in the last of the list i.e. tail
    def addTail(self, x):
        new_node = Node(x)
        if (self.isEmpty()):
            self.head = self.tail = new_node
            new_node.next = None
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = None
        self.tail = new_node

    #method to insert an element at a specific position
    def insert(self, x, pos):
        new_node = Node(x)
        temp = self.head
        i = 1
        while i < pos-1:
            temp = temp.next
            i += 1
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node

    #method to remove the element at head
    def removeHead(self):
        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        temp = None

    #method to remove element at tail
    def removeTail(self):
        temp = self.tail
        self.tail = temp.prev
        temp.prev.next = None
        temp = None

    #method to remove element at a specific position
    def remove(self, pos):
        temp = self.head
        i = 1
        while i < pos:
            temp = temp.next
            i += 1
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp = None

    #method to display the doubly linked list
    def display(self):
        temp = self.head
        if self.isEmpty():
            print("List is Empty")
            return
        print("head -> ", end = " ")
        while (temp.next != None):
            print(temp.data, end = " < -- > ")
            temp = temp.next
        print(temp.data, " <- tail")

n = DoublyLinkedList()
n.addFront(23)
n.addTail(2)
n.addFront(78)
n.addFront(45)
n.addTail(90)
n.addTail(37)
n.addTail(900)
print("Doubly Linked List is : ")
n.display()
n.insert(34,5)
print("\nDoubly Linked List after adding a Node with value 34 at position 5 : ")
n.display()
n.removeHead()
print("\nDoubly LinkedList after removing the head : ")
n.display()
n.removeTail()
print("\nDoubly Linked List after removing the tail : ")
n.display()
n.remove(4)
print("\nDoubly Linked List after deleting Node at position 4 : ")
n.display()
