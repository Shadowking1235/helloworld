# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:03:13 2019

@author: Aakash Jha
"""

#Importing pyplot and re naming it to plt for easier use of it.
from matplotlib import pyplot as plt
#Creating a population versus year graph using matplotlib
year=[1950,1970,1990,2010]
pop=[2.519,3.692,5.263,6.9720] #population
#this is for continous graph
plt.plot(year,pop)
plt.title('My first Graph')
plt.ylabel('Population')
plt.xlabel('Year')
plt.show()

#for scattered plo,we use:
plt.scatter(year,pop)
plt.title('My Second Graph')
plt.ylabel('Population')
plt.xlabel('Year')
plt.show()

#To change the scale of x axis to logarithmic
plt.xscale('log')
plt.scatter(year,pop)
plt.title('My Third Graph')
plt.ylabel('Population')
plt.xlabel('Year')
plt.show()


#Now we create histograms with matplotlib
values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
'''
Values are the random data which we have input
hist is a built in function to produce histogram
bins represent the no. of divisions on the histogram scale between starting
and ending values of values. color sets the color of the plot
''' 
plt.hist(values,bins=3,color='g')
plt.show()

