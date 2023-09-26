"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

numbers = [float(value) for value in input().split(",")]
arrLength = len(numbers)
median = (numbers[arrLength//2] + numbers[(arrLength-1)//2])/2
print(median)
 

    
    

