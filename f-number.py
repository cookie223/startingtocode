import sys

class matrix22(object):
    def __init__(self, a=0,b=0,c=0,d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __mul__(self, other):
        a= self.a*other.a + self.b*other.c
        b= self.a*other.b + self.b*other.d
        c= self.c*other.a + self.d*other.c
        d= self.c*other.b + self.d*other.d
        return matrix22(a,b,c,d)
    def pow2(self):
        power2= self * self
        return power2
def f_n_matrix(n):
    if n == 1:
        return matrix22(1,1,1,0)
    elif n ==2:
        return matrix22(2,1,1,1)
    else:
        if n % 2 == 0:
            res= f_n_matrix(n/2).pow2()
        else :
            res= f_n_matrix(n//2).pow2() * matrix22(1,1,1,0)
        return res
        
def f_number(n):
    res= f_n_matrix(n)
    return res.a
    
def main():
    print f_number(int(sys.argv[1]))

if __name__ == '__main__':
  main()