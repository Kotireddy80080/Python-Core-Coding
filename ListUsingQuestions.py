print("1.Reverse of a list")

L1=[20,6,8,0,5,5,9,1,4,3,422,44,55,44,75]
print(L1)
print()
L1.reverse()
print(L1)
print()

print("2.Find largest and smallest element of a list")

L1=[20,6,8,0,5,5,9,1,4,3,422,44,55,44,75]
print(L1)
Largest=max(L1)
print(Largest)
smallest=min(L1)
print(smallest)
print()

print("3.Remove duplicates from a list")

L1=[20,6,8,0,5,5,9,1,4,3,422,44,55,44,75]
L2=[]
for x in L1:
    if(x not in L2):
        L2.append(x)
print(L1)
print(L2)

print("4. Find the Second Largest Element in a List")

L1=[20,6,8,0,5,5,9,1,4,3,422,44,55,44,75]
print(L1)
print()
L1.sort()
print(L1)
print(L1[-2])
print()

print("5.Check it is a polindrome or not")

L1=[1,2,3,2,1]
print(L1)
if (L1==L1[::-1]):
    print(L1[::-1],":polindrome")
else:
    print("not a polindrome")
print()

print("6.Flatten a Nested List")

print("example-1")
L1=[[1],[2,3],[4,5,6,7]]
flat=[]
for x in L1:
    for y in x:
        flat.append(y)
print(flat)

print("example-2")

L1=[[1],[2,3],[4,5,6,7]]
flat=sum(L1,[])
print(flat)

print("7:sum of all elements in a list")
L1=[1,2,3,6,5]
sum=0
for i in L1:
    sum=sum+i
print(sum)
print()

print("8.merge two sorted lists")
L1=[2,6,5,8,3,9]
L1.sort()
print(L1)
L2=[55,66,88,99]
L2.sort()
print(L2)
res=L1+L2
print(res)
print()

print("9.convert list into tuple")
T1=[1,2,3,4,88,5,6,8]
T2=tuple(T1)
print(T2)
print()

print("list properties ")

s1 = [24,63,77,88,11,44,4]
print()
print(s1)
print()
print("append function")
s1.append(555)
print(s1)
print()
print("remove function")
s1.remove(77) 
print(s1)
print()
print("copy function")
s1.copy()
print(s1)
print()
print("insert function")
s1.insert(5,825)
print(s1)
print()
print("pop function")
s1.pop()
print(s1)
print()
print("sorting function")
s1.sort()
print(s1)
print()
s1.sort(reverse=True)
print(s1)
print()
print("sorted functions")
s2=sorted(s1)
print(s2)
print()
s2=sorted(s1,reverse=True)
print(s2)
print()
print("clear function")
s1.clear()
print(s1)
print()




