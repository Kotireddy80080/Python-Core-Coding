print("If statement") 
str1=input("Enter the string:")
if (str1=="Developer"):
    print(str1)
print()

print("If-else statement")
str1=input("enter the string:")
str2=input("enter the string:")
if (str1==str2):
    print(str1,str2,":valid")
else:
     print(str1,str2,":In_valid")
print()

print("Nested if statement")
F_name=input("enter the F_name:")
L_name=input("enter the L_name:")
if (F_name=="koti"):
    print(F_name)
    if (L_name=="Reddy"):
        print(L_name)
print()

print("if-elif-if statement") # "checks more than one cond:"
p1=input("enter the p1:")
if (p1=="core python"):
    print(p1)
elif (p1=="advanced python"):
    print(p1)
elif (p1=="django"):
    print(p1)
elif (p1=="java script"):
    print(p1)
elif (p1=="sql"):
    print(p1)
else :
    print(p1,"dear student please enroll cource")

print("examples on conditional statements")
print("1.check if a number is +ve or not")
num=int(input("enter the num:"))
if num>0:
    print(num,":+ve number")
elif num<0:
    print(num,":-ve number")
else:
    print(num,":zeros numbers")
print()

print("2.check if a number is even or odd")
num=int(input("enter the num:"))
if (num%2==0):
    print(num,":even  number")
else:
    print(num,":odd number")
print()

print("3.find largest number among numbers")
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if num1>num2 and num1>num3:
    print("largest num:",num1)
elif num2>num1 and num2>num3:
    print("largest number:",num2)
else:
    print("largest number:",num3)
print()

print("4.grade based marks")
marks=float(input("enter your marks:"))
if marks>=90:
    print("A")
elif marks>80:
    print("B")
elif marks>70:
    print("C")
elif marks>60:
    print("D")
else:
    print("F")
print()