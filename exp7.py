def getRow(rowIndex: int) -> list:
    # Start with the first row
    row = [1]

    # Generate the rows up to the desired rowIndex
    for i in range(1, rowIndex + 1):
        # Create the new row using the previous row, shifting and adding elements
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]

    return row


# Example Usage:
print(getRow(3))  # Output: [1, 3, 3, 1]
print(getRow(0))  # Output: [1]
print(getRow(4))  # Output: [1, 4, 6, 4, 1]
