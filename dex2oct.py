import sys

def dex2oct(n):
	nlist=[]
	res = int(n)
	wlist=['0']
	while not res == 0:
		nlist.append(str(res%8))
		res=res//8
	for i in range(len(nlist)):
		wlist.append(nlist[-i-1])
	return "".join(wlist)

def main():
	try:
		print dex2oct(sys.argv[1])
	except:
		print "Please provide a decimal number"
if __name__ =='__main__':
	main()