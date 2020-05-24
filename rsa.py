import Utils as u
import encryption as en
import decryption as de
import random

LOWERBOUND = 1e259 #RSA-260 
UPPERBOUND = 9.99999999999999999999999999999999999999999999999999999999999999e259
#the last 4 digit of N % e + (coprime to N * e mod + 662)= word breaker
class RSAObj(object):
    def __init__(self, p = None, q = None, N = None, e = None):
        self.p = p
        self.q = q
        self.N = N
        self.e = e
        self.message = None
        self.filePath = None

    @classmethod
    def newUser(cls):
        newP = u.getPrime(-1, LOWERBOUND, UPPERBOUND)
        newQ = u.getPrime(newP, LOWERBOUND, UPPERBOUND)
        newE = u.getCoPrime((newP - 1) * (newQ - 1))
        return cls(newP, newQ, newP * newQ, newE)
    
    def getMessage(self, inputMess):
        self.message = inputMess

    def encrypteString(self):
        result = ""
        breaker = ((self.N % 10000) % self.e) + u.getCoPrime(self.N * self.e + 662)    
        for i in self.message:
            numEn = en.encrypt(ord(i), self.N, self.e)
            result = result + str(numEn) + str(breaker + u.getFirstDigits(numEn)) + "~" 
            
        return result
    def decrypteString(self):
        pass