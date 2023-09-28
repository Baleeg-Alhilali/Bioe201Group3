#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

def memory__alignment_score(sequence_1, sequence_2, indel_penalty=5): #performs sequence alignment between two strings, it calculates the alignment score while minimizing memory usage
    sequence_1 = '-' + sequence_1 #to handle gaps or insertions at the begining 
    sequence_2 = '-' + sequence_2
    current_row_alignment_score = [0] * len(sequence_1) #a list of zeros with a length equal to sequence_1, it will be used to store alignment scores for the current row
    for i in range(1, len(sequence_1)): #loop representing rows 
        current_row_alignment_score[i] = current_row_alignment_score[i - 1] - indel_penalty

    for j in range(1, len(sequence_2)): #we start from 1 because this represents the cost of inserting gaps at various positions in sequence_1 to align it with the first character of sequence_2.
        next_row_alignment_score = [-indel_penalty * j] * len(sequence_1) #same as the length of sequence_1 but the values are multiplied by the negative of indel penalty, it represents the cost of inserting gaps at different positions.
        for i in range(1, len(sequence_1)): #loop representing columns 
            if (sequence_1[i], sequence_2[j]) in BLOSUM62: #having a diagonal case, match or mismatch
                key = (sequence_1[i], sequence_2[j]) 
            else:
                key = (sequence_2[j], sequence_1[i])
            next_row_alignment_score[i] = max(current_row_alignment_score[i - 1] + BLOSUM62[key], next_row_alignment_score[i - 1] - indel_penalty, current_row_alignment_score[i] - indel_penalty) #the maximum of these three values is taken as the alignment score for the current cell, and it is stored.
        current_row_alignment_score = next_row_alignment_score #matrix is updated row by row to minimize memory usage

    #note that The diagonal value current_row_alignment_score[i - 1] (representing a match or mismatch of characters) plus the BLOSUM62 score for the pair of characters
    #the value to the left next_row_alignment_score[i - 1] (representing the cost of inserting a gap at sequence_1)
    #the value above current_row_alignment_score[i] (representing the cost of inserting a gap at sequence_2)
    
    
    return current_row_alignment_score #contains the alignment scores and can be used for traceback 

def middle_edge_linear_space(sequence_1, sequence_2, top_direction=0, bottom_direction=None, left_direction=0, right_direction=None): #finding the middle edge in the alignment graph of two input strings 
    if bottom_direction is None:
        bottom_direction = len(sequence_1) #if bottom is not provided, then it is given the galue of sequence_1
    if right_direction is None:
        right_direction = len(sequence_2) ##if right is not provided, then it is given the galue of sequence_2
    middle_column = (right_direction + left_direction) // 2 #calculating the middle column indexh
    from_source = memory__alignment_score(sequence_1[top_direction:bottom_direction], sequence_2[left_direction:middle_column]) # calculates the alignment scores from the top  to the middle column of the matrix
    to_sink = memory__alignment_score(sequence_1[top_direction:bottom_direction][::-1], sequence_2[middle_column:right_direction][::-1])[::-1] #calculates the score from the bottom of the reversed sequence_1 to middle_column of reversed sequence_2
    max_current_score = -1e6 #initialized with a very low value, it will be used to track the alignment score 
    for i in range(len(from_source)): #iterates over all elements in from_source 
        current_score = from_source[i] + to_sink[i] 
        if current_score > max_current_score: #if current score is greater than the maximum current score 
            max_current_score = current_score #this gets updated 
            index_1 = i #recording the index where the maximum score was achieved 
    from_source2 = memory__alignment_score(sequence_1[top_direction:bottom_direction], sequence_2[left_direction:middle_column + 1]) #we do the same thing as before but consider the next column 
    to_sink2 = memory__alignment_score(sequence_1[top_direction:bottom_direction][::-1], sequence_2[middle_column + 1:right_direction][::-1])[::-1] 
    max_current_score = -1e6
    for i in range(len(from_source2)):
        current_score = from_source2[i] + to_sink2[i]
        if current_score > max_current_score:
            max_current_score = current_score
            index_2 = i #we record it at index 2 for the second case 
            
        
    #determining the type of middle edge
    if index_2 == index_1 + 1:
        return 'diagonal', (index_1 + top_direction, middle_column), (index_1 + top_direction + 1, middle_column + 1) #we have a match in both strings 
    if index_2 == index_1:
        return 'horizontal', (index_1 + top_direction, middle_column), (index_1 + top_direction, middle_column + 1)
    return 'vertical', (index_1 + top_direction, middle_column), (index_1 + top_direction + 1, middle_column)


