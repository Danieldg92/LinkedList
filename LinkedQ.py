class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQ:

    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        if self.first is None:
            print("Kön är tom")
            return True
        else:
            return False

    def enqueue(self, x):
        ny_node= Node(x)  # Skapa ny nod med input x
    
        if self.first is None:
            self.first = self.last = ny_node  # first o last pekar på ny nod
            print("Lade till",self.first.value,"överst")
        else:
            self.last.next=ny_node  ##next pekar på ny nod
            self.last=self.last.next ##self.last pekar på ny nod ist för first
            self.last.next=None
            print("Lade till",ny_node.value,"underst")
        return self

        
    def dequeue(self):
        
        x=self.first.value
        self.first=self.first.next      
        return x

    def remove(self, data):
        ##Om first inte existerar finns inget i kö
        if self.first==None:  
            print("Cannot remove from empty queue")
        ##Removes first of three 
        elif self.first.value == data: 
            print("Removed:", self.first.value)
            ##Tar bort om head-data är input
            self.first = self.first.next 
            print("First:", self.first.value)
            print("Second:", self.first.next.value)
    
        ##Om node-data är "data" och det ej är sist i kön - > next inte lika med None
        elif self.first.next.value==data and self.first.next.next is not None:
                print("Removed:", self.first.next.value)
                self.first.next=self.first.next.next
                print(self.first.value)
                print(self.first.next.value)
        ##Om sista nondens data är "data"
        ##tar bort med none
        elif self.last.value==data: 
                print("Removed:", self.last.value)
                self.last=None
                print(self.first.value)
                print(self.first.next.value)
        ##Om inga andra alternativ, finns bara ett kvar: finns inte i kö
        else:
            print("Cannot find",data,"in queue")

