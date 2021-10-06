#class to initialise a Node
class Node:
    #Constructor
    def __init__(self, v):
        self.data = v
        self.next = None

#class for Singly Linked List
class SinglyLinkedList():
    #constructor to initialise head and tail of a Singly Linked List. Iniltially set to None
    def __init__(self):
        self.head = self.tail = None

    #method to check if the List is empty
    def isEmpty(self):
        if (self.head == self.tail == None):
            return True
        return False

    #method to count thee no. of nodes in the list
    def count(self):
        if self.isEmpty():
            return 0
        n = 0
        temp = self.head
        while (temp != None):
            n += 1
            temp = temp.next
        return n

    #method to add an element in the front i.e. head
    def addFront(self, x):
        new_node = Node(x)
        if (self.isEmpty()):
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    #method to add element in the last i.e. tail
    def addTail(self, x):
        new_node = Node(x)
        if (self.isEmpty()):
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    #method to insert an element at a specific position
    def insert(self, x, pos):
        if pos == 1:
            self.addFront(x)
            return
        if pos == (self.count()+1):
            self.addTail(x)
            return
        new_node = Node(x)
        temp = self.head
        i = 1
        while (temp != None) and (i < pos-1):
            temp = temp.next
            i += 1
        if (temp == None):
            return
        new_node.next = temp.next
        temp.next = new_node

    #method to remove the head in the list
    def removeHead(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.next
        temp = None

    #method to remove the tail
    def removeTail(self):
        if self.isEmpty():
            return
        temp = self.head
        while (temp != None) and (temp.next != self.tail):
            temp = temp.next
        self.tail = temp
        self.tail.next = None
        temp = None

    #method to delete a specific element
    def delete(self, v):
        if self.isEmpty():
            return
        temp = self.head
        if temp.data == v:
            self.head = temp.next
            temp = None
            return
        else:
            while temp.next != None:
                if temp.data == v:
                    break
                temp = temp.next
            if temp.next == None:
                return
            temp.data = None
            if temp.next != None:
                temp.data = temp.next.data
                temp.next = temp.next.next

    #meethod to display the nodes of the list
    def display(self):
        temp = self.head
        if self.isEmpty():
            print("List is Empty")
            return
        print("head -> ", end = " ")
        while (temp.next != None):
            print(temp.data, end = " -> ")
            temp = temp.next
        print(temp.data, " <- tail")

n = SinglyLinkedList()
n.addFront(3)
n.addFront(10)
n.addFront(46)
n.addTail(678)
n.addTail(23)
n.addFront(2)
n.insert(80,3)
print("Singly Linked List is : ")
n.display()
n.insert(34,5)
print("\nSingly Linked List after adding a Node with value 34 at position 5 : ")
n.display()
n.removeHead()
print("\nSingly LinkedList after removing the head : ")
n.display()
n.removeTail()
print("\nSingly Linked List after removing the tail : ")
n.display()
n.delete(34)
print("\nSingly Linked List after deleting Node with value 34 : ")
n.display()


        
        
        
        
