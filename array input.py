# creating an empty list
arr = []

# number of elements as input
n = int(input("enter the number of elements in array"))

# iteration till the range
for i in range(0, n):
    element = int(input("enter the array element : "))

    arr.append(element)  # adding element

print(arr)
