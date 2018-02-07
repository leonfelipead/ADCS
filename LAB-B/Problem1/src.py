def isMultiple_h(num, check, doPrint, oddEven):
	if (num % check == 0):
		if doPrint == True:
			if oddEven == True:
				if num % 4 == 0:
					return 'divisible by 4';
				else:
					return 'even'
			else:
				return 'divides evenly'
		else:
			return True
	else:
		if doPrint == True:
			if oddEven == True:
				return 'odd'
			else:
				return 'does not divide evenly'
		else:
			return False
		
def isMultiple(num, check):
	return isMultiple_h(num, check, True, False)

def isOddOrEven(num):
	return isMultiple_h(num, 2, True, True)
	
def isPrime(num):
	for n in range(2, num):
		if isMultiple_h(num, n, False, False):
			return 'not a prime number'
			break
	else:
		return 'prime number'