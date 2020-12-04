arr = ['p', 'y', 't', 'h', 'o', 'n', '.', 'p', 'y']
x = str(input("enter the element to search : "))


def binary_search(array, x_element):
    a = 0
    b = len(array)
    while a <= b:
        c = (a + b) // 2
        if array[c] < x_element:
            a = c + 1
        elif array[c] > x_element:
            b = c - 1
        else:
            return c
    return -1


print("element found at index " + str(binary_search(arr, x)))
