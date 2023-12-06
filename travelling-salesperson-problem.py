from itertools import permutations

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]  # Return to the starting city
    return total_distance

def tsp(distances):
    num_cities = len(distances)
    all_routes = permutations(range(num_cities))
    min_distance = float('inf')
    optimal_route = None

    for route in all_routes:
        distance = calculate_distance(route, distances)
        if distance < min_distance:
            min_distance = distance
            optimal_route = route

    return optimal_route, min_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_route, min_distance = tsp(distances)
print("Optimal Route:", optimal_route)
print("Minimum Distance:", min_distance)
