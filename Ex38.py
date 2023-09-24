def Revpath(A,B):
    # add a space infron each segment to avoid error indexing
    A = '-'+A
    B = '-'+B
    n = len(A)
    m = len(B)
    # n*m matrix initialize at 0 that represent the score all nodes in the DAG
    score=[[0 for mm in range(m)] for mm in range(m)]
    # n*m matrix initialize at 0 that represent all dirications nodes in the DAG
    path= [["dir" for mm in range(m)] for nn in range(n)]
    # for loop that goes from(1,1) to (n,m) one by one and check which dir has the highest weight
    # record the path of the highest weight it found
    for i in range(1,n):
        for j in range(1,m):
            x = score[i-1][j-1]+ (1 if A[i]==B[j] else 0 )
            score[i][j]=max(x,score[i][j-1],score[i-1][j])
            if score[i][j] == score[i-1][j]:
                path[i][j] = "up"
            elif score[i][j]== score[i][j-1]:
                path[i][j] = "left"
            else:
                path[i][j]="dig"
    # now we just need to reconstruct the string of the path from (n,m) to (1,1)
    seq = ""
    n-=1
    m-=1
    while n > 0 and m > 0:
        if path[n][m] == "dig":
            seq = A[n]+seq
            n -=1
            m -=1
        elif path[n][m]=="up":
            n-=1
        else:
            m-=1
    return seq






if __name__ == "__main__":


    A ="ACAATCAAACTTGGGCCCCGGCAGGCACATAGTTAAAGGTATACGGAGAGACAGGTCAACCCTTCTGTTTTGTTCACATGGCTATTACTCACAACCTCTGGCCCAGATCTAGCAGGACTGATGTGCCAGACGCGATTGCCGATATAAACTATATGTCGTCGACACCTCGAATATTAAAAATACGGAAAACAACTAGCCAGCCTCCCTCGAGAAGGTGACTTATAAGCGCATATCCGGGGGTCACGGCTTCCTCCGAAGTCTGGGAGGTCACCTCACAAAGAGTGTCTGGCTCTTCTAATGTGCTCACCACTTCGCCTAGAAGTAAGACTTAATCTTTTGGACACCATGTGATAATTGATCACAAGTTAGTAATCAAAAGGTCAGATGGTCCAGTCCAGACTAGTACCATGTAGGGTATCATGGAGCACGGACTTTAGCCTAATGCACCCTTTTCGTGCCTCCTGATGGCCCATGTAGCTGGATAGCCCGATGGGGTTGGCGACACAGTTACATTATCGAAGATCCCACCATATTAACCAAGAGAAAGTCGAGTGGTTTGCTCACTTAACGACTTGTCGTCGTGAGTAATACGTGTCTCTAAACCACTGTTGGGTCGATTGAAGTACCCGCTGATGGGTATCGCAGAAAGAAATACGTAACTGGGCAAGCGTCGCCATGCGCCCCTAGATCGGTGAGGTGGCTCTCCCTAATGTTTCGCTCGCTGAATTTTGGCGTGTGAGGCCTAAAACACACGTGGGGCAGGGATTGGCCCTGATCATTTTGATAGGTGAGCCCAAAGCTGAGCAATGACTTTCATTGAGTGGCATGACGTTGGCAGGCGTGGAAACTGACTTGTGCTTGTCCCTATCATAAGAACAGGGGGCGAGGACTTAACGCGTCATCGCAGCTCCGTGAGGGTAGATAATGCAG"
    B ="GAACCTGATGCAAACGAACCCAATTTAGAGCATCTGCTGGATAGTGGAGCTCCGCTTTGTTCCGGGGGGGGCAGAACTTGGTTATTAAGCTCGAGTTAGTAATCGACGGCTCCAGTGCGATCCAACTATCTTACGTCGCCGCTCTCGCTACCGAGTCATGCCCCGACTATCGGAGGGCTTTGATTGTAGTTCCAGCAGATGAACTGCGGAAAAAAATGATCAGGTATTGCTGGGGTTTAATTGTAAAGTCGACGGTAGCTCCTGGTGTTGGCATAGTCATTTGCGGAGAGGCCACACCTCGGTTCCCGAATTATTGTTAGAGGAATAGAATACTGATCTGCATGAAATCTATGCAAGGGTAAGGATACCTGAGGCGTTCGACGGTATATGATACCATCTACCAAGTCCTTATGCGTGAGGATCCGGGATATAGCTTATTCTAAAACCGAAATAGAATTGCCAACCCAGAGAAGGGGCGTCCGCCGGGATATAGGTCAGCGGGTTTCACCTTAGCCGAGGAACGAACTTCTGCAGCCACTAGGCGATGCGTTCAGCACGAGATCCGGCAGGGGATGACATTGCTCTGACGTTCCGAGTGGGTAAGTCAGCCCGAGCAGGAGCTATTGCCACTCCGAGCCTGACGCGCAGCCCTTTTAATCTTTTCGCAAGTGTGGTTCCTATCATGCCGTGCTAAGTCTACGTTTCATAGCGCCTAAGGGAGGTTGCGGGTTGTTAATGTGGAGTAGCAGCGCTTGGATGGAGTTCCCGATTCGGAGGTACTCTCAACGTGTCGCTACCGGTGACCGCTGGACATTAGCTCATAGTTGCTGAGAGCTGGTCAGAGGGGCAGAACAGCGGTCAGCAATGTGGCCTCTCGAGACTGACCGATCTATGTCAGGTGCGAACGCGGGCCTAATTGTATCGTTTGATCATTTATACATG"
    ansR = Revpath(A,B)
    print(ansR)