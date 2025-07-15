def find_celebrity(M):
    n = len(M)
    top = 0
    end = n - 1

    # Find the potential celebrity
    while top < end:
        if M[top][end] == 1:
            # top knows end, so top can't be celebrity
            top += 1
        else:
            # top doesn't know end, so end can't be celebrity
            end -= 1

    # Now top == end, so this person is a candidate
    candidate = top

    # Verify the candidate
    for i in range(n):
        if i != candidate:
            if M[candidate][i] == 1 or M[i][candidate] == 0:
                return -1  # No celebrity found

    return candidate

# Example usage:
M = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]

print("Celebrity is:", find_celebrity(M))
