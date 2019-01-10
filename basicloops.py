# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:17:20 2019

@author: Aakash Jha
"""
#print fizz,buzz and fizzbuzz according to the problem

for i in range(1,100):
         
    print(i)
    if((i%3==0) and (i%5==0)):
       print("FizzBuzz")
    elif(i%3==0):
       print("Fizz")
    elif(i%5==0):
       print("Buzz")
    
    for j in range(2,i):
        
         if(i%j==0):
          break
    else:
     if(i!=1):   
      print("Prime")
    
    