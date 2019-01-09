# -*- coding: utf-8 -*-
"""
Created on Tue Jan 08 23:14:52 2019

@author: Aakash Jha
"""
#Creating different variables
One = 1
Two = 2
Three = "3"
integer=int(Three)
Four = 2
check=True
def fun(x,y,z):
    if(x==y or x==z or y==z):
      check=True
    else:
        check=False
    print(check)
    
    
fun(One,Two,Three) 
fun(One,Two,Four)  

    
    
