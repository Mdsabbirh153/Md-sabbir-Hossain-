a = input("enter your frist number; ")

operator = input("enter operator '(+, - ,*, /, %)  ; ")

b = input("enter your second number; ")


a = int(a)
b = int(b)


if operator == "+":
    print(a+b)
    
elif opetator == "-":
    print(a-b)
    
elif operator == "*":
    print(a*b)
    
elif operator == "/":
    print(a/b)
    
elif operator == "%":
    print(a%b)
    
else:
        print("invaid oparetoion")