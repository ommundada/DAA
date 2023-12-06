def knapsack_greedy(weights, profits, capacity):
    n = len(weights)
    ratios = [(profits[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    selected_items = []
    total_weight = 0
    total_profit = 0

    for ratio, index in ratios:
        if total_weight + weights[index] <= capacity:
            total_weight += weights[index]
            total_profit += profits[index]
            selected_items.append((index,1))
        elif(total_weight + weights[index] > capacity and total_weight != capacity):
          remain_weight = capacity - total_weight
          quantity = remain_weight/weights[index]
          total_weight = capacity
          total_profit += profits[index] * quantity
          selected_items.append((index,quantity))


    return selected_items, total_weight, total_profit

def main():
    # Given data
    indexes = [1,2,3,4,5]
    weights = [3, 5, 5, 8, 4]
    profits = [10, 20, 21, 30, 16]
    capacity = 20

    # Solve the knapsack problem using the greedy method
    selected_items, total_weight, total_profit = knapsack_greedy(weights, profits, capacity)

    # Display the results
    print("Selected Items: (item number ,quantity )", selected_items)
    print("Total Weight:", total_weight)
    print("Total Profit:", total_profit)

if __name__ == "__main__":
    main()


