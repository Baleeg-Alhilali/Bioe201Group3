#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_longest_common_subsequence(str1, str2, str3):
    # Initialize the dimensions of the dynamic programming table for memoization.
    len_str1 = len(str1)  # Length of the first input string.
    len_str2 = len(str2)  # Length of the second input string.
    len_str3 = len(str3)  # Length of the third input string.

    # Create a 3D table (dp) to store the scores and alignment information.
    # dp[i][j][k] will represent the length of the longest common subsequence of
    # the first i characters of str1, the first j characters of str2, and the
    # first k characters of str3.
    dp = [[[0] * (len_str3 + 1) for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

    # Create a table (alignment) to store information about the alignment.
    # alignment[i][j][k] will be '1' if characters str1[i-1], str2[j-1], and str3[k-1]
    # are part of the longest common subsequence, or '0' if they are not.
    alignment = [[['0'] * (len_str3 + 1) for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

    # Fill in the dynamic programming table (dp) and alignment information.
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            for k in range(1, len_str3 + 1):
                if str1[i - 1] == str2[j - 1] == str3[k - 1]:
                    # If the current characters in all three strings match, extend the LCS.
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    alignment[i][j][k] = '1'  # '1' represents alignment
                else:
                    # If characters do not match, update dp based on the previous values.
                    if dp[i - 1][j][k] >= dp[i][j - 1][k] and dp[i - 1][j][k] >= dp[i][j][k - 1]:
                        dp[i][j][k] = dp[i - 1][j][k]
                        alignment[i][j][k] = '0'  # '0' represents a gap in the alignment
                    elif dp[i][j - 1][k] >= dp[i][j][k - 1]:
                        dp[i][j][k] = dp[i][j - 1][k]
                        alignment[i][j][k] = '0'  # '0' represents a gap in the alignment
                    else:
                        dp[i][j][k] = dp[i][j][k - 1]
                        alignment[i][j][k] = '0'  # '0' represents a gap in the alignment

    # Initialize variables to store the alignment and maximum score.
    i = len_str1
    j = len_str2
    k = len_str3
    aligned1 = ''  # Store the aligned characters from str1.
    aligned2 = ''  # Store the aligned characters from str2.
    aligned3 = ''  # Store the aligned characters from str3.

    # Backtrack to reconstruct the alignments.
    while i > 0 or j > 0 or k > 0:
        if i > 0 and j > 0 and k > 0 and alignment[i][j][k] == '1':
            # If the characters are part of the LCS, add them to the aligned strings.
            aligned1 = str1[i - 1] + aligned1
            aligned2 = str2[j - 1] + aligned2
            aligned3 = str3[k - 1] + aligned3
            i -= 1
            j -= 1
            k -= 1
        else:
            if i > 0 and j > 0 and k > 0:
                # If characters are not part of the LCS, backtrack to find the direction
                # with the maximum score and add gaps accordingly.
                max_val = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
                if max_val == dp[i - 1][j][k]:
                    aligned1 = str1[i - 1] + aligned1
                    aligned2 = '-' + aligned2
                    aligned3 = '-' + aligned3
                    i -= 1
                elif max_val == dp[i][j - 1][k]:
                    aligned1 = '-' + aligned1
                    aligned2 = str2[j - 1] + aligned2
                    aligned3 = '-' + aligned3
                    j -= 1
                else:
                    aligned1 = '-' + aligned1
                    aligned2 = '-' + aligned2
                    aligned3 = str3[k - 1] + aligned3
                    k -= 1
            else:
                if i > 0:
                    aligned1 = str1[i - 1] + aligned1
                    aligned2 = '-' + aligned2
                    aligned3 = '-' + aligned3
                    i -= 1
                elif j > 0:
                    aligned1 = '-' + aligned1
                    aligned2 = str2[j - 1] + aligned2
                    aligned3 = '-' + aligned3
                    j -= 1
                else:
                    aligned1 = '-' + aligned1
                    aligned2 = '-' + aligned2
                    aligned3 = str3[k - 1] + aligned3
                    k -= 1

    # Return the maximum score and the aligned strings.
    return dp[len_str1][len_str2][len_str3], aligned1, aligned2, aligned3


# Example usage:
str1 = "TTAAGTGATAGCCGGAGCTACAGATGC"
str2 = "ACGCTTTCTGACCCCTAACTCCGTAT"
str3 = "CGATAATCACCCATATAATCAGCC"
score, aligned1, aligned2, aligned3 = find_longest_common_subsequence(str1, str2, str3)
print(score)
print(aligned1)
print(aligned2)
print(aligned3)


# In[ ]:




