print("1.union of two sets")  #"combines all unique elements in two sets"
set1={1,2,3}
set2={3,4,5}
union=set1.union(set2)  #you can also use union symbol "|"
print(union)
print()

print("2.intersection of two sets")  #"common elements in two sets"
set1={1,2,3}
set2={3,4,5}
set3=set1.intersection(set2)  #you can also use intersection symbol "&"
print(set3)
print()

print("3.difference between two sets")  #"returns elements in first set not in second set"
set1={1,2,3}
set2={3,4,5}
set3=set1.difference(set2)  #you can also use difference symbol "-"
print(set3)
print()

print("4.Symmetric difference between two sets")  #"repeted elements in two sets but not inn both"
set1={1,2,3}
set2={3,4,5}
set3=set1.symmetric_difference(set2)  #you can also use symmetric symbol "^"
print(set3)
print()

print("5.adding a element in a set")
set={1,2,6,3}
set.add(8)
print(set)
print()

print("6.remove a element in a set")
set={1,2,6,3}
set.remove(2)
print(set)
print()

print("7.discard a element in a set")
set={1,2,6,3}
set.remove(2)
print(set)
print()

print("8.discard a element in a set")   #" discard means remove a number"
set={1,2,6,3}
set.discard(2)
print(set)
print()

print("9.remove last element in a set")
set={1,2,6,3}
set.pop()
print(set)
print()


print("10..isdisjoint  of two set") #"set has no common elements in both sets"
set1={1,2,3}
set2={4,5,6}
set3=set1.isdisjoint(set2)
print(set3)
print()


print("11.issubset of two sets")  #"set1 issubset of set2 or not"
set1={1,2,3}
set2={4,5,6}
set3=set1.issubset(set2)
print(set3)
print()

print("12.issuperset  of two set") #"set1 issuperset of set2 or not"
set1={1,2,3}
set2={4,5,6}
set3=set1.isdisjoint(set2)
print(set3)
print()

