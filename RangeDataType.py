print("1.print even numbers between begin and end")
for x in range(0,10,2):
    print(x)
print()

print("2.count the no.of elements in range")
r=range(1,10)
print(len(r))
print()

print("3.reverse of a range number")
r=range(1,11)
r1=range(10,0,-1)
print(list(r1))
print()

print("4.check if a number within range or not")
num=5
if num in range(1,11):
    print(num)
print()

print("5.sum of all elements in a range")
r=range(1,11)
print(sum(r))
print()

print("6.largest elements in a range")
r=range(1,11)
print(max(r))
print()

print("7.range of numbers is divisible by number")
r=range(5,50,5)
print(list(r))