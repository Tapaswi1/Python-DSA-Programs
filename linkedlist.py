#linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class single:
    def __init__(self):
        self.head=None
    def display(self):
            temp=self.head
            if(self.head is None):
                print("Empty")
            else:
                while(temp):
                    print(temp.data)
                    temp=temp.next
n1=node(10)
s1=single()
s1.head=n1
n2=node(20)
n2=n1.next()
n3=node(30)
n3=n2.next()
n4=node(40)
n4=n3.next()
s1.display()
print()
