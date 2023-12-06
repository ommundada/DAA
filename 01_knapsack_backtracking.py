def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    max_value = [float('-inf')]

    def backtrack(index, current_weight, current_value):
        if index == n or current_weight == capacity:
            max_value[0] = max(max_value[0], current_value)
            return

        if current_weight + weights[index] <= capacity:
            backtrack(index + 1, current_weight + weights[index], current_value + values[index])

        backtrack(index + 1, current_weight, current_value)

    backtrack(0, 0, 0)
    return max_value[0]

# Example usage
weights = [3, 5, 5, 8, 4]
values = [10, 20, 21, 30, 16]
capacity = 20
result = knapsack_backtracking(weights, values, capacity)
print(result)

