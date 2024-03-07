cnt = int(input())
wine = [0 for _ in range(cnt)]
for i in range(cnt):
    wine[i] = int(input())
    
dp = [0 for _ in range(cnt+1)] # 규칙성 쉽게 만들려고 dp[0]=0 추가
for i in range(cnt+1):
    if i == 0:
        pass
    elif i == 1:
        dp[i] = wine[0]
    elif i == 2:
        dp[i] = wine[0]+wine[1]
    else:
        dp[i] = max(dp[i-3]+wine[i-2]+wine[i-1], dp[i-2]+wine[i-1], dp[i-1])
print(dp[cnt])

## 최소 케이스에서 출력을 또 해버리는 실수 때문에 이틀 날려먹음 ㅁㅊ ; 
