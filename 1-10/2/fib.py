sum = 0
f1 = 2
f2 = 1
while f1 < 4000000:
    sum += f1 if f1%2==0 else 0
    f1 += f2
    f2 = f1 - f2

print(sum)

