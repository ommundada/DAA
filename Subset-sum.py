def subset_sum_recursive(S, target, current_subset, index, result):
    if target == 0:
        result.append(current_subset.copy())
        return

    if index == len(S):
        return

    # Include the current element in the subset
    if S[index] <= target:
        current_subset.append(S[index])
        subset_sum_recursive(S, target - S[index], current_subset, index + 1, result)
        current_subset.pop()

    # Exclude the current element from the subset
    subset_sum_recursive(S, target, current_subset, index + 1, result)

def find_subsets_with_sum(S, target):
    result = []
    subset_sum_recursive(S, target, [], 0, result)
    return result

# Example usage:
S = [1, 2, 5, 6, 8,7,3]
target_sum = 9

subsets = find_subsets_with_sum(S, target_sum)

if subsets:
    print("Subsets with sum", target_sum, "are:")
    for subset in subsets:
        print(subset)
else:
    print("No subset found with sum", target_sum)
