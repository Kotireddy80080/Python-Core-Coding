print("1.How can you iterate over a range of numbers using a for loop?")
for i in range(5):
    print(i)
print()

print("2.How does the range() function work in Python?")
for i in range(0,10,2):
    print(i)
print()

print("3.Can you use else with a for loop? How?")
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
print()

print("4.How can you iterate over a list with both index and value?")
iteams=["a","b","c","d"]
for index,value in enumerate(iteams):
    print(index,value)
print()

print("5.How do you loop through multiple lists")    # "using zip function"
L1=["a","b","c","d"]
L2=[2,6,4,7]
for L1,L2 in zip(L1,L2):
    print(L1,L2)
print()

print("6.How can you skip an iteration in a for loop?")
for i in range(5):
    if i == 2:
      continue
    print(i)
print()

print("7.How do you exit a for loop prematurely?")
for i in range(5):
    if i ==2:
        break
    print(i)
print()

print("8.How can you reverse iterate using a for loop?")
for i in reversed(range(5)):
    print(i)
print()

print("9.print each word in a sentence ")
seentence="I will become a software developer in compaany"
for word in seentence.split():
    print(word)
print()

print("10.print each letter in a string")
seentence="ramu"
for letter in seentence:
    print(letter)
print()

print("11.print letters in a row")
seentence="ramu"
for letter in seentence:
   print(letter,end="  ")
print()

print("12.print odd and even num")
L1=[101,102,103,104,105,106]
print("print odd numbers")
for i in L1:
    if i%2==1:
        print(i)
print("print even num")
for i in L1:
    if i%2==0:
        print(i)
print()

print("13.sum of num in a list")
L1=[55,558,999,666,11,5]
sum=0
for i in L1:
    sum=sum+i
print(sum)
print()

print("14.remove duplicates in a string and list")
str="core python"
sum=""
for i in str:
    if i not in sum:
        sum=sum+i
print(sum)

L1=[1,58,5,1,6,84,58]
sum=[]
for i in L1:
    if i not in sum:
        sum.append(i)
print(sum)