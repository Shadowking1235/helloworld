# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:13:23 2019

@author: Aakash Jha
"""
#import os.path for checking file existing not working for some reason

'''
Lecture Program


VacationSpots=["India","London","New York","Iceland"]
VacationFile=open("VacationPlaces","w")

for spots in VacationSpots:
    VacationFile.write(spots)
print("done")
VacationFile=open("VacationPlaces","r")
TheWholeFile=VacationFile.read()
print(TheWholeFile)    
VacationFile.close() 

'''
'''
A program to check if the file exist or not and doing the reading and writing accordingly.

import os.path
Name=input("Enter the file Name: ")

while(True):
 if (os.path.isFile(Name)):
    
    File=open("Name","r")
    TheWholeFile=File.read()
    print(TheWholeFile)

 else:
   File=open("Name","w")
   temp=input("Enter a data")
   #if we enter -1 then we come out of the loop
   if(temp==-1):
        break
   File.write(temp)    
   '''
   
Name=input("Enter a file name: ")

while(True):
    #Creates a new file
    File=open(Name,"x")
    temp=input("Enter a line to write in the file: ")
    File.write(temp)
    if(temp == "-1"):
        break
    print("Menu\n1.Read\n2.Delete the file and start over\n3.Append")
    ch=input("Enter your choice 1,2,3: ")
    
    if(ch=="1"):
     File=open(Name,"r")
     TheWholeFile=File.read()
     print(TheWholeFile)
    elif(ch=="2"):
        File=open(Name,"w")
        temp=input("Enter a line to write in the file: ")
        File.write(temp)
        if(temp == "-1"):
         break
    elif(ch=="3"):
        File=open(Name,"a")
        temp=input("Enter a line to write in the file: ")
        File.write(temp)
        if(temp == "-1"):
          break
     