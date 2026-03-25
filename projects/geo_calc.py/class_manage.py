import math
import json

#there are comments throughout just to clarify what a few things do, since I had to learn quite a bit about json files
#had to learn a few more things about class implementation as well!

def choices():
    shape = input("What is the shape that you want to calculate?\nCircle\nRectangle\nSquare\nTriangle\n").lower().strip()
    if shape == "circle":
        print("Alrighty, you chose a circle!")
        try:
            radius = float(input(f"What is the radius of your {shape}?\n"))
            return Calculate_circle(radius)
        except ValueError:
            print("Bruh you can't do that!")
    elif shape == "rectangle":
        print("Alrighty, you chose a rectangle!")
        try:
            length = float(input(f"What is the length of your {shape}?\n"))
            width = float(input(f"What is the width of your {shape}?\n"))
            return Calculate_rectangle(length, width)
        except ValueError:
            print("Bruh you can't do that!")
    elif shape == "square":
        print("Alrighty, you chose a square!")
        try:
            side_length = float(input(f"What is the side length of your {shape}?\n"))
            return Calculate_square(side_length)
        except ValueError:
            print("Bruh you can't do that!")
    elif shape == "triangle":
        print("Alrighty, you chose a triangle!")
        try:
            base = float(input(f"What is the base of your {shape}?\n"))
            height = float(input(f"What is the height of your {shape}?\n"))
            return Calculate_triangle(base, height)
        except ValueError:
            print("Bruh you can't do that!")
    else:
        print("That ain't a shape you can choose!")

class Calculate_circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            return "Bro you can't have a negative radius"
        else:
            return math.pi * (self.radius) ** 2

    def perimeter(self):
        if self.radius < 0:
            return "Bro you can't have a negative radius"
        else:
            return 2 * math.pi * self.radius

class Calculate_rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        if self.length < 0 or self.width < 0:
            return "Bro you can't have negative dimensions"
        else:
            return self.length * self.width
    def perimeter(self):
        if self.length < 0 or self.width < 0:
            return "Bro you can't have negative dimensions"
        else:
            return 2 * (self.length + self.width)

class Calculate_square():
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        if self.side_length < 0:
            return "Bro you can't have a negative side length"
        else:
            return self.side_length ** 2
    def perimeter(self):
        if self.side_length < 0:
            return "Bro you can't have a negative side length"
        else:
            return 4 * self.side_length

class Calculate_triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        if self.base < 0 or self.height < 0:
            return "Bro you can't have negative dimensions"
        else:
            return 0.5 * self.base * self.height
    def perimeter(self):
        if self.base < 0 or self.height < 0:
            return "Bro you can't have negative dimensions"
        else:
            #adds the three sides of the triangle together to form the perimeter
            return self.base + self.height + math.hypot(self.base, self.height)
        
def save_shapes(obj):
    #checks if the object is a dictionary
    if isinstance(obj, dict):
        shape_data = obj
    else:
        if isinstance(obj, Calculate_circle):
            shape = "circle"
            dims = {"radius": obj.radius}
        elif isinstance(obj, Calculate_rectangle):
            shape = "rectangle"
            dims = {"length": obj.length, "width": obj.width}
        elif isinstance(obj, Calculate_square):
            shape = "square"
            dims = {"side_length": obj.side_length}
        elif isinstance(obj, Calculate_triangle):
            shape = "triangle"
            dims = {"base": obj.base, "height": obj.height}
        else:
            #saves object as an organized lowercase string
            shape = obj.__class__.__name__.lower()
            dims = {}

        area = obj.area()
        perimeter = obj.perimeter()

        shape_data = {"shape": shape}
        shape_data.update(dims)
        shape_data["area"] = area
        shape_data["perimeter"] = perimeter

    try:
        with open("calculations.json", "r") as f:
            calculations = json.load(f)
            if not isinstance(calculations, list):
                calculations = []
        #below is a json built in error that prevents the file from being read if it is not valid json
    except (FileNotFoundError, json.JSONDecodeError):
        calculations = []

    calculations.append(shape_data)
    with open("calculations.json", "w") as f:
        json.dump(calculations, f, indent=2)

    return shape_data

def view_shapes_made():
    try:
        with open("calculations.json", "r") as f:
            calculations = json.load(f)
            if not calculations:
                print("No calculations found.")
                return
            for c in calculations:
                print(c)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No calculations found.")

def select_specific_shape():
    shape_choice = input("Which shape do you want to select in your shapes?\nCircle\nRectangle\nSquare\nTriangle\n").lower().strip()
    try:
        with open("calculations.json", "r") as f:
            calculations = json.load(f)
            found = False
            for shape_data in calculations:
                if shape_data.get("shape") == shape_choice:
                    found = True
                    print(f"Shape: {shape_data.get('shape')}")
                    print(f"Area: {shape_data.get('area')}")
                    print(f"Perimeter: {shape_data.get('perimeter')}")
                    print("-" * 20)
            if not found:
                print("That ain't a shape you have!")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No calculations found.")

def compare_shape_data():
    shape_choice = input("Which shape's data do you want to compare?\nCircle\nRectangle\nSquare\nTriangle\n").lower().strip()
    second_choice = input("Which shape's data do you want to compare that shape with?\nCircle\nRectangle\nSquare\nTriangle\n").lower().strip()
    try:
        with open("calculations.json", "r") as f:
            calculations = json.load(f)
            shape_data = None
            second_shape_data = None
            for data in calculations:
                if not shape_data and data.get("shape") == shape_choice:
                    shape_data = data
                if not second_shape_data and data.get("shape") == second_choice:
                    second_shape_data = data
            if shape_data and second_shape_data:
                print(f"Comparing {shape_choice} and {second_choice}:")
                print(f"Area: {shape_data.get('area')} vs {second_shape_data.get('area')}")
                print(f"Perimeter: {shape_data.get('perimeter')} vs {second_shape_data.get('perimeter')}")
            else:
                print("One or both shapes not found.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No calculations found.")

def sort_shapes():
    print("Alrighty, sorting in smallest to biggest area!")
    try:
        with open("calculations.json", "r") as f:
            calculations = json.load(f)
            shapes = []
            for shape_data in calculations:
                area = shape_data.get("area")
                if isinstance(area, (int, float)):
                    shapes.append(shape_data)
            #sorts the shapes by area starting from lowest area to biggest
            shapes.sort(key=lambda x: x.get("area", 0))
            for shape in shapes:
                print(f"Shape: {shape.get('shape')}")
                print(f"Area: {shape.get('area')}")
                print(f"Perimeter: {shape.get('perimeter')}")
                print("-" * 20)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No shapes found.")

def show_shape_formulas():
    print("Here are the formulas for the shapes:")
    print("Circle: Area = πr², Perimeter = 2πr")
    print("Rectangle: Area = l * w, Perimeter = 2(length + width)")
    print("Square: Area = sides², Perimeter = 4 * sides")
    print("Triangle: Area = ½base * height, Perimeter = a + b + c")

#simply checks if it is ran in main!
if __name__ == "__main__":
    obj = choices()
    if obj:
        saved = save_shapes(obj)
        print("Saved:", saved)