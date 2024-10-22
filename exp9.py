def bin_packing(weights, bin_capacity):
    weights.sort(reverse=True)
    bins = []

    for weight in weights:
        placed = False

        for i in range(len(bins)):
            if sum(bins[i]) + weight <= bin_capacity:
                bins[i].append(weight)
                placed = True
                break

        if not placed:
            bins.append([weight])

    for i, b in enumerate(bins):
        print(f"Bin {i + 1}: {b}, Total weight: {sum(b)}")

    return len(bins)

weights = [5, 1, 9, 3, 7, 8, 2]
bin_capacity = 10

min_bins = bin_packing(weights, bin_capacity)
print(f"Minimum number of bins required: {min_bins}")
