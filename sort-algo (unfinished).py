list_of_things = []

digits = '0123456789'

add_to_list: bool = True

print("\nCreate a new string to add to the list")
print("Enter 'done' to quit\n")

while add_to_list == True:
    new = input("> ")

    match new:
        case 'done':
            add_to_list = False
        case _:
            list_of_things.append(new)
            print("Added to the list!\n")

print("How do you want your list sorted?")
print("Enter 'asc', 'desc', or 'none'")
sort_type = input("> ")

for item in list_of_things:
    if sort_type.lower() == 'asc':
        pass
    elif sort_type.lower() == 'desc':
        pass
    elif sort_type.lower() == 'none':
        pass
    else:
        pass
