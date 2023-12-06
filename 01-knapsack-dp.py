def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
weights = [3, 5, 5, 8, 4]
profits = [10, 20, 21, 30, 16]
capacity = 20
result = knapsack_dynamic_programming(weights, profits, capacity)
print(result)
