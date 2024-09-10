def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    sequence = "1"
    for _ in range(2, n + 1):
        new_sequence = ""
        i = 0

        while i < len(sequence):
            count = 1

            while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
                i += 1
                count += 1

            new_sequence += str(count) + sequence[i]

            i += 1

        sequence = new_sequence

    return sequence

print(countAndSay(1))
print(countAndSay(2)) 
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))
