dp = [[-1 for i in range(3001)] for j in range(1001)]
def recBananaCnt(A, B, C):
    if (B <= A):
        return 0
    if (B <= C):
        return B - A
    if (A == 0):
        return B
    if (dp[A][B] != -1):
        return dp[A][B]
    maxCount = -2**32
    tripCount = ((2 * B) // C) - 1 if (B % C == 0) else ((2 * B) // C) + 1
    for i in range(1, A+1):
        curCount = recBananaCnt(A - i, B - tripCount * i, C)
        if (curCount > maxCount):
            maxCount = curCount
            dp[A][B] = maxCount
    return maxCount


def maxBananaCnt(A, B, C):
    print("Calculating...")
    return recBananaCnt(A, B, C)


A = 1000
B = 3000
C = 1000
print(maxBananaCnt(A, B, C))
