def find(cost):
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])

cost = list(map(int, input("Enter: ").split()))
res = find(cost)
print(res)
