def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    #   initializes object
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom
    #   string representation
     def __str__(self):
         return str(self.num)+"/"+str(self.den)
    #   printing of the fraction?
     def show(self):
         print(self.num,"/",self.den)
    #   adding fractions
     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
    #   subtracting fractions
     def __sub__(self,otherfraction):
         newnum = self.num*otherfraction.den - \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
    #   equality test for fractions
     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

     def __mul__(self, other):
         newnum = self.num * other.num
         newden = self.den * other.den
         common = gcd(newnum, newden)
         return Fraction(newnum//common, newden//common)

     def __truediv__(self, other):
         newnum = self.num * other.den
         newden = self.den * other.num
         common = gcd(newnum, newden)
         return Fraction(newnum // common, newden // common)

     def __le__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum <= secondnum

# this code is not elegant, I realize I should
# have done more review of the split() function...
with open("lab02data.txt") as f:
    header_line = next(f)
    for line in f:
        n = line.find(" ", 0)
        firstnum = int(line[0:n])
        m = n + 1
        n = line.find(" ", m)
        firstden = int(line[m:n])
        m = n + 1
        n = line.find(" ", m)
        secondnum = int(line[m:n])
        m = n + 1
        n = line.find(" ", m)
        secondden = int(line[m:])
        firstcommon = gcd(firstnum, firstden)
        secondcommon = gcd(secondnum, secondden)
        firstfrac = Fraction(firstnum//firstcommon, firstden//firstcommon)
        secondfrac = Fraction(secondnum//firstcommon, secondden//firstcommon)

        print("The first fraction is: ", firstfrac)
        print("The second fraction is: ", secondfrac)
        print("The sum of the two fractions is: ", firstfrac + secondfrac)
        print("The difference of the two fractions is: ", firstfrac - secondfrac)
        print("The product of the two fractions is: ", firstfrac * secondfrac)
        print("The first fraction divided by the second fraction is: ", firstfrac / secondfrac)
        print("The first fraction is <= the second fraction: ", firstfrac <= secondfrac, end='\n\n')


# x = Fraction(1,2) #3/6
# y = Fraction(2,3) #4/6
# print(x+y)
# print(x-y)
# print(x == y)
# print(x*y)
# print(x/y)
# print(x<=y)