s = raw_input()
p = raw_input()

a = [-1]*2100

for i in xrange(len(s)):
    j = i
    for k in xrange(len(p)):
        while j<len(s) and s[j]!=p[k]:
            j += 1
        if j==len(s):
            break
        else:
            j += 1
    if (k == len(p)-1 and len(p)>1) or (len(p)==1 and s[i]==p):
        a[i]=j-i
    else:
        a[i]=-1


d = [[0 for i in xrange(2100)]for j in xrange(2100)]

for i in xrange(len(s)):
    for j in xrange(i+1):
        d[i+1][j]=max(d[i+1][j], d[i][j])
        d[i+1][j+1]=max(d[i+1][j+1],d[i][j])
        if a[i]>=0:
            d[i+a[i]][j+a[i]-len(p)]=max(d[i][j]+1,d[i+a[i]][j+a[i]-len(p)])

for i in xrange(len(s)):
    print d[len(s)][i],
print d[len(s)][len(s)]
###  time limit exceded


