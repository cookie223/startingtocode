digits = [8,9,9,9]
class Found(Exception): pass

def plusOne(digits):
	if len(digits)==0:
		return None
	else:
		digits[-1] +=1
		try:
			while 1:
				for i in range(len(digits)-1):
					if not digits[-i-1] == 10:
						raise Found
					else:
						digits[-i-1] = 0
						digits[-i-2] +=1
				break
		except Found:
			digits=digits
		if digits[0] == 10: 
			digits[0] = 0
			digits.insert(0,1)

		return digits

print plusOne(digits)