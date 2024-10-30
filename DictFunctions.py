print("1.access a value using a key")
dict={"name":"ravi","age":24,"salary":30000}
print(dict["name"])
print(dict["salary"])
print()

print("2.add or update a key value pair")
dict={"name":"ravi","age":24,"salary":30000}
dict["city"]="new york"  # "adding new key value pair"
dict["age"]=25   #"updating "
print(dict)
print()

print("3.delete key value pair")
dict={"name":"ravi","age":24,"salary":30000}
del dict["age"]
print(dict)
print()


print("4.loop through a dict")
dict={"name":"ravi","age":24,"salary":30000}
for key,value in dict.items():
    print(key,value)
print()

print("5.check key exist or not in dict")
dict={"name":"ravi","age":24,"salary":30000}
print("age" in dict)
print("sal" in  dict)
print()

print("6.dict comprehension")
dict={x:x*x for x in range (1,6)} 
print(dict)
print()

print("7.merge two dict")
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
dict1.update(dict2)
print(dict1)
print()

print("8.get  all keys and values")
dict={"name":"ravi","age":24,"salary":30000}
print(dict.keys())
print(dict.values())