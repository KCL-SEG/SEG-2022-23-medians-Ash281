"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

numbers = [float(value) for value in input().split(",")]
arrLength = len(numbers)
if arrLength % 2 == 0:
     median = (numbers[arrLength//2] + numbers[(arrLength-1)//2]) / 2
else:
    median = numbers[arrLength//2]
print(median)
 

    
    

