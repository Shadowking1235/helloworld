# -*- coding: utf-8 -*-
"""
Created on Wed Jan 09 20:30:09 2019

@author: Aakash Jha
"""
#Creating an empty list
myUnqiueList=[]
myLeftOvers=[]
print(myUnqiueList)

#Function to add an element if it does't exist
def add(x):
    if x in myUnqiueList:
     return False
    else:
        myUnqiueList.append(x)
        return True

#Push to put the rejected inputs in another array
def push(x):
    if x in myUnqiueList:
        myLeftOvers.append(x)
    else:
        add(x)
    
#adding various elements in the array and testing the program
push(1)
push(2)
push(3)
push(4)
push("Hello") 
push(2)
push(3)
push("Hello")
push(6.3)
print(myUnqiueList) 
print(myLeftOvers)  
        