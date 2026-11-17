int minimumChanges(char* s, int k) {
    int n = strlen(s);
    int INF = 1e9;

    // Allocate cost[n][n+1]
    int** cost = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        cost[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) {
            cost[i][j] = INF;
        }
    }

    // Precompute conversion costs for semi-palindromes
    for (int i = 0; i < n; i++) {
        for (int j = i + 2; j <= n; j++) {
            int m = j - i;
            for (int d = 1; d < m; d++) {
                if (m % d != 0) continue;
                int changes = 0;
                int group_len = m / d;

                for (int r = 0; r < d; r++) {
                    for (int t = 0; t < group_len / 2; t++) {
                        int left = i + r + t * d;
                        int right = i + r + (group_len - 1 - t) * d;
                        if (s[left] != s[right]) {
                            changes++;
                        }
                    }
                }
                if (changes < cost[i][j]) {
                    cost[i][j] = changes;
                }
            }
        }
    }

    // Allocate dp[n+1][k+1]
    int** dp = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int*)malloc((k + 1) * sizeof(int));
        for (int p = 0; p <= k; p++) {
            dp[i][p] = INF;
        }
    }
    dp[0][0] = 0;

    // Dynamic programming transition
    for (int i = 1; i <= n; i++) {
        for (int p = 1; p <= k; p++) {
            for (int j = 2 * (p - 1); j < i - 1; j++) {
                if (dp[j][p - 1] == INF) continue;
                int val = dp[j][p - 1] + cost[j][i];
                if (val < dp[i][p]) {
                    dp[i][p] = val;
                }
            }
        }
    }

    
    return dp[n][k];
}


