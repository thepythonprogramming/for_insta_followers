num = int(input("enter a number : "))
if num < 1:
    print("not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number")
            break
    else:
        print("it is prime number")


lower = 100
upper = 200
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
