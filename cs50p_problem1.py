# these are the problem given by CS50P
# This All problem solved code is in the def main function u can use seprate for eack

#problem 1: implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

#problem 2: n a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
# #If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,#
# and treat the user’s greeting case-insensitively.

#problem 3: In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media #
# type if the file’s name ends, case-insensitively, in any of these suffixes

#problem 4: In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs
# the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space #
# between x and y and one space between y and z, wherein:
#x is an integer
#y is +, -, *, or /
#z is an integer
#For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
#
# Problem 5: implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time 
# #for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that 
# #each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
#Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
# # to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 
# #7.5 (i.e., 7.5 hours).


def main ():

#Solution of Problem 1 
 Que = input("What is Answer to the great question of Life, the Universe, and Everything:")
 if Que == "42" or Que == "forty-two" or Que == "forty two":
  print("Yes")
 else:
  print("No")

#Solution for Problem 2
  
  Greet = input("Greetings:").strip().lower()

  if Greet == ("hello"):
    print("$0")
  elif  Greet.startswith("h"):
    print("$20")
  else:
    print("$100")

#Solution for Problem 3
    #Solved without creating a funnction
    print("Note :- The file extensions should be proper file types")
    File_name = input("Enter the file Name:")

    if f"{File_name}".endswith(".gif"):
        print("image/gif")
    elif f"{File_name}".endswith(".jpg"):
        print("image/jpg")
    elif f"{File_name}".endswith(".jpeg"):
        print("image/jpeg")
    elif f"{File_name}".endswith(".png"):
        print("image/png")
    elif f"{File_name}".endswith(".pdf"):
        print("Document/pdf")
    elif f"{File_name}".endswith(".txt"):
        print("text/txt")
    elif f"{File_name}".endswith("zip"):
        print("application/zip")
    else:
        print("error")

#Solution for Problem 4:

    Exp = input("Expression:")
    x_str,y,y_str = Exp.split()

    x = int(x_str)
    z = int(y_str)

    match y:
        case "+":
            print(float(x + z))

        case "-":
            print(float(x - z))
        case "*":
            print(float(x * z))
        case "/":
            if z == 0:
                print("error z cannot be zero")
            else:
                print(float(x / z))  
                
# Solution of problem 5:           
    Tme = input("Enter a Time:")
    time = convert(Tme)  

    if 7.00 <= time <= 9.00 :
        print("Breakfast time")
    elif 12.00 <= time <= 14.00 :
        print("Lunch time")
    elif 18.00 <= time <= 19.00:
        print("Dinner time")
    
def convert(time):
    hrs, minutes = time.split(":")

    new_time = float(hrs) + float(minutes) / 60
    return new_time
main()