class Number:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return Number(self.value + other.value)

    def subtract(self, other):
        return Number(self.value - other.value)

    def multiply(self, other):
        return Number(self.value * other.value)

    def divide(self, other):
        if other.value == 0:
            raise ValueError("Cannot divide by zero.")
        return Number(self.value / other.value)

    def __repr__(self):
        return f"Number({self.value})"
    

class RationalNumber(Number):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        super().__init__(numerator / denominator)
        self.numerator = numerator
        self.denominator = denominator
        
    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)
    
    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return RationalNumber(new_numerator, new_denominator)
    
    def multiply(self, other):
        numeratorv = self.numerator * other.numerator
        denominatorv = self.denominator * other.denominator
        return RationalNumber(numeratorv, denominatorv)
    
    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return RationalNumber(new_numerator, new_denominator)
    
    def __repr__(self):
        return f"RationalNumber({self.numerator}/{self.denominator})"