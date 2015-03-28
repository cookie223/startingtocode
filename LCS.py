'''import sys

def lcs_matrix(string1,string2):
	'Learn the Dynamic Programming process'
	#Initialize the matrix
	m = [([0]*(len(string1)+1))]*(len(string2)+1)
	while i < len(string1) and j < len(string2):
		if string2[j] == string1[i]:
				try:
					m[j][i]=max(m[j-1][i],m[j][i-1])+1
				except:
					m[j][i]=1
	print m
	

	
	
	
	
def main():
	lcs_matrix(sys.argv[1],sys.argv[2])

if __name__ =='__main__':
	main()
	
'''