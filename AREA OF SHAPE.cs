using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Choose a shape to calculate its area:");
        Console.WriteLine("1. Circle");
        Console.WriteLine("2. Rectangle");
        Console.WriteLine("3. Triangle");
        
        int choice = int.Parse(Console.ReadLine());
        
        switch (choice)
        {
            case 1:
                CalculateCircleArea();
                break;
            case 2:
                CalculateRectangleArea();
                break;
            case 3:
                CalculateTriangleArea();
                break;
            default:
                Console.WriteLine("Invalid choice. Please choose 1, 2, or 3.");
                break;
        }
    }

    static void CalculateCircleArea()
    {
        Console.Write("Enter the radius of the circle: ");
        double radius = double.Parse(Console.ReadLine());
        double area = Math.PI * Math.Pow(radius, 2);
        Console.WriteLine("The area of the circle is: " + area);
    }

    static void CalculateRectangleArea()
    {
        Console.Write("Enter the length of the rectangle: ");
        double length = double.Parse(Console.ReadLine());
        Console.Write("Enter the width of the rectangle: ");
        double width = double.Parse(Console.ReadLine());
        double area = length * width;
        Console.WriteLine("The area of the rectangle is: " + area);
    }

    static void CalculateTriangleArea()
    {
        Console.Write("Enter the base of the triangle: ");
        double baseLength = double.Parse(Console.ReadLine());
        Console.Write("Enter the height of the triangle: ");
        double height = double.Parse(Console.ReadLine());
        double area = 0.5 * baseLength * height;
        Console.WriteLine("The area of the triangle is: " + area);
    }
}
