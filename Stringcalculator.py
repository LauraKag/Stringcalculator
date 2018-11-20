# -*- coding: utf-8 -*-

#%%

#String calculator: Create a function string_calculator that takes
#a string as parameter and sums the digitw it contains. In the input
#string, the numbers should be separated by a comma. Trying to sum
#an empty string should return zero.
#Input examples:

#""
#"4"
#"2,3,4,5,3,2"
#Create tests for this function.

def Stringcalculator(string):
    string=string.replace(" ","")
    if string=="":
        return 0
    else:
        list=string.split(",")
        sum=0
        for i in list:
            sum+=int(i)
    
    return sum

 