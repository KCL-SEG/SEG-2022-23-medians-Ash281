"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import numpy

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median = numpy.median(numbers)
        print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

    
    