if __name__ == "__main__":
   
    
    sequence_1 = 'KHLKLFGKWPFGFRGCYSHYLLFWAGCPFRVWRKNMTRCLNCMGNEKFITHADCVCCDDEVRPYESDCVPKGKMKGITWPRGARRPMGCFDPEMMKNMDYISYWGWQKTFDISFPFRKMTVFTISCTHLEWAYPPWWFSHFPWCMERIMAVHWHKLGNPGGTAHKSVRCKHTYAIISWARCPPLQQTYCLVTMGCGYFTCAWQDHCWHPTVCMCSPTRLLTILPRRIPKPSYEYWHINIVEANFLTWGKYPFNGMACNMQPGNFIEPRVNRHRLEFIHWALPKSGSCVPVPIYHTFYMIPVSTPLCNKFIPIIIMSLVPECMIWHHCVQATMKYHLPNPLDMACECNHFTNRSPWHLMLVHGKDRYAHSGFPFCLLNLTYGCFFWRSVFRGWVWCAVAKEPDKSADGPLCVTLMCTDNFRFNHCSKRHMHATIMLHFVFMWAFIVSHSECNPMPWYNHYFTNAVSKQYGGYNLKGELHCGMNSVIFHMPAVFYSGTRIPLFYKDSLANAMECYIEGTHNVEQLTAHCAEIMIIFNQQMKYVEHRRWCHYNCALTRTDNDGCVPFHIRWCHAILVQADCAQIVHRWRDVKPIYKHIHTKPMPNRYLFWWDSSYVLLMCDQWAGMAWAALFWDSEIWNYEPDCCYLYLRQQQGFDGCQIIIDVRITHYVFVQYNFYSHYNKLMHMQQNECASPHKHPFRWGCELARPEFLKPVDVCSQMFMPGCKNEVFESLCMSYKHCKYRIMMTILHDKNVVQEWQPMAMYWNCADIKCVLLQDNMMKTIYDKYAETQDMNMKYLGDTMKTTVRKCCPNCDIMSWQHDMHGLRDRKLTTPFFVMGDAPAFCAHTADLADVSNCRWVCWHRKKQANNTQHQEYLEIHSFSDSWIRCDRADWPWPMGYGLRYILDCTGAKKPVDCIAHEYWSNALDEKIGWIPCGIFTALCHHIIIWRKNYIMKWSANRKNGTNRGHQNFFAQIPRPEDRPYPSDGVWHWVESTIMARRSPHSDESHRYRCRKPNVMYTLKIMQCEHFDKDSDNLAK'
    sequence_2 = 'ERHAGNKEKYRAKAIRVRESSWFLKEDHHCWMNPIGYNKNNHCTFYCGSGIFFPFKLPLVDESTEHYRFADQKGLTRAAIPNWAIIMTLCFLPIASDAETKSCIPAEMTWIAIWFFRRNYDYRAQFKVGAFALNSEWNDECYAYHQAVWVMEVGAVFIFVSWAKFMHRNAAAHPSDMYRFVQKTGCGGAVAPFEHHMELYCGKNFTADPSLSYQKLYLPYYEYLDLYYEDCCIKWHHGAMREQKILWTYCDKMTFQPSGKKSRWVHFAPVCVIETQCDLWLCNKSMLKSKWCKPWQCCDITWNPRFDSMYDYWKRISIVADPLRKFYKPVRKPPSSHAKSFASTPGDWIDLQMHMTEGPTQGFTMKTNSFTQDYCLKIFITAMLLGIMNAELAKHALMSEKPTPEMMTTSMGYHQCYRREKCFQPKARCQYAGIYYDQHNAEVHYWVRYKNPMPWYNHYFTNAVKGEMNDVIPQAHCMPAKIKVFIRCRDMCAWHLFYKILANAMFYHIYSCYIPGTHSVEQLTAIGHYACAEMMIFNQQMIDYKEHRRWCHYYNLNQALTRTDNDGCVPFIFPNDDSLVQTMWDRAQIVIYRWKVNNIVQWALIYDKQEVSRNYPRDKCLLEFLLNCKRPMGNWCYVTKEMMACKTVYCDNEHAWEDCECQKNVICGGWRAKEAPFRYNVLDVCTMLSHWKPYPHDYPTDSDMTEGTVIEAAHWVVSMNPTCMCIENSYDHAVPHEWECHQILVCKVEMRHTYASLYFLFTSFRRAYGHEQYPHVTIELRQVPGNACTYCEEWEAWNMCFQDTNMGMYSLMSRKVFEERQQFYSKDLMYVYCDLAHFFSKTNGACEMYMPANSCQYDNGQKWLENPRMIHLLFGPDDNAQFEMGKISRNKVFLTWTHGTRRIPGDMHCQARQMEGPHPPISSRQGGSPWDHFNHMDPTWINDMISGQWFWTSAVGIPPFSVLDKWGRTWSCSTGQYVGLAATGCGNRCRKGAWMYLTQPVIETRIIWKFCCGKVNNWFESCIMVCMMPTMLMAAGNEDDVCPGQ'
    
    _, middle_edge_from, middle_edge_to = middle_edge_linear_space(sequence_1, sequence_2) #_ determines the return value which can be discarded

    print(f"({middle_edge_from[0]}, {middle_edge_from[1]}) ({middle_edge_to[0]}, {middle_edge_to[1]})")


# In[ ]:




