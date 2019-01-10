# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:05:57 2019

@author: Aakash Jha
"""
#attributes of a song with dictionary
dictionary={}

dictionary["Genre"]="Pop"
dictionary["Artist"]="Shawn Mendes"
dictionary["Year"]=2017

print(dictionary)

def fun(key,value):
    if key in dictionary:
        if(dictionary[key]==value):
            print("Correct guess")
            return True
        else:
         print("Incorrect guess")
         return False
    else:
         print("Incorrect guess")
         return False
         
    
    
fun("Genre","Pop")
fun("Artist","Justin")  
fun("Artist","Shawn Mendes")  
    