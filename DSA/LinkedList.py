class Node:
    #constructor to initialise the node
    def __init__(self, v = None):
        self.value = v
        self.next = None

class LinkedList(Node):
    #constructor to initialise a Linked List i.e head node is NULL
    def __init__(self):
        self.head = None
        
    #method/function to check if the linked list is empty or not
    def isEmpty(self):
        if (self.head == None):
            return True
        return False

    #method to add a node at the end of the list
    def append(self, v):
        if self.isEmpty():
            self.head = Node(v)
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = Node(v)
        return

    #method to insert a node at the front of the list
    def addFront(self, v):
        new_node = Node(v)
        new_node.next = self.head
        self.head = new_node
        return

    #method to delete a node with a given value v
    def delete(self, v):
        if self.isEmpty():
            return
        temp = self.head
        if temp.value == v:
            self.head = temp.next
            temp = None
            return
        else:
            while temp.next != None:
                if temp.value == v:
                    break
                temp = temp.next
            if temp.next == None:
                return
            temp.value = None
            if temp.next != None:
                temp.value = temp.next.value
                temp.next = temp.next.next

    #method to add a node at a specified position
    def addNode(self, v, pos):
        if pos == 1:
            addFront(v)
            return
        new_node = Node(v)
        temp = self.head
        i = 1
        while (temp != None) and (i < pos-1):
            temp = temp.next
            i += 1
        if temp == None:
            return
        new_node.next = temp.next
        temp.next = new_node
        
    #method to display the linked list
    def display(self):
        temp = self.head
        if self.isEmpty():
            print("List is Empty")
            return
        while (temp.next != None):
            print(temp.value, end = " -> ")
            temp = temp.next
        print(temp.value)
                
n = LinkedList()
n.addFront(5)
n.addFront(7)
n.addFront(3)
n.append(6)
print("Linked List is : ")
n.display()
n.delete(7)
print("\nLinked List after deleting Node with value 7 : ")
n.display()
n.addNode(10,2)
print("\nLinked List after adding a Node with value 10 at position 2 : ")
n.display()
