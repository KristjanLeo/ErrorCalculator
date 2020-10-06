class Ovissa:
    def __init__(self, est, uncert):
        self.est = est
        self.uncert = uncert

    def __str__(self):
        return str(self.est)+' ± '+str(self.uncert)

    def __add__(self, B):
        new_est = self.est + B.est
        new_uncert = self.uncert + B.uncert
        return Ovissa(new_est, new_uncert)

    def __radd__(self, n):
        new_est = self.est + n
        new_uncert = self.uncert
        return Ovissa(new_est, new_uncert)

    def __sub__(self, B):
        new_est = self.est - B.est
        new_uncert = self.uncert + B.uncert
        return Ovissa(new_est, new_uncert)

    def __rsub__(self, n):
        new_est = self.est-n
        new_uncert = self.uncert
        return Ovissa(new_est, new_uncert)

    def __mul__(self, B):
        new_est = self.est*B.est
        new_uncert = new_est*(self.uncert/self.est+B.uncert/B.est)
        return Ovissa(new_est, new_uncert)

    def __rmul__(self, r):
        new_est = self.est*r
        new_uncert = self.uncert*r
        return Ovissa(new_est, new_uncert)

    def __div__(self, B):
        new_est = self.est/B.est
        new_uncert = new_est*(self.uncert/self.est+B.uncert/B.est)
        return Ovissa(new_est, new_uncert)

    def __rdiv(self, r):
        new_est = self.est/r
        new_uncert = self.uncert/r
        return Ovissa(new_est, new_uncert)

    def __pow__(self, n):
        if n > 0:
            new_est = self.est**n
            new_uncert = new_est*(n*self.uncert/self.est)
            return Ovissa(new_est, new_uncert)


A = Ovissa(2, 0.1)
B = Ovissa(13, 4)
C = Ovissa(3.1, 0.001)


print(A*B)
print(A**5)
print(A*B*C)
print((A+B)*C)
