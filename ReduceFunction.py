print("Reduce Function")  #"combine multipule objects into a single entity" and it is a functools module
print("functools module")

from functools  import reduce
if(__name__=="__main__"):
    emp_salary=[5500,55566,56989,99620,56388]
    total_salary=reduce(lambda x1,y1:x1+y1,emp_salary)
    print(total_salary)
print()