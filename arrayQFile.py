from array import array as arr

class ArrayQ:
    def __init__(self, x=None):
        self.lista=arr('i')
        self.innan=list()

    def enqueue(self, x):
        ##Append lägger till i slutet av lista, insert lägger in på position
        self.lista.append(x)
        self.innan.append(x)
        return self
    
    def dequeue(self):
        ##Skriver ut kortens ordning innan
        print("Ordning på lista innan trick:", self.innan)
        i=0
        Ordning=list()
        while i<len(self.innan):
            ##när index 0="1", index 1="2" etc...                  
            if self.lista[0] == i+1: ## 
             Ordning.append(self.lista[0])
             print("Ta ut", self.lista[0])
             self.lista.pop(0)
             i+=1
            elif self.lista[0]!=i+1:
             print("Kasta bak", self.lista[0])
             ##Om ej, stoppa första elementet längst bak
             self.lista.append(self.lista[0]) 
             ##och kasta ut elementet från index 0
             self.lista.pop(0)   
        else: 
            ##Efter while loop, skriv ut nya ordningen
            print("Ordning efter trick:", Ordning)
        return self

    def isEmpty(self):
        ##Om listan inte har några element
        if len(self.lista)==0:
            print("Kortleken är tom")
        return True