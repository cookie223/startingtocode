import sys

def majorityElement(num):
	#num=[3,2,3,1,3] #For test
	numdict ={}
	for i in num:
		numdict[i]=numdict.get(i,0)+1
	for text, i in numdict.items():
		if i > len(num)//2:
			return str(text)
			break
			
def main():
	try:
		print majorityElement(sys.argv[1])
	except:
		print "error. Maybe invalid input"
if __name__ == '__main__':
	main()
	