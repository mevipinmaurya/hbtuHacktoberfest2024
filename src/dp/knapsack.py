def knapsack_01(values, weights, capacity):
    # the classic 0/1 knapsack problem, solved by using dynamic programming techniques
    n = len(values)
    opt = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weights[i-1] <= j:
                opt[i][j] = max(opt[i-1][j],opt[i-1][j-weights[i-1]]+values[i-1])
            else:
                opt[i][j] = opt[i-1][j]

    return opt[n][capacity]

def unbounded_knapsack(values, weights, capacity):
    # a version of the knapsack problem which considers unlimited supplies for each item
    n = len(values)
    opt = [0]*(capacity+1)

    for j in range(capacity+1):
        for i in range(n):
            if weights[i]<=j:
                opt[j] = max(opt[j], opt[j-weights[i]]+values[i])

    return opt[capacity]

weights = [3,5,1,2,6]
values = [4,8,3,2,5]
capacity = 10

solution_01 = knapsack_01(weights=weights, values=values, capacity=capacity)
print(f"Maximum value (0/1 knapsack): {solution_01}")

solution_unbounded = unbounded_knapsack(weights=weights, values=values, capacity=capacity)
print(f"Maximum value (unbounded knapsack): {solution_unbounded}")

