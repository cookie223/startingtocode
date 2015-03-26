import sys

def matrix_multi(list1, list2):
    list3=[0,0,0,0]
    list3[0]=list1[0]*list2[0]+list1[1]*list2[2]
    list3[1]=list1[0]*list2[1]+list1[1]*list2[3]
    list3[2]=list1[2]*list2[0]+list1[3]*list2[2]
    list3[3]=list1[2]*list2[1]+list1[3]*list2[3]
    return list3
    
def f_n_matrix(n):
    if n == 1:
        return [1,1,1,0]
    elif n ==2:
        return [2,1,1,1]
    else:
        return matrix_multi(f_n_matrix(n//2), f_n_matrix(n-n//2))
        
def f_number(n):
    return f_n_matrix(n)[0]
    
def main():
    print f_number(int(sys.argv[1]))

if __name__ == '__main__':
  main()