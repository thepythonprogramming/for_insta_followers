num = int(input("Enter a number : "))  # input

sum_ = 0
temp = num
while temp > 0:  # sum of the cube of each digit
    digit = temp % 10
    sum_ += digit ** 3
    temp //= 10

# result
if num == sum_:
    print(num, " is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


