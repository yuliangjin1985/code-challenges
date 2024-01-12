def wildcardMatching(string, pattern):
    """
    :type string: str
    :type pattern: str
    :rtype: bool
    """
    m, n = len(string), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = True
        else:
            break
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]

    return dp[m][n]

# tests
print(wildcardMatching("aa", "a") == False)
print(wildcardMatching("aa", "*") == True)
print(wildcardMatching("cb", "*a") == False)
print(wildcardMatching("adceb", "*a*b") == True)
print(wildcardMatching("acdcb", "*cb") == True)
print(wildcardMatching("acdcb", "*cdb") == False)

