class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # assign last to newNode
        self.last = newNode

        # create link to iteself
        self.last.next = self.last
        return self.last

    def addFront(self, data):

        # check if the list is empty
        if self.last == None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # store the address of the current first node in the newNode
        newNode.next = self.last.next

        # make newNode as last
        self.last.next = newNode

        return self.last
    
    def addEnd(self, data):
        # check if the node is empty
        if self.last == None:
            return self.addToEmpty(data)

        # allocate memory to the new node and add data to the node
        newNode = Node(data)

        # store the address of the last node to next of newNode
        newNode.next = self.last.next

        # point the current last node to the newNode
        self.last.next = newNode

        # make newNode as the last node
        self.last = newNode

        return self.last