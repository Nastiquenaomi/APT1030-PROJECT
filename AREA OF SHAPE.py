def pi():
    return 3.142

def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = pi() * radius ** 2
    return area

def square():
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    return area

def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    return area

def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    return area

def calculate_area():
    print("Choose a shape - Circle, Square, Rectangle, or Triangle: ")
    shape = input().lower()
    area = None  # Initialize area

    if shape == "circle":
        area = circle()
        
    elif shape == "square":
        area = square()
        
    elif shape == "rectangle":
        area = rectangle()
        
    elif shape == "triangle":
        area = triangle()

    else:
        print("Invalid shape")
        return

    print(f"The area of the {shape} is: {area}")

#call the function to run the program
calculate_area()

