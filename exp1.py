def circle_of_friends(n, k):
    friends = list(range(1, n + 1))
    index = 0

    while len(friends) > 1:
        index = (index + k - 1) % len(friends)
        eliminated_friend = friends.pop(index)
        print(f"Eliminated friend: {eliminated_friend}")

    winner = friends[0]
    return winner

n = int(input("Enter the number of friends: "))
k = int(input("Enter the count: "))

winner = circle_of_friends(n, k)
print(f"The final winner is friend: {winner}")