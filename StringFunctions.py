print("1.Reverse of a string")

S1=("koti is a good boy")
print(S1)
S2=S1[::-1]
print(S2)
print()

print("2.count of char in a string")
from collections import Counter
text="koti is a boy"
String=Counter(text)
print(String)
print()

print("polindrome of string")
S1=("koti is a good boy")
print(S1)
if S1[::-1]:
    print("polindrome")
else:
    print("not a polindrome")
print()

print("count vowels and consonants in a string:")
count_vowels=0
count_consonants=0
alphabets=input("enter any string:")
vowels="AEIOUaeiou"
for i in alphabets:
    if i in vowels:
        count_vowels+=1
    else:
        count_consonants+=1
print("count vowels:",count_vowels)
print("count_consonanats:",count_consonants)
print()

print("4.Remove duplicates in a string")
S1=("koti is a software developer")
S2=" "
for i in S1:
    if(i not in S2):
        S2=S2+i
print(S2)
print()

print("anagrams")
S1="listen"
S2="silent"
anagram=sorted(S1)==sorted(S2)
print(anagram)
print()

print("title case of a string")
S1=("koti")
print(S1)
S2=S1.title()
print(S2)