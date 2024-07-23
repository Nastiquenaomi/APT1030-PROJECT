def grading_system():
    mark= int(input("Enter marks out of 100: "))
    if 0<=mark <=100: #Ensures that only values between 0 and 100 are input
        if mark >= 90: #Assigns a grade depending on the marks imput out of 100
           grade = "A"
        elif mark >= 87:
            grade = "A-" 
        elif mark >= 83:
            grade = "B+"  
        elif mark >= 80:
            grade = "B"
        elif mark >= 77:
            grade = "B-"
        elif mark >= 74:
            grade = "C+"
        elif mark >= 70:
            grade = "C"
        elif mark >= 67:
            grade = "C-"
        elif mark >= 64:
            grade = "D+"
        elif mark >= 62:
            grade = "D"
        elif mark >= 62:
            grade = "D-"
        else:
            grade = "F"
        print(f"Your grade is: {grade}")
    else: 
        print("Enter a value between 1 and 100") #Prompts the user to enter values within the range specified 

   


def main():
    while True:
        grading_system() #Calls the function to assign grade if the user inputs 'YES'
        decision = input("Enter 'YES' or any other character to continue with the process 'NO' to log out: ")
        if decision.lower() == "no":
            print("Program terminated successfully") 
            break #Terminates the program if the user enters 'NO'
       
            
main() #Calls the function to run the main program
