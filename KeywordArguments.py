print("Keyword arguments")  # actual paramenters with there values


print("example-1")
import time 
def Test_Student_Case1(Sid,Sname,Subject,Marks):
    print("====Student_Details====")
    print("Sid is:",Sid)
    print("Sname is:",Sname)
    print("Subject is :",Subject)
    print("Marks are:",Marks)
if(__name__=="__main__"):
    Test_Student_Case1(Sid=1001,Sname="Jessica",Subject ="Python",Marks=78)
print()
time.sleep(3)
print('End of an application')


print("example-2")
import time 
def Test_Customer_Case1(Cid=1007,Cname="Jessica",Address="New York"):
    print("====Customer_Information====")
    print("Cid is:",Cid)
    print("Cname is:",Cname)
    print("Address is:",Address)
if(__name__=="__main__"):
    Test_Customer_Case1(Cid=1008,Cname="John",Address="Chicago")
print()
time.sleep(3)
print('End of an application')