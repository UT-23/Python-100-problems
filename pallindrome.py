a = input("Enter a string : ")
a = a.lower()
a = a.replace(" ", "")
result = ""
for i in range(len(a)-1, -1, -1):
    result += a[i]
if a == result:
    print("Palindrome")
else:
    print("Not Palindrome")