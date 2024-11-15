print("Zip Function")   #"it is used to convert one Data_Str to another Data_Str"

print("List to list example-1")
L1=[101,102,103,104,10,5,105]
L2=[25,69,7,555,9,66,66]
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(list(L3))

print("List to tuple example-2")
L1=[101,102,103,104,10,5,105]
L2=[25,69,7,555,9,66,66]
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(tuple(L3))

print("List to set example-3")
L1=[101,102,103,104,10,5,105]
L2=[25,69,7,555,9,66,66]
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(set(L3))


print("List to dict example-4")
L1=[101,102,103,104,10,5,105]
L2=[25,69,7,555,9,66,66]
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(dict(L3))


print("List and set in dict  example-5")
L1=(101,102,103,104,10,5,105)
L2=[25,69,7,555,9,66,66]
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(dict(L3))


print("tuple to List example-6")
L1=(101,102,103,104,10,5,105)
L2=(25,69,7,555,9,66,66)
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(list(L3))

print("tuple to set example-7")
L1=(101,102,103,104,10,5,105)
L2=(25,69,7,555,9,66,66)
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(set(L3))

print("set to list example-8")
L1={101,102,103,104,10,5,105}
L2={25,69,7,555,9,66,66}
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(list(L3))

print("set to tuple example-9")
L1={101,102,103,104,10,5,105}
L2={25,69,7,555,9,66,66}
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()
L3=zip(L1,L2)
print(tuple(L3))

print("dict example-10")
L1={101,102,103,104,10,5,"aman"}
L2={25,69,7,555,9,66,66}
print(L1)
print(type(L1))
print()
print(L2)
print(type(L2))
print()       
L3=zip(L1,L2)                 #"zib has no attribute items"
for a,b in L3.items():
    print(a,"----",b)
print()








