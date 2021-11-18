print("EMPLOYEE SALARY")
input("Enter Employee name: ")
print("1.Manager")
print("2.Team Leader")
print("3.Team Member")
a=int(input("Choose your designation:"))
if a==1:
  sl=2000
elif a==2:
  sl=1800
elif a==3:
  sl=1500
else:
  print("Enter correct number ")   
present= float(input("Enter days Employee was present: "))
if present>31:
  print("Enter correct value")
bs=float(sl*present)
print("Salary without overtime is: ",bs)
overtime= float(input("How many days of overtime: "))
ot= float(overtime*sl)
print("Overtime Salary is: ",ot)
ts= float(bs+ot)
print("TOTAL SALARY: ",ts)