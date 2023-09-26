"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        arrLength = len(numbers)
        median = (numbers[arrLength//2] + numbers[(arrLength-1)//2])/2
        print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

    
    

