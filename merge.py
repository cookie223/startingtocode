

A = [1, 2, 3, 4, 0, 0, 0, 0]
B = [2, 3, 4, 5]

m = 4
n = 4


def merge(A, m, B, n):
    'Leetcode requires that change A in place without return anything'
    i, j = 0, 0
    while j < n:
        if i >= m or B[j] < A[i]:
            A.insert(i, B[j])
            j += 1
            m += 1
        i += 1
    return A


print merge(A, m, B, n)
