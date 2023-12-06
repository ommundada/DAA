class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    items = list(zip(values, weights, range(n)))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    max_profit = 0
    queue = []

    u = Node(-1, 0, 0, 0)
    v = Node(0, 0, 0, 0)

    queue.append(u)

    while queue:
        u = queue.pop(0)

        if u.level == n - 1:
            continue

        v.level = u.level + 1
        v.weight = u.weight + items[v.level][1]
        v.profit = u.profit + items[v.level][0]

        if v.weight <= capacity and v.profit > max_profit:
            max_profit = v.profit

        v.bound = bound(v, n, capacity, items)

        if v.bound > max_profit:
            queue.append(v)

        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, capacity, items)

        if v.bound > max_profit:
            queue.append(v)

    return max_profit

def bound(u, n, capacity, items):
    if u.weight >= capacity:
        return 0

    total_value = u.profit
    j = u.level + 1
    total_weight = u.weight

    while j < n and total_weight + items[j][1] <= capacity:
        total_weight += items[j][1]
        total_value += items[j][0]
        j += 1

    if j < n:
        total_value += (capacity - total_weight) * (items[j][0] / items[j][1])

    return total_value

# Example usage
weights = [3, 5, 5, 8, 4]
values = [10, 20, 21, 30, 16]
capacity = 20
result = knapsack_branch_and_bound(weights, values, capacity)
print(result)

