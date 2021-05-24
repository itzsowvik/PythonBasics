name_list = []
for i in range (5):
    val = input("Enter Name: ")
    name_list.append(val)

print(name_list)

choice = input("Do you Want to remove someone from list?: ")

if(choice == "Yes"):
    to_remove = input("Enter your choice: ")
    for i in range (len(name_list)-1):
        if(name_list[i] == to_remove):
            name_list.remove(name_list[i])
            print("Name Removed")
            break
        else:
            print("Name Not Found on the list")


print(name_list)
"""print(type(name_list))"""