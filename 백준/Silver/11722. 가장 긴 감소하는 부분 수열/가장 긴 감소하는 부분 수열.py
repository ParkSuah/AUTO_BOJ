cnt = int(input())
num = list(map(int, input().split()))
    
dp = [1] * (cnt)
for i in range(cnt):
    for j in range(i):
        if num[j] > num[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))