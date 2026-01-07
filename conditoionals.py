
# all programed are wrriten inside the main function
# for odd even program by builting another way of function
def even(l):
   return l % 2 == 0

def main():

    #simple compariion program using if-elif-else
    x = int(input(f"what is x:"))
    y = int(input(f"What is y"))

    if x < y:
        print("y is grater than X")
    elif x > y:
        print("x is greater than x")
    else:
        print(" x is Equal to y")

#program 2
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

    if a == b:
        print(f"{a} is Equal to {b}")
    elif a > b:
        print(f"{a} is greater than  {b}")
    else:
        print(f"{a} is smaller than {b}")

#program 3

#program using of OR

    score = int(input("Enter the marks:"))

    if score >= 90 or score <= 100:
        print("The Grade is A".title())
    elif score >= 80 or score <= 90:
        print("The grade is B".title())
    elif score >= 70 or score <= 80:
        print("the Grade is C".title())
    else:
        print("the Grade is D".title())

    #program using AND

    Age = int(input("Enter Age:"))
    netizen_info = (input("weather Your Netizens or not: "))
    
    if Age > 18 and netizen_info == ("yes"):
        print("You can vote".title())
    else: 
        print("You cannot Vote".title())

#even odd program using function 
    def is_even(n):
     if    n % 2 == 0:
        return True
     else:
        return False
     
    
     

    num = int(input("Enter a  number"))
    if is_even(num):
       print(f"{num} is even")
    else:
       print(f"{num} is Odd")

    k = int(input("What is number:"))

    if even(k):
        print(f"{k} is Even")
    else:
        print(f"{k} is Odd")


#Match method of conditions | use as or 
    no_plate = (input("Enter the Intial of No plate:"))
    match no_plate:
        case "MH" | "GA":
            print("Car is From Western india".title())
        case "DL" | "HR" | "PB" | "JK" | "UP" | "UK" | "HP":
            print("Car is from north india".title())
        case "SK" | "NL" | "MG" | "MZ" | "MN" | "AR" | "TR":
            print("Car is from North-East India".title())
        case "KA" | "KL" | "TN" | "TS" | "AP":
            print("car is from south india".title())
        case "JH" | "WB":
            print("Car is from East india".title())
        case _:
            print("car is from Middle of India".title())



main()
