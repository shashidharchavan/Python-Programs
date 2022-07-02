import fractions
n1=int(input("1st numerator:"))
d1=int(input("1st denominator:"))
n2=int(input("2nd numerator:"))
d2=int(input("2nd denominator:"))

f1=fractions.Fraction(n1,d1)
f2=fractions.Fraction(n2,d2)

print(f1+f2)