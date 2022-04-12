def simple_interest(p,t,r):
	print('principal is', p)
	print('time period is', t)
	print('rate of interest is',r)
	si = (p * t * r)/100
	print('The Simple Interest is', si)
	return si
simple_interest(8, 6, 8)
