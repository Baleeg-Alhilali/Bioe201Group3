#!/usr/bin/env python
# coding: utf-8

# In[1]:



#this matrix is used to assign scores between pairs of amino acids
BLOSUM62 = {
    ('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
    ('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
    ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
    ('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
    ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
    ('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
    ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
    ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
    ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
    ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
    ('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
    ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
    ('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
    ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
    ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
    ('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
    ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
    ('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
    ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
    ('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
    ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
    ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
    ('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
    ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
    ('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
    ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
    ('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
    ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
    ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
    ('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
    ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
    ('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
    ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
    ('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
    ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
    ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
    ('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
    ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
    ('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
    ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
    ('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
    ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
    ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
    ('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
    ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
    ('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
    ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
    ('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
    ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
    ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
    ('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
    ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
    ('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
    ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
    ('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
    ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
    ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
    ('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
    ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
    ('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
    ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
    ('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
    ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
    ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
    ('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
    ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
    ('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
    ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
    ('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
}

def alignment_strings_using_affine_gap(v,w,gap_opening_penalty=11,gap_extension_penalty=1): 
    #v and w are input amino acids to be aligned
    v='-'+v #this is done to represent the gaps at the begining of the alignment, create space for potential gaps 
    w='-'+w

    
    #These 2D matrices are initialized to store scores during the alignment process. The matrices show the upper, middle, and lower layers of the DAG algorithm
    upper_layer = [[0 for j in range(len(w))] for i in range(len(v))] #starting from 0 to all lengths of v and w
    middle_layer = [[0 for j in range(len(w))] for i in range(len(v))]
    lower_layer = [[0 for j in range(len(w))] for i in range(len(v))]
    
    middle_layer[1][0] = -gap_opening_penalty #at node 1,0 (beginning of the v sequence at row 1, column 0)
    middle_layer[0][1] = -gap_opening_penalty #at node 0,0 (beginning of the w sequence at row 0, column 1)

    #initialization step for the middle layer
    for i in range(2, len(middle_layer)): #starting from 2 because the first 2 rows have already been initialized with gap opening penalties 
        middle_layer[i][0] = middle_layer[i - 1][0] - gap_extension_penalty #extension with cost
    for j in range(2, len(middle_layer[0])): #starting from 2 because the first 2 columns have already been initialized with gap opening penalties 
        middle_layer[0][j] = middle_layer[0][j - 1] - gap_extension_penalty #extension with cost
        
    #initialization steps for the upper and lower layers
    for j in range(len(lower_layer[0])):
        lower_layer[0][j] = -1e6 #to discourage gap openings at the beggining of sequence w, we set it to a very large negative value 
    for i in range(0, len(lower_layer)):
        lower_layer[i][0] = middle_layer[i][0] #lower represents gap extensions in sequence v and since there are no in the beginning it takes the value of the middle layer at that point
    for i in range(len(upper_layer)):
        upper_layer[i][0] = -1e6 #to discourage gap openings at the beggining of sequence v, we set it to a very large negative value 
    for j in range(0, len(upper_layer[0])):
        upper_layer[0][j] = middle_layer[0][j] #lower represents gap extensions in sequence w and since there are no in the beginning it takes the value of the middle layer at that point
    
    #initialization steps for backtracking, stores information about direction
    backtrack_middle = [['diagonal' for j in range(len(w))] for i in range(len(v))] #we go diagonally 
    backtrack_lower = [['upward' for j in range(len(w))] for i in range(len(v))] #we go vertically
    backtrack_upper = [['leftward' for j in range(len(w))] for i in range(len(v))] #we go horizontally

    for i in range(len(backtrack_middle)):
        backtrack_middle[i][0] = 'upward' #connected to the lower matrix
    for j in range(len(backtrack_middle[0])):
        backtrack_middle[0][j] = 'leftward' #connected to the upper matrix

    for j in range(len(backtrack_lower[0])):
        backtrack_lower[0][j] = 'leftward' #connected to the upper matrix at the j component
    for i in range(len(backtrack_upper)):
        backtrack_upper[i][0] = 'upward' #the i component is upward

    backtrack_middle[0][0] = None #at point 0,0 we have no direction while backtracking for the middle layer
    backtrack_lower[0][0] = None #at point 0,0 we have no direction while backtracking for the lower layer
    backtrack_upper[0][0] = None #at point 0,0 we have no direction while backtracking for the upper layer
    

    for i in range(1, len(v)): #iterating through all cells except the first row because it represents the starting point for gap extensions
        for j in range(1, len(w)): #iterating through all cells except the first column because it represents the starting point for gap extensions
            
            # lower layer case, score is collected by considering the gap expension and gap opening scenarios which are stored in the lower_layer matrix, we take the max of these scores
            lower_layer[i][j] = max(lower_layer[i - 1][j] - gap_extension_penalty, middle_layer[i - 1][j] - gap_opening_penalty)
            if lower_layer[i][j] == lower_layer[i - 1][j] - gap_extension_penalty: 
                backtrack_lower[i][j] = 'upward'
            else:
                backtrack_lower[i][j] = 'diagonal' #if the case above doesn't exist we have a match
                
            # upper layer case
            upper_layer[i][j] = max(upper_layer[i][j - 1] - gap_extension_penalty, middle_layer[i][j - 1] - gap_opening_penalty)
            if upper_layer[i][j] == upper_layer[i][j - 1] - gap_extension_penalty:
                backtrack_upper[i][j] = 'leftward'
            else:
                backtrack_upper[i][j] = 'diagonal' #if the case above doesn't exist we have a match
                
            # middle layer case, we calculate the score of a diagonal movement
            if (v[i], w[j]) in BLOSUM62: #we check if it's in this scoring matrix
                key = (v[i], w[j])
            else:
                key = (w[j], v[i]) #if not we look up this score
            diagonal_direction = middle_layer[i - 1][j - 1] + BLOSUM62[key] #we add the blosum62 score to the old cell
            middle_layer[i][j] = max([diagonal_direction, upper_layer[i][j], lower_layer[i][j]])

            if middle_layer[i][j] == diagonal_direction: #here we update the direction matrix
                backtrack_middle[i][j] = 'diagonal'
            elif middle_layer[i][j] == lower_layer[i][j]:
                backtrack_middle[i][j] = 'upward'
            else:
                backtrack_middle[i][j] = 'leftward'
                
    #traceback step after the calculations            
    i = len(backtrack_middle) - 1 
    j = len(backtrack_middle[0]) - 1
    aligning_traceback1 = ''
    aligning_traceback2 = ''
    layer = 'middle' #we start tracback from the middle_layer matrix
    while backtrack_middle[i][j] is not None: #it continues as long as we did not reach the top left corner
        if layer == 'middle': #starting at the middle layer
            if backtrack_middle[i][j] == 'diagonal': #we came from a diagonal move
                aligning_traceback1 = v[i] + aligning_traceback1
                aligning_traceback2 = w[j] + aligning_traceback2
                i -= 1
                j -= 1
            elif backtrack_middle[i][j] == 'upward': #we came from an upward move in the lower matrix
                layer = 'lower'
            else:
                layer = 'upper'

        elif layer == 'lower': #then the lower layer, focuses on i 
            if backtrack_lower[i][j] == 'upward':
                aligning_traceback1 = v[i] + aligning_traceback1
                aligning_traceback2 = '-' + aligning_traceback2
                i -= 1
            elif backtrack_lower[i][j] == 'diagonal':
                aligning_traceback1 = v[i] + aligning_traceback1
                aligning_traceback2 = '-' + aligning_traceback2
                i -= 1
                layer = 'middle'
            else:
                layer = 'middle'

        elif layer == 'upper': #then the upper layer, focuses on j 
            if backtrack_upper[i][j] == 'leftward':
                aligning_traceback1 = '-' + aligning_traceback1
                aligning_traceback2 = w[j] + aligning_traceback2
                j -= 1
            elif backtrack_lower[i][j] == 'diagonal':
                aligning_traceback1 = '-' + aligning_traceback1
                aligning_traceback2 = w[j] + aligning_traceback2
                j -= 1
                layer = 'middle'
            else:
                layer = 'middle'

    return middle_layer[len(v) - 1][len(w) - 1], aligning_traceback1, aligning_traceback2            
                
     
if __name__ == "__main__":
 
    sequence1 = 'GFRDRMSAFSARAGGWPAENWEITHNDAQICHKLEHYMIENCMAKGWAEAFWRKALSAVCVFKIEFKDCIAGEQP'

    sequence2 = 'GFCDRMSAFSARAGGWPAENWEITHNDYGKVAQELEAMVHKLEHYMIENCLAKGWARAFWRKALSPVCVFKIGFKDCIAGEQD'

    score, aligning_traceback1, aligning_traceback2 = alignment_strings_using_affine_gap(sequence1, sequence2)
    print(score)
    print(aligning_traceback1)
    print(aligning_traceback2)


# In[ ]:




