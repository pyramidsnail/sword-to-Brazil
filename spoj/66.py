test = int(raw_input())
girl = [int(x) for x in raw_input().lstrip('0').split()]
line=raw_input()
while test:
    test -=1
    while line!='0':
        score=0
        boy = [int(x) for x in line.lstrip('0').split()]
        dp=[[0 for x in xrange(2100)] for x in xrange(2100) ]
        dp[0][0]=1
        for i in xrange(len(girl)):
            for j in xrange(len(boy)):
                if i==0 or j==0:
                    dp[i][j]=1
                if boy[j]==girl[i]:
                    dp[i][j] = dp[i-1][j-1]+1
        if dp[len(girl)-1][len(boy)-1]>score:
            score=dp[len(girl)-1][len(boy)-1]

        line=raw_input()
    print score     
