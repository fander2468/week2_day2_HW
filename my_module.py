# Module should have the following capabilities:
# 1) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area
# 2) Has a function to calculate the circumference of a circle
# Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses # square footage

def square(lenght, width):
    area = lenght * width
    return area

def circle_circumference(radius):
    circumference = 3.14 * radius * 2
    return circumference
