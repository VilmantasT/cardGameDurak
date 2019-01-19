def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self, top, bottom):
        try:
            common = gcd(top, bottom)

            self.num = top // common
            self.den = bottom // common
        except:
            print('Numerator or denumerator is not a number.')


    def __str__(self):
        return str(self.num)+ '/' + str(self.den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def show(self):
        print(self.num, '/', self.den)

    def __add__(self, otherfraction):

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):

        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __eq__ (self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(newnum, newden)

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum > secondnum

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum >= secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum <= secondnum


    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print('Addition:')
print(str(f1 + f2).rjust(15))
print('Subtraction: ')
print(f1 - f2)
print('Equality: ')
print(f1 == f2)
print('Less than: ')
print(f1 < f2)
print('Greater than: ')
print(f1 > f2)
print('Multiplication: ')
print(f1 * f2)
print('Division: ')
print(f1 // f2)
