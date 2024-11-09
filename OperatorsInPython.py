print("1.Arithematic operators are +,-,*,/,//,** ")
x1=eval(input("enter the number of x1:"))
x2=eval(input("enter the number of x2:"))
res1=x1+x2
print(res1)
res2=x1-x2
print(res2)
res3=x1*x2
print(res3)
res4=x1/x2
print(res4)
res5=x1//x2  #"print without zero"
print(res5)
res6=x1**x2
print(res6)
print()

print("2.Assignment operators are =,+=,-=,*=,/=,//=,**=,%=")
x1=eval(input("enter the number of x1:"))
x2=eval(input("enter the number of x2:"))
x1=x2
print(x1)
x1+=x2           #"x1+=x2=x1=x1+x2"
print(x1)
x1-=x2
print(x1)
x1*=x2
print(x1)
x1/=x2
print(x1)
x1//=x2
print(x1)
x1**=x2
print(x1)
x1%=x2
print(x1)
print()

print("3.spical type operators")
print("a.Indentity operators are is,is not")
L1=input("enter the string:")
print("i" in L1)
print("k" not in L1)
print()

print("b.Membership operators are in and not in")
L1=input("enter the string:")
print("i" in L1)
print("k" not in L1)
print()

print("4.Equality operators are ==,!=")
x1=eval(input("enter the number of x1:"))
x2=eval(input("enter the number of x2:"))
print(x1==x2)
print(x1!=x2)
print()

print("5.comparision operators are <,>,<=,>=")
x1=eval(input("enter the number of x1:"))
x2=eval(input("enter the number of x2:"))
print(x1<x2)
print(x1>x2)
print(x1<=x2)
print(x1>=x2)
print()

print("6.Logical operators are and ,or ,not")
print("Logical And") # "if both are true then only true otherwise false"
gmail=input("enter the email:")
password=input("enter the password:")
if(gmail=="koti123@gmail.com" and password==123456):
    print("login successsfully")
else:
    print("invalid")
print()

print("Logical or") #"if both are false then only false otherwise true"
gmail=input("enter the email:")
password=input("enter the name:")
p1=input("enter the p1:")
if(gmail=="koti123@gmail.com" or password=="koti123@gmail.com" or p1==123 ):
    print("login successsfully")
else:
    print("invalid")
print()

print("Logical not")  #"true----->false"
x1=True
print(x1)
x2=not x1
print(x2)
print()

print("7.Bitwise Operators are &,|,^,~,<<,>>")
print("BItwise And(&)") #"if both gets true then only true otherwise false"
print("the result:",4&5)
print()
print("Bitwise Or(|)")  #"if both gets false then only false otherwise true"
print("the result:",4|5)
print()
print("Bitwise Exclusive(^)")  #"if only one true in true otherewise false"
print("the result:",4^5)
print()
print("Bitwise Complement(~)") #"it is used for increment and decrement" 
x1=123
x2=~x1
print(x2)
print()
print("BItwise Right Shift(>>)")
x1=123
x2=x1>>123
print(x2)
print()
print("BItwise Left Shift(<<)")
x1=123
x2=x1<<123
print(x2)
print()











