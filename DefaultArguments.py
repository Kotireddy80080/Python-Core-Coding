print("Default arguments")  # one or more than one formal paramenters with there values. last value must be placed.


print("example-1")
import time 
def Test_Product_Case1(Pname,Price,Company,Pid=1001):
    print("-----Product_Information-----")
    print("Pid is:",Pid)
    print("Pname is:",Pname)
    print("Price is:",Price)
    print("Company is:",Company)
if(__name__=="__main__"):
    Test_Product_Case1("Laptop_1",23000,"S1")
print()
time.sleep(2)
print('End of an application')


print("example-2")
import time 
def Test_Product_Case1(Pname,Company,Pid=1001,Price=2800):
    print("-----Product_Information-----")
    print("Pid is:",Pid)
    print("Pname is:",Pname)
    print("Price is:",Price)
    print("Company is:",Company)
if(__name__=="__main__"):
    Test_Product_Case1("Laptop_1","S1")
print()
time.sleep(2)
print('End of an application')


print("example-3")
import time 
def Test_Employees_Case1(Eid=1001,Ename="Rahul",Esal=29000,Design="DAD developer"):
    print("====Employee_Details=====")
    print("Eid is:",Eid)
    print("Ename is:",Ename)
    print("Esal is:",Esal)
    print("Design is:",Design)
if(__name__=="__main__"):
    Test_Employees_Case1()
print()
time.sleep(3)
print('End of an application')


print("example-4")
import time 
def Test_Employees_Case1(Eid=1001,Ename="Rahul",Esal=29000,Design="DAD developer"):
    print("====Employee_Details=====")
    print("Eid is:",Eid)
    print("Ename is:",Ename)
    print("Esal is:",Esal)
    print("Design is:",Design)
if(__name__=="__main__"):
    Test_Employees_Case1(1002,"Jessica",56000,"Python Developer")
print()
time.sleep(3)
print('End of an application')


print("example-5")
import time 
def Test_Case1(a,b,c=100):
    return a+b+c 
if(__name__=="__main__"):
    print(Test_Case1(12,18))
print()
time.sleep(3)
print('End of an application')


print("example-6")
import time 
def Test_Case1(a,b,c=100):
    return a+b+c 
if(__name__=="__main__"):
    print(Test_Case1(12,18,1000))
print()
time.sleep(3)
print('End of an application')


print("example-7")
import time 
def Test_Case1(a,b,c=100):
    return a*b+c 
if(__name__=="__main__"):
    print(Test_Case1(12,18,1000))
print()
time.sleep(3)
print('End of an application')

