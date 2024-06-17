#This is Q5 code
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insertAtIndex(self, data, index):
        if index == 0 or self.headval is None:
            self.AtBegining(data)
            return

        new_node = Node(data)
        temp = self.headval
        count = 0

        while temp is not None:
            if count == index - 1:
                new_node.nextval = temp.nextval
                temp.nextval = new_node
                return
            temp = temp.nextval
            count += 1

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
