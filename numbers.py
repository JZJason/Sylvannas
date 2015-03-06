__author__ = 'jasonzhang'

import math

class number:
    rational = True
    def __add__(self, other):
        if self.rational == True and other.rational == True:
            return rationalNumber(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        elif self.rational == False and other.rational == True:
            return irrational(self.value + other.value())
        elif self.rational == True and other.rational == False:
            return irrational(self.value() + other.value)
        else:
            return irrational(self.value + other.value)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if self.rational == True and other.rational == True:
            return rationalNumber(self.numerator * other.numerator, self.denominator * other.denominator)
        elif self.rational == True and other.rational == False:
            return irrational(self.value() * other.value)
        elif self.rational == True and other.rational == False:
            return irrational(self.value() * other.value)
        else:
            return irrational(self.value * other.value)

    def __div__(self, other):
        return self * other.reverse()

    def __pow__(self, power, modulo=None):
        if self.rational == True and power.rational == True:
            return irrational(self.value() ** power.value())
        elif self.rational == True and power.rational == False:
            if int(power.value) == power.value:
                return rationalNumber(self.numerator ** power.value, self.denominator ** power.value)
            else:
                return irrational(self.value()**power.value)
        elif self.rational == False and power.rational == True:
            return irrational(self.value ** power.value())
        else:
            return irrational(self.value**power.value)

class rationalNumber(number):
    def __init__(self,number1,number2):
        self.rational = True
        largeMulti = max(findMultiplier(number1),findMultiplier(number2))
        result1 = number1 * largeMulti
        result2 = number2 * largeMulti
        gcdX = gcd(result1,result2)
        self.numerator = result1 / gcdX
        self.denominator = result2 / gcdX

    def value(self):
        return self.numerator / float(self.denominator)

    # def __add__(self, other):
    #     return rationalNumber(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
    #
    # def __sub__(self, other):
    #     return self + (-other)
    #
    # def __mul__(self, other):
    #     return rationalNumber(self.numerator * other.numerator, self.denominator * other.denominator)
    #
    # def __div__(self, other):
    #     return self * rationalNumber(other.denominator, other.numerator)
    # def __pow__(self, power, modulo=None):
    #     if type(pow) is int:
    #         return rationalNumber(self.numerator ** power, self.denominator ** power)
    #     else:
    #         return rationalNumber.value() ** power

    def __neg__(self):
        return rationalNumber(-self.numerator,self.denominator)

    def reverse(self):
        return rationalNumber(self.denominator, self.numerator)

    def pprint(self):
        print self.numerator,"/",self.denominator

class irrational(number):
    def __init__(self, value):
        self.rational = False
        self.value = value

    def __neg__(self):
        return irrational(-self.value)

    def reverse(self):
        return irrational(1/self.value)

class complexNumber:
    rational = True
    def __add__(self, other):
        return rationalComplex(self.re + other.re, self.im + other.im)
    def __sub__(self, other):
        return self + (-other)
    def __mul__(self, other):
        return rationalComplex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
    def __div__(self, other):
        return self * other.reverse()

class rationalComplex(complexNumber):
    def __init__(self,re,im):
        self.re = re
        self.im = im
        self.rational = True

    def conjugate(self):
        return rationalComplex(self.re, -self.im)

    def value(self):
        return complex(self.re.value(),self.im.value())

    def arg(self):
        return math.atan((self.re / self.im).value())

    # def __add__(self, other):
    #     return rationalComplex(self.re + other.re, self.im + other.im)
    #
    # def __sub__(self, other):
    #     return self + (-other)
    #
    # def __mul__(self, other):
    #     return rationalComplex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
    #
    # def __div__(self, other):
    #     l = (other.re ** 2 + other.im ** 2) ** 0.5
    #     m = self * other.conjugate()
    #     return rationalComplex(rationalComplex(m.re,l),rationalNumber(m.im,l))

    def __neg__(self):
        return rationalComplex(-self.re, self.im)

    def reverse(self):
        l = self.re ** rationalNumber(2,1) + self.im ** rationalNumber(2,1)
        return rationalComplex(rationalNumber(self.re, l),rationalComplex(self.im, l))

class complex(complexNumber):
    def __init__(self, re, im):
        self.re = re
        self.im = im
        self.rational = False

    def conjugate(self):
        return complex(self.re, -self.im)

    def arg(self):
        return math.atan(self.re.value / self.im.value)

    def __neg__(self):
        return complex(-self.re, -self.im)

    def reverse(self):
        l = self.re.value ** 2 + self.im.value ** 2
        return complex(irrational(self.re.value/l),-irrational(self.im.value/l))

    def convertToExp(self):
        return [(self.re**2+self.im**2)**0.5, self.arg()]

def findMultiplier(number1):
    stringOfNumber = str(number1)
    count = len(stringOfNumber)
    positionOfPoint = stringOfNumber.find(".")
    mi = count - positionOfPoint - 1
    return 10 ** mi

def gcd(number1, number2):
    if number1 == 0:
        return number2
    else:
        return gcd(number2%number1, number1)

r1 = rationalNumber(1,3)

print r1 + irrational(3.0)
print r1 * irrational(3.0)
print r1 / r1
print irrational(3.0) ** irrational(4.0)
print r1 ** r1
print r1 ** irrational(3.0)
print irrational(3.0) ** r1

print rationalComplex(r1,r1) + rationalComplex(r1,r1)

print complex(irrational(3.0),irrational(3.0)) + complex(irrational(3.0),irrational(3.0))

print complex(irrational(3.0),irrational(3.0)) + rationalComplex(r1,r1)
print (rationalComplex(r1,r1)/complex(irrational(3.0),irrational(3.0))).re.value