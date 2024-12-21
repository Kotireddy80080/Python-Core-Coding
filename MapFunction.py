print("map function")   #"perform some operations and store into another list"
print("map with namefull function")

def test_case1(number1):
    return number1 * 5
if(__name__=="__main__"):
    number1=[122,555,666,88,44,0,5,4]
    L1=list(map(test_case1,number1))
    print(L1)
    print()
    for x in L1:
        print(x)
    print()


print("map with nameless function")
if(__name__=="__main__"):
    number1=[122,555,666,88,44,0,5,4]
    L1=list(map(lambda x1:x1 * 5,number1))
    print(L1)
    print()
    for x in L1:
        print(x)
    print()