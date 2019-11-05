def ssm(L):
    best, best_start, best_end = int(-1e10), 0, 0
    s, start, end = 0, 0, 0


    for i in range(len(L)):
        if s < 0:
            start = end = i
            s = L[i]
        else:
            s += L[i]
            end += 1

        if s > best:
            best, best_start, best_end = s, start, end

    return (best, best_start, best_end)

print (ssm([5, -6, 3, 4, -2, 3, -3]))
