# Python based calculator..

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operation=input("Which operation would you like to perform? ")

# check which number is greater
if "greater" in operation:
    if a>b:
        print(f'{a} is greater than {b}')
    elif a<b:
        print(f'{b} is greater than {a}')

# check if both numbers are even or not
elif "even" in operation:
    if (a%2==0 and b%2==0):       
        print ("Yes, both numbers are even")
    else:
        print ("No, both numbers are not even")     

# performs addition
elif "add" in operation or "+" in operation:
    print(f"The sum of this is {a+b}")

# performs subtraction
elif "subtract" in operation or "-" in operation:
    print(f"The substraction of this is {a-b}")

# performs multiplication
elif "multiply" in operation or "*" in operation:
    print(f"The multiplication of this is {a*b}")

# performs division
elif "divide" in operation or "/" in operation:
    print(f"The division of this is {round(a/b,2)}")

# if some error occurs
else:
    print("Something went wrong..")
