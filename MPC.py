from calendar import c
import numpy as np
import scipy.optimize as min

class LTI_System:
    
    A = np.array([[1, 1],
                    [0 ,1]])
    B = np.array([0 , 1])
    P = np.array([[1, 0],
                    [0 ,1]])
    Q = P
    R = 10
    x0 = np.array([-4.5 ,2])
    xk = np.zeros(2)
    uk = 0
    N = 0
        # x0 = np.array([-4.5 ,3])
    
    def systemfunc(self):
        return self.A@self.xk + self.B@self.uk

    def sysgo(self):
        if self.N > 0 :
            xk = self.systemfunc()
            self.N -= 1
    def xk_abound(self):
        for x in self.xk:
            if x > 5 :
                x = 5
            elif x <-5 :
                x = -5
       
    def uk_abound(self):
        if self.uk > 0.5 :
            self.uk = 0.5
        elif self.uk < -0.5:
            self.uk = -0.5

    def costfunction(self):
        return (self.xk@self.Q@self.xk + self.uk * self.R * self.uk)/2
    
    def hfunction(self):
        return self.xk@self.Q@self.xk/2

    def con(args,self):
        cons = ({'type': 'ineq', 'fun':  0.5 + self.uk },
                {'type': 'ineq', 'fun':  0.5 - self.uk },
                {'type': 'ineq', 'fun':  5 - self.xk[0]},
                {'type': 'ineq', 'fun':  5 - self.xk[1]},
                {'type': 'ineq', 'fun':  5 + self.xk[0]},
                {'type': 'ineq', 'fun':  5 + self.xk[1]},
                {'type': 'eq', 'fun':  self.sysgo()})
        return cons


if __name__ == "__main__":
    print(LTI_System.xk)