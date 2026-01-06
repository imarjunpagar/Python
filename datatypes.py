# 01-01-2026

#String 
def Square(X):
    return X * X 

def main():
 print("String is set of variables in Sequence")

#using of Methods in A String
#Type 1 declaring methods
 
Avegenrs = input("Who is Avenger: ")
Avegenrs = Avegenrs.capitalize()
print(f"Hello Sir {Avegenrs}")

# # #Type 2 declaring methods
Film = input("Enter the Movie Name: ").title().strip()
print(f"The Movie is : {Film}")

Fullname = input("Enter your full Name :")
First,middle,last = Fullname.split()
print(f"the First name is {First}, Middle is {middle}, Sirname is {last}")



# # Integers 
A = 45
print(A)

# #Simple Addition Calculator
x = input("What is First number:")
y = input("What is second number:")

z = int(x) + int(y)  #Here By chaging opreator we Can Perform any mathemathical Opreation
print(z)

num = int(input("Enter a number"))
print("The Square of given number is:", Square(num))



def Square(X):
      return X * X    # also we can delcare this function before the def main if we have to 

#Float
flt = float(input("Enter the num:"))
print(f"the given float is :{flt}")

Subs = float(input("Enter first no"))
Subs1 = float(input("Enter the second no"))

Ans = float(Subs) - float(Subs1)

print(round(Ans))



 
main()


 



