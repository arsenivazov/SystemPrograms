def egyptian_fraction(numerator, denominator):
    result = []

    while numerator != 0:

        unit_denominator = -(-denominator // numerator)


        result.append(unit_denominator)

        numerator = numerator * unit_denominator - denominator
        denominator = denominator * unit_denominator

    return result


fraction1 = egyptian_fraction(2, 3)
fraction2 = egyptian_fraction(6, 14)
fraction3 = egyptian_fraction(12, 13)

print("Egyptian Fraction Representation of 2/3:", fraction1)
print("Egyptian Fraction Representation of 6/14:", fraction2)
print("Egyptian Fraction Representation of 12/13:", fraction3)
