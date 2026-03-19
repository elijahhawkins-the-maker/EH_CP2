import math
import json

def inputs():
    shape = input("What is the shape that you want to calculate?\n").lower()
    if shape == "circle":
        radius = float(input(f"What is the radius of your {shape}\n"))
    elif shape == "rectangle":
        length = int()

class Shapes():
    
    def __init__(self):
        self.calculations = 0

    def calculate_circle(radius):
        if radius < 0:
            return "Bro you can't have a negative radius"
        else:
            return math.pi * (radius) ** 2
    
    def calculate_rectangle():