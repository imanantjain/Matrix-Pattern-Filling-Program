# -*- coding: utf-8 -*-
"""
@author: Anant
"""

def outerChkmyMatrix(passmat, strVal, PAT_LEN):
    currID = 0
    def innerChkmyMatrix(passmat):
        nonlocal currID, PAT_LEN, strVal
        if(passmat == []):
            currID = filler(passmat, currID, PAT_LEN, strVal)
        else:
            for row in passmat:
                if(isinstance(row, list) and len(row) != 0):
                    innerChkmyMatrix(row)
                else:
                    currID = filler(row, currID, PAT_LEN, strVal)
    innerChkmyMatrix(passmat)

def filler(row, currID, PAT_LEN, strVal):
    e = 0
    while(e < PAT_LEN):
        currID = currID % len(strVal)
        val = strVal[currID]
        currID += 1
        row.append(val)
        e += 1
    return currID

print()
strVal = 'abcdefghijk'
PAT_LEN = 3
myMat0 = []
print('strVal: ', strVal, '\nPAT_LEN:', PAT_LEN)
print()
outerChkmyMatrix(myMat0, strVal, PAT_LEN)
print('myMat0: ', myMat0)