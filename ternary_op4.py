value = input("enter any value: ")
res = "Palindrome" if value == value[::-1] else "Not Palindrome"
print("{},{}".format(value,res))