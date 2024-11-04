print("1.print tables with nested while loop")
a=1
while(a<11):
    b=1
    while(b<11):
        print(a,"x",b,"=",a*b)
        b+=1
    a+=1
    print()

print("2.print one num below all nums ")
L1=[1,2,3,4]
L2=[5,6,7,8]
a=0
while(a<len(L1)):
    print(L1[a])
    b=0
    while(b<len(L2)):
        print(L2[b])
        b+=1
    a+=1
print()

print("3.print one num below all nums")
a=1
while(a<5):
    print(a)
    b=1
    while(b<5):
        print(b)
        b+=1
    a+=1
print()

print("4.print one loop to another loop")
a=1
while(a<5):
    b=1
    while(b<5):
        print(a,"----",b)
        b+=1
    a+=1
print()



print("5.Nested whileloop problems")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
a=0
while(a<len(L1)):
    print(L1[a])
    b=0
    while(b<len(L1[a])):
        print(L1[a][b])
        b+=1
    a+=1
print()

print("6.Nested whileloop problems")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
a=0
while(a<len(L1)):
    b=0
    while(b<len(L1[a])):
        print(L1[a][b] ,end=" ")
        b+=1
    a+=1
print()

print("7.Nested while loop problems")
L1=[["A","B","C"],["D","E","F"],["G","H","I"]]
print(L1)
a=0
while(a<len(L1)):
    b=0
    while(b<len(L1[a])):
        print(L1[a][b])
        b+=1
    a+=1
print()








