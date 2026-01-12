# The Squence of problem is from Easy to Tough level

# problem 1: Check a positive, Negative or Zero
# problem 2: simple Pass or Fail program for students
# problem 3: program for Grade of Students using match method
# problem 4: Largest of Two Numbers
# problem 5: Age category
# problem 6: Eligibility for Exam
# problem 7: Leap Year Checker
# problem 8: Password Validator
# problem 9: Traffic Signal
def main():

#solution for Problem 1

    num = int(input("Enter a Number:"))   #only taking integers as input

    if 0 < num:
        print(f"The Number {num} is Positive")
    elif 0 > num:
        print(f"The number {num} is Negative")
    elif num == 0:
        print(f"The number {0} is zero")
    else:
        print("Invalid!!!!!!!!")
        
# Solution for problem 2

    def passed(b):
      if 35 <= Marks  < 80:
        return (passed)
    
    Marks =int(input("Enter a Marks:"))

    if 80 <= Marks <= 100:
        print("Student passed with disticntion")
    elif passed:
        print(f"Student is passed")
    else:
        print("Failed!!!!")


# Solution for problem 3:

    mrk = int(input("Enter a Marks"))

    if 90 <= mrk <= 100:         
        print("A")
    elif 80 <= mrk < 90:          
        print("B")
    elif 70 <= mrk < 80:
        print("C")
    elif 60 <= mrk < 70:
        print("D")
    elif 35 <= mrk < 60:
        print("E")
    else:
        print("Student Failed!!!!!")

# Solution for problem 4
    
    x = int(input("Enter the First Number:"))
    y = int(input("Enter the Second Number:"))

    if int(x) < int (y):
        print(f"second no {y} is greater then {x}")
    elif int (x) > int (y):
        print(f"First no {x} is greater than {y}")
    else:
        print(f"The no {x} and {y} are Both Equal")

#Subsitute solution using match method

    Exp = (input("Enter a comparision:"))

    f_string,t,c_string = Exp.split()

    match t:
        case "<":
            print(f"Second no {c_string} is greater than {f_string}")
        case ">":
            print(f"first No {f_string} is greater than {c_string}")
        case "=":
            print(f" the no {f_string} is Equal to {c_string}")

#solution for problem 5:

    AGE = int(input("Enter a Age:"))

    if AGE < 13:
        print("User is Child")
    elif 13<= AGE <= 19:
        print("User is teenager")
    elif 20<= AGE <= 59:
        print("User is Adult")
    elif 60 <= AGE < 150:         #150 added for just someone won't enter unlogical input
        print("User is Senior Cetizens")
    else:
        print("Error! Enter valid AGE")


# Solution for Problem 6:

    x_atd = float(input("Enter a Attendence:"))
    y_imr = int(input("Enter a Internal marks:"))
    

    if 75 <= x_atd and 40 <= y_imr:
        print("Student Eligible for Examination")
    else:
        print("Not Eligible for Examination")


# Solution for problem 7:

    def lp_year(n):
       if n % 400 == 0 or n % 4 ==0 and n % 100 != 0:
          return True
       else:
         return False
     
    yr = int(input("Enter a Year :"))
    if lp_year(yr):
        print(f"The year {yr} is Leap year")
    else:
        print(f"The Year {yr} is Not Leap Year")
  
# Solution for problem 8:
    
    ps = input("Enter a password:").strip()

    if len(ps) >= 8 and ps[0].isalpha() :
        print("valid Password")
    else:
        print("Invald Password")

# Solution for problem 9:
    sig = input("Enter a Signale Colour:").strip().lower()
    
    if sig == "red":
        print("Stop!!!!!")
    elif sig == "green":
        print("Gooooo!!")
    elif sig == "yellow":
        print("Get Ready")
    else:
        print("Eror!! Enter a Correct Signal ")


    
main()