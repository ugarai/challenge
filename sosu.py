#-*- coding: utf-8 -*-

limit = 1000;

for i in range(1,limit + 1) :
	for j in range(2,(i + 1)):
		n = i % j
		if j != i and 0 == n: 
			break
		elif j == i:
			print '%d.' % i
		
