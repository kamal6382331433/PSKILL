total = int(input())
a = []
b = []
for i in range(0, total):
    x = int(input())
    a.append(x)
print(a)

for i in range(0, total - 2):
    for j in range(i, i + 3):
        print(a[j], end='')
    print()
