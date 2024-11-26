print("Transfer Statements")
print("1.Break-it used to exit the loop")
print("Break with example")
for i in range(10):
    if i==5:
        print("breaking at:",i)
        break
    print(i)
print()


print("2.continue-skips the current and procedus the next iteration")
for i in range(10):
    if i==5:
        print("skip num:",i)
        continue
    print(i)
print()

print("3.pass-it acts as a placeholder and prints nothing")
if True:
    pass  # Placeholder for future code
else:
    print("This will never run.")
print()

print("4.how we use both break and continue")
for i in range(10):
    if i%2==0:
        continue
    if i >7:
        break
    print(i)
print()

print("5. Write a program to find the first multiple of 7 greater than 50 using break.")
for i in range(50,101):
    if i%7==0:
        print("first multiple of 7 greater than 50:",i)
        break
print()

print("6.How does the else block work with loops in Python")
for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("loop completed successfully")
print()

print("7.print greater than 50 in a list")
L1=[5,4,8,99,55,77,5,11,88,77,55,1,55,8,86]
for i in L1:
    if i>50:
        print(i)
print()



