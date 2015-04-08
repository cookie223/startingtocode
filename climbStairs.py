class Solution:
    # @param n, an integer
    # @return an integer
    class matrix22:
        def __init__(self,a=0,b=0,c=0,d=0):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        def __mul__(self,other):
            a= self.a*other.a + self.b*other.c
            b= self.a*other.b + self.b*other.d
            c= self.c*other.a + self.d*other.c
            d= self.c*other.b + self.d*other.d
            return Solution.matrix22(a,b,c,d)
        def pow2(self):
            power2 = self * self
            return power2
    def f_n_matrix(self,n):
        if n == 1:
            return Solution.matrix22(1,1,1,0)
        elif n ==2:
            return Solution.matrix22(2,1,1,1)
        else:
            if n%2 ==0:
                return self.f_n_matrix(n/2).pow2()
            else:
                return self.f_n_matrix(n//2).pow2() * Solution.matrix22(1,1,1,0)
    def climbStairs(self, n):
        return self.f_n_matrix(n).a
        