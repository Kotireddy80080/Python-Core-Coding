print("List comprehension")
print("1.print list comprehension numbers")
L1=[x*x for x in range(3,12)]
print(L1)
print(type(L1))
print()
for x in L1:
    print(x)
print()

print("2.print even comprehension numbers")
L1=[x*x for x in range(3,12) if x%2==0]
print(L1)
print(type(L1))
print()
for x in L1:
    print(x)
print()

print("3.print odd comprehension numbers")
L1=[x*x for x in range(3,12) if x%2==1]
print(L1)
print(type(L1))
print()
for x in L1:
    print(x)
print()

print("tuple comprehensions")
print("1.print tuple comprehension numbers")
L1=(x*x for x in range(3,12))
print(*L1) # Here "*" is used to print the result
print(type(L1))
print()


print("2.print tuple comprehension numbers")
L1=(x*x for x in range(3,12) )
for i in L1:
    print(i)
print(type(L1))
print()

print("3.print even tuple comprehension numbers")
L1=(x*x for x in range(3,12) if x%2==0)
for i in L1:
    print(i)
print(type(L1))
print()

print("set comprehension")
print("1.print set comprehension numbers")
L1={x*x for x in range(3,12)}
print(L1)
print(type(L1))
print()
for x in L1:
    print(x)
print()

print("1.print even set comprehension numbers")
L1={x*x for x in range(3,12) if x%2==0}
print(L1)
print(type(L1))
print()
for x in L1:
    print(x)
print()

print("Dict comprehension")
print("1.print dict comprehension numbers")
L1={x:x*x for x in range(3,12)}
print(L1)
print(type(L1))
print()
for x1,x2 in L1.items():
    print(x1,"----",x2)
print()

print("1.print dict comprehension numbers")
L1={x:x*x for x in range(3,12) if x%2==0}
print(L1)
print(type(L1))
print()
for x1,x2 in L1.items():
    print(x1,"----",x2)
print()















