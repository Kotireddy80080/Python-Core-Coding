print("Variable arguments")

import time 
def Test_Case1(*obj1):
    print(obj1)
if(__name__=="__main__"):
    Test_Case1()
    print()
    Test_Case1(1001)
    print()
    Test_Case1(1001,1002)
    print()
    Test_Case1(1001,1002,1003)
    print()
    Test_Case1(1001,1002,1003,1004)
print()
time.sleep(2)
print("End of an application")


import time 
def Test_Case1(*obj1):
    for x1 in obj1:
        print(x1)
  
if(__name__=="__main__"):
    Test_Case1()
    print()
    Test_Case1(1001)
    print()
    Test_Case1(1001,1002)
    print()
    Test_Case1(1001,1002,1003)
    print()
    Test_Case1(1001,1002,1003,1004)
print()
time.sleep(2)
print("End of an application")

import time 
def Test_Case1(*obj1):
    S1=0 
    for x1 in obj1:
        S1=S1+x1 
    print("Sum of argumets are:",S1)
if(__name__=="__main__"):
    Test_Case1()
    print()
    Test_Case1(1001)
    print()
    Test_Case1(1001,1002)
    print()
    Test_Case1(1001,1002,1003)
    print()
    Test_Case1(1001,1002,1003,1004)
print()
time.sleep(2)
print("End of an application")

import time 
def Test_Case1(*obj1):
    for x1 in obj1:
        time.sleep(1)
        print(x1)
 
if(__name__=="__main__"):
    Test_Case1("Jessica_1","John","jessica_12346","JA_12346","JA_12346","jessica_1@gmail.com")
    print()
    Test_Case1("Jessica_2","John","jessica_12346","JA_12346","JA_12346","jessica_2@gmail.com")
   
print()
time.sleep(2)
print("End of an application")
