# I had to use the np libary to import the data from the text

import numpy as np

def Longestpath(n,m,down,right):
    score = [[0 for mm in range(m+1)]for nn in range(n+1)]
    # the route from the source to bottom of the first colum
    for S in range(1,n+1):
        score[S][0]=score[S-1][0]+down[S-1][0]
    # the route from the source to the right of the first row
    for W in range(1,m+1):
        score[0][W]=score[0][W-1]+right[0][W-1]
    # now we can fill the rest of the DAG
    for i in range(1,n+1):
        for j in range(1,m+1):
            score[i][j]=max(score[i][j-1]+right[i][j-1],score[i-1][j]+down[i-1][j])
    ans = score[n][m]
    return ans

if __name__ == "__main__":
    n = np.loadtxt( 'rosalind_ba5b.txt',max_rows=1,dtype=int)[0]
    m = np.loadtxt( 'rosalind_ba5b.txt',max_rows=1,dtype=int)[1]
    down = np.loadtxt( 'rosalind_ba5b.txt',max_rows=n,skiprows=1,dtype=int)
    right = np.loadtxt( 'rosalind_ba5b.txt', skiprows=n+2,dtype=int)
    ans = int(Longestpath(n,m,down,right))
    print(n)
    print(m)
    print(ans)