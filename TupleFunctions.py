print("1.accessing elements in a tuple")
tuple=(12,55,88,66,8,44)
T1=tuple[2]
T2=tuple[5]
print(T1,T2)
print()

print("2.checking  elements exist in tuple or not")
tuple=(25,6,8,1,44,75,266)
T1=1 in tuple
print(T1)
print()

print("3.add or concatnating two tuples")
T1=(5,48,68,1,8)
T2=(9,58,11,44,66)
result=T1+T2
print(result)
print()

print("4.slicing of a string")
T1=(285,8968,858,5,8,66996,526,963,6,)
T2=T1[1:4]
print(T2)
print()

print("5.length of a string")
T1=(1,2,3,4,5,6,8,7,9)
length=len(T1)
print(length)
print()

print("6.find max and min functions")
T1=(55,88,0,8,71,4,712,7,22,75,89,3,847,5,85)
maximum=max(T1)
minimum=min(T1)
print(maximum,minimum)
print()

print("7.count of repited or occurrences in a tuple")
T1=(25,11,88,1,665,81,815,5,1,852,8,1)
count=T1.count(1)
print(count)
print()

print("8.find index of a element")
T1=(25,11,88,1,665,81,815,5,852,8)
index=T1.index(1)
print(index)
print()

print("9.unpacking a tuple")
tuple=(1,2,3,4,5,6)
a,b,c,d,e,f=tuple
print(a,b,c,d,e,f)
print()

print("10.convert tuple in a list")
T1=(1,2,3,4,88,5,6,8)
T2=list(T1)
print(T2)
print()


