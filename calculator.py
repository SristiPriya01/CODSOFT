print("enter the choice of operation you want to perform")
print("==>1.Add")
print("==>2.Substraction")
print("==>3.multiplication")
print("==>4.Division")
print("==>5.Modulus")
choice=int(input("enter your choice "))
if choice==1:
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    sum=num1 +num2
    print("the sum is",sum)
elif choice==2:
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    difference=num1 -num2
    print("the sum is",difference)
elif choice==3:
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    multiplication=num1 *num2
    print("the sum is",multiplication)
elif choice==4:
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    division=num1 /num2
    print("the sum is",division)
elif choice==5:
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    modulus=num1%num2
    print("the modulus is",modulus)

else:
    print("enter valid choice")