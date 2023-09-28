#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Finding a highest-scoring overlap alignment of two strings 

def overlap_alignment (sequence_1, sequence_2):
    sequence_1='-'+sequence_1 #also known as v, -to create space for potential gaps
    sequence_2='-'+sequence_2 #also known as w
    
    score_matrix=[[0 for j in range(len(sequence_2))] for i in range(len(sequence_1))] #at the whole length of string 1 we have 0 for j
    backtrack_matrix=[[None for j in range(len(sequence_2))] for i in range(len(sequence_1))] #at the whole length of string 1 we have no direction for j
    
    #penalty is 1 if we have a match 
    #penalty is -2 if we have an mismatch/indel
    
    for j in range(1, len(sequence_2)): 
        score_matrix[0][j]=score_matrix[0][j-1]-2 #applying the penalty 2 at point(0,j-1)
        backtrack_matrix[0][j]='left' #the direction is left between (i,j-1) and (i,j)
        
    for i in range(1,len(sequence_1)): #comparing between both strings here
        for j in range(1, len(sequence_2)):
            #scoring_matrix cases
            case_1=score_matrix[i-1][j-1]+(1 if sequence_1[i]==sequence_2[j] else -2) #our case is looking for a match, we add 1 if we find it and we subtract 2 if we don't (penalties)
            case_2=score_matrix[i-1][j] -2 #applying the penalty -2 if we have an indel at (i-1,j)
            case_3=score_matrix[i][j-1] -2 #applying the penalty -2 if we have an indel at (i,j-1)
            
            #back_track matrix cases
            score_matrix[i][j]=max(case_1,case_2,case_3) #highest score
            if score_matrix[i][j]==case_1:
                backtrack_matrix[i][j]='diagonal' #if both sequences are equal we go diagonaly
                
            elif score_matrix[i][j]==case_2:
                backtrack_matrix[i][j]='upwards'#the direction is upwards between (i,j-1) and (i,j)
                
            elif score_matrix[i][j]==case_3:
                backtrack_matrix[i][j]='left'   #the direction is left between (i,j-1) and (i,j)
      
    
    i=len(sequence_1)-1 #the whole sequence, -1 as the last point
    j=max(range(len(sequence_2)), key=lambda x:score_matrix[i][x]) #key is used to determine the maximum value in the range, based on score_matrix[i][j]
    #j represents the index where the maximum value in score_matrix[i][j] is found
    maximum_score=score_matrix[i][j]
    
    #back_track
    
    alignment_case1=''
    alignment_case2=''
    while backtrack_matrix[i][j] is not None:
        direction=backtrack_matrix[i][j]
        if direction=='diagonal': #the case where we have a match
            alignment_case1=sequence_1[i]+ alignment_case1
            alignment_case2=sequence_2[j]+ alignment_case2
            i-=1
            j-=1
            
        elif direction=='upwards': #the case where we have an indel(specifically a deletion)
            alignment_case1=sequence_1[i]+ alignment_case1
            alignment_case2='-'+ alignment_case2
            i-=1
            
        elif direction=='left':#the case where we have an indel(specifically an insertion)
            alignment_case1='-'+ alignment_case1
            alignment_case2=sequence_2[j]+ alignment_case2
            j-=1
        
        
    return maximum_score,alignment_case1,alignment_case2

#Main Function
if __name__=='__main__':
    
    sequence_1='GCACGCCCTATGGCAGGAGGGATCAACCTGATATGCGCCGTCTCAGGGCCTTGTGGTAGAGACGTACGTCTTAACCAATGGGGGATACTACGTCTGGTGACTCTCAAACTTTCTGTAGGCATAGCTACTAAGCCCGCTAATTTAGCCCCGGTGGATTACTCACGCAGGTGCTCCCCGCCAGTAAGAGAATTCGGCTTATACATAATTCTACTGTTTTAGTCATCGCGGGGGGATCATCCTAGTCACTAATCATACCATATCCCGGTTCGCGTTATGCGTACTCGCTGACTGGAATGGCTATGTACGCCAATGCCTTTGGATATGATAGTTTGCGACAACGACAAGTCACCGTTTAAAACTTTCATTTTTACTCGGATGAGCTGGCGCCAATCCTCTCGTGGAGACCAGCAGAATTAGAGCGCTCGAACGCTTTACTTTGTCGGTCGGGAGAGACTCTATTATTGCATAAGCTAGCTTAAACTACGCCGCTGGTCTCTTGCATGCTCTAAACGATTCTAGCCTATGCGGACGTCCAGCCGCGTCAGGACCACCTGCACGGTCACTAATTAATTTACTCCTGAAGTTGCCTGTGCCCGGACATGCAAAGTGAACGAACTATTGTTGATAACCAAGTTTCATCTAGACGGCGTGCGGGTCGTCAAAAAAATAGTGAAAGCCATTCCTTATCATGTGTTCTCTACTACGCGCCAACGGGAGAGTCACGCGTCGGGTTCGGAGTGATCAATATCACTCCTCAAACAATATTGGACAGAACGCTACAACCCACTCCTTGATCCTAGGGCGCCCATCCGGTGGCAAGATCCAGAGTTGGGTGGTCGTTCTTAAGGGGTCGAAAATG'
    sequence_2='ACGGACTGATCGTTGATCCAAGTATCTCTAGCCGTGCGGCGGGCCTTTAAAAAAATAGAGCGAGAACTCAGTCCGTGACCATGTTTCTTTTTACAACTCAGCTGAAGTCACAGCCGTCGAGTCGAGTCAGCAAAATCCACTCCGCAAACAATATGGGACGACTACCGCAACACATCCCGTTGATCCTAGACGCATCGCCACCCGGTATCAGATCCGGAACGTGGGCGGCGGTTCTTTAGTGTGCTGAAACGCGGAAAGGGATCAGAGAAGATCCGCGCCGGGCGCTTCCGTTCTAGTGTTGTGTCAATGAACAGAGGGTCGGCACTATGGTACCGATGTTTCCCTTTCTCATTAATGACGTGGTTTGTACAGCCTGTTTCGACAAGGCGCATTGGCTTCCTGCACCGCATCGCGGCAACTGTTCTGACTCCTTGCCACAGCTCGAAACAAGTCCCTCCGAGTCCTTGCACAGCAGGGGCCGGAAACGTCGAATTCCGGTAGCAATATCATCTCCCCGTTAGTCAATCGGACTCCGCTTATCAACGTGGTCTATTGCTGGCGGCTTTTAGCAAGTTTCCCCCGCATGCGCTAGTGTCCCGAACCTGTCCACAAGCGCCCGTTGGTAATATGACCAATACGTTTCATTCACTTTCGACGCCCCCGATTGAACCTTGAATAACACTCCGGGTAAGGTATTTCCGAGAGTTCTCGAATGGGCTTAAAACGTTGAAGAGTGGGCTACTCTAGAGTCGGATTGCAGCCGTTAATGCCAGGCCAAATCGCGCATCGCTTTATATTTCAAGACCTGCTTTCGGGCGTGTGGTTATACGCAATATACGTCCGATTGCACTATACATTCCATTTGGTCCTTAAGGTGACAAAGCTACAATAATAACGTCGGGCAAGACCCAAATACAACCGCTTCGGCCGGCCGTAGTCCTAGCATTTGAAGGCTACCTTCAAGAC'


    score,alignment1,alignment2=overlap_alignment(sequence_1,sequence_2)
    
    print(score)
    print(alignment1)
    print(alignment2)


            
                
                
            
            
    
    


# In[ ]:





# In[ ]:




