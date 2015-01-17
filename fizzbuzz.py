#-*- coding: utf-8 -*-

for n in range(1,101) :
	if 0 == (n % 3 ) and 0 == (n % 5):
		print u"Fizz Buzz"
	elif 0 == (n % 3):
		print u"Fizz"
	elif 0 == (n % 5):
		print u"Buzz"
	else: print n

