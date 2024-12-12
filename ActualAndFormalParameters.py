print("formal parameters")   # creating a function
print("actual parameters")   # calling a function


print("example-1")
import time 
def Test_Employee_Case1(Eid,Ename,Esal,Company):
    print("=====Employee_Details=====")
    print("Eid is:",Eid)
    print("Ename is:",Ename)
    print("Esal is:",Esal)
    print("Company is:",Company)
if(__name__=="__main__"):
    Test_Employee_Case1(1001,"Rahul",23000,"Dell")
print()
time.sleep(3)
print("End of an application")


print("example-2")
import time 
def Test_Employee_Case1(Eid,Ename,Esal,Company):
    print("=====Employee_Details=====")
    print("Eid is:",Eid)
    print("Ename is:",Ename)
    print("Esal is:",Esal)
    print("Company is:",Company)
if(__name__=="__main__"):
    Test_Employee_Case1(1001,"Rahul_1",23000,"TCS")
    print()
    Test_Employee_Case1(1002,"Rahul_2",29000,"TCS")
    print()
    Test_Employee_Case1(1003,"Rahul_3",31000,"TCS")

print()
time.sleep(3)
print("End of an application")


print("example-3")
import time 
def Test_Product_Details():
    Pid=int(input("Enter the Pid:"))
    Pname=input("Enter the Pname:")
    Price=float(input("Enter the Price:"))
    Company=input("Enter the Company:")
    print()
    print("=====Product_Details=======")
    print(Pid,Pname,Price,Company)
    print("============================")
if(__name__=="__main__"):
    Test_Product_Details()
print()
time.sleep(3)
print("End of an application")

print("example-4")
import time 
def Test_Product_Details(Pid,Pname,Price,Company):
    Pid=int(input("Enter the Pid:"))
    Pname=input("Enter the Pname:")
    Price=float(input("Enter the Price:"))
    Company=input("Enter the Company:")
    print()
    print("=====Product_Details=======")
    print(Pid,Pname,Price,Company)
    print("============================")
if(__name__=="__main__"):
    Test_Product_Details(Pid=None,Pname=None,Price=23000,Company=None)
print()
time.sleep(3)
print("End of an application")