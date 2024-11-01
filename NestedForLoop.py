print("1.print multiplication tables")
for i in range(1,11):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
print()

print("2.print pyramid pattern with numbers")
rows=5
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print()

print("3.print reverse pyramid pattern with numbers")
rows=5
for i in range(rows,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print()
print()

print("4.1.Nested for loop problem")
for i in range(3):
    print(i)
    for j in range(3):
        print(j)
print()

print("4.2.Nested for loop problem")
for i in range(3):
    for j in range(3):
        print(i,"-----",j)
print()

print("4.3.Nested for loop problem ")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
for i in L1:
    print(i)
    for j in i:
        print(j)
print()

print("4.4.Nested for loop problem")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
for i in L1:
    for j in i:
        print(j)
print()

print("4.5.Nested for loop problem")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
for i in L1:
    for j in i:
        print(j,end=" ")
print()

print("4.6.Nested for loop problem")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
for i in L1:
    for j in i:
        print(j,end=" ")
    print()



