def rec(N):
    if N:
        rec(N - 1)
    return N
