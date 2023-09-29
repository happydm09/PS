dp = [0] * 35
n = 10

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 8

for i in range(6, 35):
    dp[i] = dp[i - 1] + dp[i - 2]
    if dp[i] >= 4000000: break
    if dp[i] % 2 == 0: n += dp[i]

print(n)

# Answer: 4613732
# Place: 778415
