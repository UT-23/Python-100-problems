a=input("Enter a string : ")
result=""
for i in range(len(a) -1,-1,-1):
    result += a[i]
if (a == result):
    print("Pallindrome")
else:
    print("Not Pallindrome")