class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class double:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        if(self.head is None):
            print("Empty")
        else:
            while(temp):
                print(temp.data,end="--->")
                temp=temp.next
n1=node(10)
s1=double()
s1.head=n1
n2=node(20)
n1.next=n2
n2.prev=n1
n3=node(30)
n2.next=n3
n3.prev=n2
n4=node(40)
n3.next=n4
n4.prev=n3
s1.display()
