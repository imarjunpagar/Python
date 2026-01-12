# let's Start with While:
#Program that wrritens Meow 3 times
i = 3
while i != 0:
    print("Meow")
    i = i - 1
print()            #added for givving extra line in shown output


#promgram that prints 1 to 10
c = 0
while c < 11:
    print(f"{c}", sep="/n")
    c = c + 1
print()

#reverse printing of number
a = 20
while a >- 0:
    print(f"{a}")
    a = a -1


#program that gives only even no as output by taking Range for user


x = int(input("Enter a Start:"))
y = int(input("Enter the end:"))
z = x
if x % 2 == 0 and y % 2 == 0:
    while x <= z <= y:
     print(f"{z}")
     z = z + 2
else:
   print("Error Enter a valid Even Number at Start")
print()


password = "YOMEOW123"
guess = ""

while guess != password:
   guess = input("Enter the Password:")

   if guess != password:
      print("Wrong Try again!!!!")

print("Valid password")



#Let's go with For loop


snd = "meow"
for i in range(3):
   print(f"{snd}", end=",")
print()


while True:
   n = int(input("Enter the No:"))
   if n > 0:
      break
   
p = n
for _ in range(p):
   print("Meow")



students = ["Homelander","Hugie","Starlght","Butcher","A-train"]


# for students in students:
#    print(students)
 
for i in range(len(students)):
   print(students[i], i + 1)



while True:
   
     e = int(input("Enter a Start number:"))
     f = int(input("Enter a Stop  number:"))
     if e % 2 != 0 and f % 2 != 0 and e != 0 :
        break
    
for _ in range(e,f,2):
 print(_)




# Combining  for and while
 def main():

    while True:
     Sound_num = int(input("enter the number"))
     if Sound_num != 0:
        break
    M_N(Sound_num)
     
def M_N(s):
    fr = "Meow"
    for _ in range(s):
      print(f"{fr}")

main()
 