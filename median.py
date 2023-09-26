"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

numbers = [float(value) for value in input().split(",")]
arrLength = len(numbers)
if (arrLength % 2 == 1):
    median = numbers[(arrLength-1)/2]
    print(median)

else:
    median = numbers[arrLength/2] + numbers[(arrLength-2)/2] 
    print(median)


 

    
    

