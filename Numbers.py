#Numbers

a = 10
b = 5.0

print(type(a))  
print(type(b))     #Checking Data Type of Given Valiue

R = 10
J = 5
print(R + J)       # Addition
print(R - J)       #Substraction
print(R * J)       #Multipliction
print(int(R / J))  # Dvivision Type casted here 
print(R // J)      # Floor Division (Answer only given Without division)
print(R % J)       # gives the remainder
print(R ** J)      # Gives Powers to 


#Some important  in-Built Functions For numbers in python
N = -32
print(abs(N))      #Gives absolute value of given Numbers


print(round(2.5686)) #Gives round up Number
print(pow(2,10))     #Gives Power to the number
print(divmod(17,5))  #Gives the output of Floor divison and Remainder of Passed values
S = [1000, 100 , 10]
print(max(S))        #Gives Maximum Values from Set   
print(min(S))        #Gives Minimum Values From Set
print(sum(S))        #Gives Sum of element in the array, List and Tupple

 
#Typecasting Of values
print(int(10.11))
print(float(9))
print(complex(1))



import math              #Library containing Matheatical Function
print(math.sqrt(2500))   #Gives Squereroot of given number
print(math.ceil(30.30))  #Round ups the value
print(math.floor(10.10)) #Rounddowns the vaue 
print(math.factorial(15))#Gives the Factorial of given value
print(math.pi)           #Gives the value of pi
print(math.e)            #Gives th value of exponential 
print(math.cos)          #takes the value of coasine to use 
print(math.sin)          #Takes the value of sine to use
print(math.gcd(10,5))    #give the value of greatest common divisor
print(math.lcm(30,25))   #Give the LCM of the given two numbers

M = 4 + 2j
print(M.real)           #Finds the real part from the complex mumber
print(M.imag)           #FInds the imaginary parts of complex number








