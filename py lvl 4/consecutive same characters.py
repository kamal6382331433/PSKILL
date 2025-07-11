def find(s):
    n = len(s)
    k = []
    i = 0

    while i < n:
        count = 1
        j = i + 1
        while j < n and s[i] == s[j]:
            count += 1
            j += 1
        k.append(count)
        i = j

    return max(k)
s = input("Enter: ")
res = find(s)
print(res)
