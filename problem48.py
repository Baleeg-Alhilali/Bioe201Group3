{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b07ea831",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "--TTA---AGT--GAT-----AGCCGGAGC--TA-CA------GAT-----GC\n",
      "----ACGC--T----T-TCTGA-CC----C-CTA--ACTCCGT-AT-------\n",
      "CG--A-----TAA--TC----A-CC----CA-TAT-A-------ATCAGCC--\n"
     ]
    }
   ],
   "source": [
    "def find_longest_common_subsequence(str1, str2, str3):\n",
    "    # Initialize the dimensions of the dynamic programming table for memoization.\n",
    "    len_str1 = len(str1)  # Length of the first input string.\n",
    "    len_str2 = len(str2)  # Length of the second input string.\n",
    "    len_str3 = len(str3)  # Length of the third input string.\n",
    "\n",
    "    # Create a 3D table (dp) to store the scores and alignment information.\n",
    "    # dp[i][j][k] will represent the length of the longest common subsequence of\n",
    "    # the first i characters of str1, the first j characters of str2, and the\n",
    "    # first k characters of str3.\n",
    "    dp = [[[0] * (len_str3 + 1) for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]\n",
    "\n",
    "    # Create a table (alignment) to store information about the alignment.\n",
    "    # alignment[i][j][k] will be '1' if characters str1[i-1], str2[j-1], and str3[k-1]\n",
    "    # are part of the longest common subsequence, or '0' if they are not.\n",
    "    alignment = [[['0'] * (len_str3 + 1) for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]\n",
    "\n",
    "    # Fill in the dynamic programming table (dp) and alignment information.\n",
    "    for i in range(1, len_str1 + 1):\n",
    "        for j in range(1, len_str2 + 1):\n",
    "            for k in range(1, len_str3 + 1):\n",
    "                if str1[i - 1] == str2[j - 1] == str3[k - 1]:\n",
    "                    # If the current characters in all three strings match, extend the LCS.\n",
    "                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1\n",
    "                    alignment[i][j][k] = '1'  # '1' represents alignment\n",
    "                else:\n",
    "                    # If characters do not match, update dp based on the previous values.\n",
    "                    if dp[i - 1][j][k] >= dp[i][j - 1][k] and dp[i - 1][j][k] >= dp[i][j][k - 1]:\n",
    "                        dp[i][j][k] = dp[i - 1][j][k]\n",
    "                        alignment[i][j][k] = '0'  # '0' represents a gap in the alignment\n",
    "                    elif dp[i][j - 1][k] >= dp[i][j][k - 1]:\n",
    "                        dp[i][j][k] = dp[i][j - 1][k]\n",
    "                        alignment[i][j][k] = '0'  # '0' represents a gap in the alignment\n",
    "                    else:\n",
    "                        dp[i][j][k] = dp[i][j][k - 1]\n",
    "                        alignment[i][j][k] = '0'  # '0' represents a gap in the alignment\n",
    "\n",
    "    # Initialize variables to store the alignment and maximum score.\n",
    "    i = len_str1\n",
    "    j = len_str2\n",
    "    k = len_str3\n",
    "    aligned1 = ''  # Store the aligned characters from str1.\n",
    "    aligned2 = ''  # Store the aligned characters from str2.\n",
    "    aligned3 = ''  # Store the aligned characters from str3.\n",
    "\n",
    "    # Backtrack to reconstruct the alignments.\n",
    "    while i > 0 or j > 0 or k > 0:\n",
    "        if i > 0 and j > 0 and k > 0 and alignment[i][j][k] == '1':\n",
    "            # If the characters are part of the LCS, add them to the aligned strings.\n",
    "            aligned1 = str1[i - 1] + aligned1\n",
    "            aligned2 = str2[j - 1] + aligned2\n",
    "            aligned3 = str3[k - 1] + aligned3\n",
    "            i -= 1\n",
    "            j -= 1\n",
    "            k -= 1\n",
    "        else:\n",
    "            if i > 0 and j > 0 and k > 0:\n",
    "                # If characters are not part of the LCS, backtrack to find the direction\n",
    "                # with the maximum score and add gaps accordingly.\n",
    "                max_val = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])\n",
    "                if max_val == dp[i - 1][j][k]:\n",
    "                    aligned1 = str1[i - 1] + aligned1\n",
    "                    aligned2 = '-' + aligned2\n",
    "                    aligned3 = '-' + aligned3\n",
    "                    i -= 1\n",
    "                elif max_val == dp[i][j - 1][k]:\n",
    "                    aligned1 = '-' + aligned1\n",
    "                    aligned2 = str2[j - 1] + aligned2\n",
    "                    aligned3 = '-' + aligned3\n",
    "                    j -= 1\n",
    "                else:\n",
    "                    aligned1 = '-' + aligned1\n",
    "                    aligned2 = '-' + aligned2\n",
    "                    aligned3 = str3[k - 1] + aligned3\n",
    "                    k -= 1\n",
    "            else:\n",
    "                if i > 0:\n",
    "                    aligned1 = str1[i - 1] + aligned1\n",
    "                    aligned2 = '-' + aligned2\n",
    "                    aligned3 = '-' + aligned3\n",
    "                    i -= 1\n",
    "                elif j > 0:\n",
    "                    aligned1 = '-' + aligned1\n",
    "                    aligned2 = str2[j - 1] + aligned2\n",
    "                    aligned3 = '-' + aligned3\n",
    "                    j -= 1\n",
    "                else:\n",
    "                    aligned1 = '-' + aligned1\n",
    "                    aligned2 = '-' + aligned2\n",
    "                    aligned3 = str3[k - 1] + aligned3\n",
    "                    k -= 1\n",
    "\n",
    "    # Return the maximum score and the aligned strings.\n",
    "    return dp[len_str1][len_str2][len_str3], aligned1, aligned2, aligned3\n",
    "\n",
    "\n",
    "# Example usage:\n",
    "str1 = \"TTAAGTGATAGCCGGAGCTACAGATGC\"\n",
    "str2 = \"ACGCTTTCTGACCCCTAACTCCGTAT\"\n",
    "str3 = \"CGATAATCACCCATATAATCAGCC\"\n",
    "score, aligned1, aligned2, aligned3 = find_longest_common_subsequence(str1, str2, str3)\n",
    "print(score)\n",
    "print(aligned1)\n",
    "print(aligned2)\n",
    "print(aligned3)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6f93b07",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}