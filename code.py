name = input("Enter your name: ")

age =  input("Enter your Age: ")

if(age.isdigit()):
    age = int(age)
else:
    print("Age must be number!!")