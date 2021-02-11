#Pseudo code
#1)Prompt user to enter marks
#2)Average
#3)Print grade
a=int(input("Enter Maths marks:"))
b=int(input("Enter Kiswahili marks:"))
c=int(input("Enter English marks:"))
d=int(input("Enter Biology marks:"))
e=int(input("Enter Chemistry marks:"))
f=int(input("Enter Swimming marks:"))

x=((a+b+c+d+e+f)/6)
if(x>=70 and x<=100):
    print("Mean Grade is A")
elif(x>=60 and x<=69):
    print("Mean Grade is B")
elif(x>=50 and x<=59):
    print("Mean Grade is C")
elif(x>=40 and x<=49):
    print("Mean Grade is D")
else:
    print("Mean Grade is E")