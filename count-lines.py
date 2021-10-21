""" 
This module counts the number of lines in standard input
Input: a string
Output : count
"""


import sys

count = 0
for line in sys.stdin:
	count +=1

print(count, "lines in standard input")
