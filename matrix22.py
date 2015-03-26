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
        res= self * self
        return res