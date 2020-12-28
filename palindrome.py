def palindrome(string):
    for i in range(1, int(len(string) / 2)):
        if string[i] == string[len(string) - i - 1]:
            return True
    return False


print(palindrome("heehe"))


def palin(string):
    x = ""
    for i in string:
        x = i + x
    return x


print(palin("hello"))
print(int(palin(str(4567))))
print(palin(str(input(":"))))
