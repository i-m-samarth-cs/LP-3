def knapsack(values, weights, capacity):
    dp = [0] * (capacity + 1)
    for v, w in zip(values, weights):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]

if __name__ == "__main__":
    while True:
            print("\nPress Ctrl+C to terminate...")
            
            # Use 'split()' for flexible space separation
            values_in = [int(i) for i in input("Enter values of items (space-separated): ").split()]
            weights_in = [int(i) for i in input("Enter weights of items (space-separated): ").split()]
            capacity_in = int(input("Enter maximum weight: "))
            
            if len(values_in) != len(weights_in):
                print("Error: The number of values must match the number of weights.")
                continue

            maximum_value = knapsack(values_in, weights_in, capacity_in)
            print('The maximum value of items that can be carried:', maximum_value)