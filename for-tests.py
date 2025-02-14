class Calculator:
    a = 3
    b = 4

    def add(self):  # oddiy method
        return self.a + self.b

    def multiply(self):
        sum_result = self.add()
        return sum_result * 2


calc = Calculator()  # obyekt yaratamiz
print(calc.multiply())  # Natija: 14