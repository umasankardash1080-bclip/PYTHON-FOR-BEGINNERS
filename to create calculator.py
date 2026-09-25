a = int(input("enter your first value :"))
b = int(input("enter your second value :"))
choice = input("enter your choice :(+,-,*,/,%)")
if choice == "+":
    print("sum is ",a+b)
elif choice == "-":
    print("difference is ",a-b)
elif choice == "*":
    print("multiplicaation is ",a*b)
elif choice == "/":
    print("division is",a/b)
elif choice == "%":
    print("modulous is ",a%b)
else :
    print("invalid operator")