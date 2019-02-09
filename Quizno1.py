import numpy as np
#import sys

s1 = input("Enter Word 1:")
s2 = input("Enter Word 2:")

insertion=int(input('Enter Insertion Cost: '))
deletion=int(input('Enter Deletion Cost: '))
substitution = insertion+deletion
s_matrix = np.ndarray(shape=(len(s1)+1,len(s2)+1), dtype=int)
s_matrix.fill(0)
bt_matrix = np.ndarray(shape=(len(s1)+1,len(s2)+1), dtype=int)
bt_matrix.fill(3)
for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i==0 and j==0:
                continue
            bs1 = s1[i-1] 
            bs2 = s2[j-1] 
            scores = [999,999,999]
            if i==0 and j > 0:
                scores[0]=j*insertion
            if j==0 and i > 0:
                scores[2]=i*deletion
            if j > 0 and i > 0:
                if bs1==bs2:
                    scores[1]=min(s_matrix[i-1,j-1]+0,s_matrix[i-1,j]+insertion,s_matrix[i,j-1]+deletion)
                if bs1 != bs2 and (s_matrix[i-1,j-1]+substitution) <= (s_matrix[i-1,j]+insertion) and (s_matrix[i-1,j-1]+substitution) <= (s_matrix[i,j-1]+deletion):
                    scores[1]=s_matrix[i-1,j-1]+substitution
                if bs1 != bs2 and (s_matrix[i-1,j]+insertion) <= (s_matrix[i,j-1]+deletion) and (s_matrix[i-1,j]+insertion) <= (s_matrix[i-1,j-1]+substitution):
                    scores[2]=s_matrix[i-1,j]+insertion
                if bs1 != bs2 and (s_matrix[i,j-1]+deletion) <= (s_matrix[i-1,j-1]+substitution) and (s_matrix[i,j-1]+deletion) <= (s_matrix[i-1,j]+insertion):
                    scores[0]=s_matrix[i,j-1]+deletion
            best = min(scores)
            s_matrix[i,j]=best
            for k in range(3):
                if scores[k] == best:
                    bt_matrix[i,j] = k
                    
print("Levenshtein Distance matrix:")
print(s_matrix)
print("\nBack pointers:")
print(bt_matrix)
align1 = ""
align2 = ""
i=len(s1)
j=len(s2)
while i>0 or j>0:
        if bt_matrix[i,j] == 0: 
            align1 += "-"
            align2 += s2[j-1]
            j -= 1
        if bt_matrix[i,j] == 1:
            align1 += s1[i-1]
            align2 += s2[j-1]
            i -= 1
            j -= 1
        if bt_matrix[i,j] == 2:
            align1 += s1[i-1]
            align2 += "-"
            i -= 1
align1 = align1[::-1]
align2 = align2[::-1]
print("\nAlignment:")
print(align1)
print(align2)
print("Best Score: ",s_matrix[len(s1)][len(s2)])