import sys

def lcs_matrix(string1,string2):
    'Learn the Dynamic Programming process'
    '''#Generate the matrix
    m0 = [0]*(len(string1)+1)
    #m[j][i] = 0, if j=0 or i =0
    m=[]
    for j in range(len(string2)+1):
        m.append(m0[:]) #[:]is important to duplicate list, not refer to the same one'''
    m = [[0 for i in range(len(string1)+1)] for j in range(len(string2)+1)]
    #better way to generate m without refering to the same list
    j=1
    while j <len(string2)+1:
        i=1
        while i <len(string1)+1:
            if string1[i-1] == string2[j-1]:
                m[j][i] = m[j-1][i-1]+1
            else:
                m[j][i]=max(m[j][i-1],m[j-1][i])
            i +=1
        j+=1
    print m
    
    #Read out the Longest common string
    i=len(string1)
    j=len(string2)
    lcslist=[]
    while i >0 and j>0:
        if m[j][i]==m[j-1][i]:
            j-=1
        elif m[j][i]==m[j][i-1]:
            i-=1
        else:
            assert string2[j-1]==string1[i-1]
            lcslist.insert(0,string2[j-1])
            i-=1
            j-=1
    lcs="".join(lcslist)
    return lcs

	

	
	
	
	
def main():
	print lcs_matrix(sys.argv[1],sys.argv[2])

if __name__ =='__main__':
	main()
	
