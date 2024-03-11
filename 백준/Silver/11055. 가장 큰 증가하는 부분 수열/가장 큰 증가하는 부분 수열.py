cnt = int(input())
num = list(map(int, input().split()))
    
dp = [0] * (cnt)
for i in range(cnt):
    dp[i] = num[i]
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[j] + num[i], dp[i])
print(max(dp))