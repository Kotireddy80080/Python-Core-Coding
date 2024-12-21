print("Filter Function") #"filter the data"
print("filter with namefull function")

def test_case1(number1):
    if number1%2==0:
        return True
    else:
        return False
if(__name__=="__main__"):
    number1=[1,2,3,4,5,6,7,8,9,10]
    L1=list(filter(test_case1,number1))
    print(L1)
    print()
    for x1 in L1:
        print(x1)
print()


print("filter with nameless function")
if(__name__=="__main__"):
    number1=[1,2,3,4,5,6,7,8,9,10]
    L1=list(filter(lambda x1:x1%2==0, number1))
    print(L1)
    print()
    for x in L1:
        print(x)
print()
