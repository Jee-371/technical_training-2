def min_trips(boxes, max_weight):
    n = len(boxes)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        total_weight = 0
        unique_ports = set()
        for j in range(i - 1, -1, -1):
            total_weight += boxes[j][0]
            unique_ports.add(boxes[j][1])
            if total_weight > max_weight or len(unique_ports) > 2:
                break
            dp[i] = min(dp[i], dp[j] + 1)
    return dp[n]
boxes = [(1, 'A'), (2, 'A'), (1, 'B'), (4, 'A'), (1, 'B')]
max_weight = 5
print("Minimum number of trips:", min_trips(boxes, max_weight))
