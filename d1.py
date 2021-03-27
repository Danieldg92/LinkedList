from array import array
from arrayQFile import ArrayQ
from LinkedQ import LinkedQ
import math

lista=[7,1,12,2,8,3,11,4,9,5,13,6,10]
if __name__=="__main__":
    q = LinkedQ() 
    
    for item in lista:
        q.enqueue(item)

    q.isEmpty()

    print("\n---------------\n")

    counter = 1

    while q.isEmpty() is False:              
        x = q.dequeue()
        if x == counter:
            print ("Plockade ut:", counter)
            counter+=1

        else:
            q.enqueue(x)

  