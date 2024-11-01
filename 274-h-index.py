"""
Given an array of integers citations where citations[i] is the number of citations
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as 
the maximum value of h such that the given researcher has published at least h papers 
that have each been cited at least h times.
 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them 
had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two
with no more than 3 citations each, their h-index is 3.


Example 2:

Input: citations = [1,3,1]
Output: 1
"""

"""
[6,5,3,1,0]

i = 0; numCit = 6; numArt = 1 (i+1) | h = 1 && 6 > i + 1
i = 1; numCit = 5; numArt = 2 (i+1) -> Existem 2 artigos com pelo menos 5 citações | h = 2 && 5 > i + 1
i = 2; numCit = 3; numArt = 3 (i+1) | h = 3 && 3 == i + 1
i = 3; numCit = 1; numArt = 4 (i+1) | 1 < i + 1, ou seja, numCit < i + 1
"""

def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

citations1 = [3, 0, 6, 1, 5]
print(hIndex(citations1))