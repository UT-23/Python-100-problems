a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# GCD
c = []
for i in range(1, a+1):
    if a % i == 0:
        c.append(i)
d = []
for i in range(1, b+1):
    if b % i == 0:
        d.append(i)
gcd = max(list(set(c) & set(d)))
print("GCD", gcd)

# LCM
e = []
for i in range(2, max(a,b)+1):
    s = max(a,b) * i
    if s % min(a,b) == 0:
        e.append(s)
print("LCM", min(e))