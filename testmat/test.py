# check hackerrank.com


import sys
import os

#------------------------------------------------------------------

def  carParking(n, available):
    for col in range(n):
        for row in range(n):
            if available[row][col] == 0:
                return [row+1,col+1]
    return [0,0]

"""
try copy this input
5
5
5
1 1 1 1 0
0 0 0 0 0
1 1 0 0 0
1 0 0 0 0
1 1 1 0 0
"""

_n = int(raw_input());


_available_rows = 0
_available_cols = 0
_available_rows = int(raw_input())
_available_cols = int(raw_input())

_available = []
for _available_i in xrange(_available_rows):
    _available_temp = map(int,raw_input().strip().split(' '))
    _available.append(_available_temp)

res = carParking(_n, _available)
for res_cur in res:
    print str(res_cur) + "\n"

#------------------------------------------------------------------

def permutate(string1, string2):
    s1 = list(string1)
    s1r = s1[::-1]
    print s1r
    s2 = list(string2)
    print s2
    if s1r == s2:
        return 1
    else:
        return 0
        

print permutate('avd ',' dva')

#------------------------------------------------------------------

def  accomplice(numberOfBars):
    holes = 2, 3, 4, 5, 6, 7
    n = numberOfBars//2 - 1
    if numberOfBars % 2 > 0:
        return holes[n] * holes[n - 1]
    else:
        return holes[n] * holes[n]
    print n

_numberOfBars = int(raw_input());

print accomplice(_numberOfBars)

