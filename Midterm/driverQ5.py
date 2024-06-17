import Q5
#Driver Code
list = Q5.SLinkedList()
list.headval = Q5.Node("Mon")
e2 = Q5.Node("Tue")
e3 = Q5.Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")
list.insertAtIndex("Thur", 4)
list.listprint()