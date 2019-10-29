#!/usr/bin/python
from sympy import *

def rotations(num):
	count=0 
	rotation_lst=[]
	num=str(num)
	while(count<len(num)):
		num=num[1:]+num[0]
		count+=1 
		rotation_lst.append(int(num))
	rotation_lst1=sorted(rotation_lst,key=int)
	return rotation_lst1


def CircullerPrime(x):
	x = rotations(x)
	for i in x:
		if not isprime(i):
			return False
	return True


if __name__ == "__main__":
	#print CircullerPrime(197)
	for i in range(1,1000001):
		if CircullerPrime(i):
			print i

'''
OUTPUT:
2
3
5
7
11
13
17
31
37
71
73
79
97
113
131
197
199
311
337
373
719
733
919
971
991
1193
1931
3119
3779
7793
7937
9311
9377
11939
19391
19937
37199
39119
71993
91193
93719
93911
99371
193939
199933
319993
331999
391939
393919
919393
933199
939193
939391
993319
999331
'''
