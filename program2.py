def decode_message(s: str, p: str) -> bool:
    # Length of the message and the pattern
    m, n = len(s), len(p)
    
    # DP table of size (m+1) x (n+1) initialized to False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns with '*' at the start that can match an empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # If current characters match, or '?' can replace a single character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # If '*' can match zero or more characters
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    
    # The result is whether the entire message matches the entire pattern
    return dp[m][n]
