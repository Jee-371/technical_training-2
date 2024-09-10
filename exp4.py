def crack_safe(n: int, k: int) -> str:
    seen = set()
    result = []

    start = "0" * (n - 1)

    def dfs(node):
        for i in range(k):
            new_node = node + str(i)
            if new_node not in seen:
                seen.add(new_node)
                dfs(new_node[1:])
                result.append(str(i))

    dfs(start)

    return "".join(result) + start

n = 2
k = 2
print(crack_safe(n, k))
