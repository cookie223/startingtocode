digits = [8,9,9,9]

def plusOne(digits):
	if not digits:
		return None
	else:
		digits[-1] +=1
		check = 1
		while check:
			for i in range(len(digits)-1):
				if not digits[-i-1] == 10:
					check = 0
					break
				else:
					digits[-i-1] = 0
					digits[-i-2] +=1
			check = 0
		if digits[0] == 10: 
			digits[0] = 0
			digits.insert(0,1)

		return digits

print plusOne(digits)