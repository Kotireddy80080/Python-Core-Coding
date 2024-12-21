print("Lambda fuction")   #"nameless function"
print("1.squares of numbers")

if(__name__=="__main__"):
    s1=lambda x1:x1*x1     #x1:x1**2
    print(s1(5))
    print(s1(-5))
    print(s1(5.5))
print()


print("2.add two numbers")
if(__name__=="__main__"):
    s1=lambda a,b:a+b
    print(s1(4,6))
    print(s1(5.5,6.6))
print()


print("3.max number")
if(__name__=="__main__"):
    s1=lambda a,b:a if a>b else b
    print(s1(8,4))
print()


print("4.check even or not")
if(__name__=="__main__"):
    s1=lambda x:x%2==0
    print(s1(4))
    print(s1(9))
print()

print("5.To sort list of tuples be second element")
if(__name__=="__main__"):
    s1=[(1,5),(5,1),(2,5)]
    x=sorted(s1,key=lambda x:x[1])
    print(x)
print()

print("6.polindrome of a string")
if(__name__=="__main__"):
    s1=lambda x:x==x[::-1]
    print(s1("radar"))
print()


print("6.Reverse of a string")
if(__name__=="__main__"):
    s1=lambda x:x[::-1]
    print(s1("radar"))
print()