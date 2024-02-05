def numberinlist(new_array):
    new_list = []
    list_string = map(str, new_array)
    for elem in list_string:
        new_list.append(len(elem))

    return new_list



new_array = []

number = input("Enter the number of items in your array")

for i in range(number):
    element = input("Enter element for the array: ")
    new_array.append(element)

print(numberinlist(new_array))