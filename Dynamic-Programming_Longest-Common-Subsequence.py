def lcs(X, Y):
    m = len(X)
    n = len(Y)
    lcs_table = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])
    return lcs_table[m][n], reconstruct_lcs(X, Y, lcs_table)

def reconstruct_lcs(X, Y, lcs_table):
    i = len(X)
    j = len(Y)
    lcs = ''
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs = X[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_table[i-1][j] > lcs_table[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs
X = "AGGTAB"
Y = "GXTXAYB"
length, LCS = lcs(X, Y)
print("Length of LCS:", length)
print("LCS:", LCS)
