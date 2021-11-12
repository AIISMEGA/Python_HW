class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f'{self.real} + {self.imaginary}j'

my_complex_number_1 = Complex(12, 16)
my_complex_number_2 = Complex(-15, 28)
print(f'Сумма: {my_complex_number_1 + my_complex_number_2}')
print(f'Произведение: {my_complex_number_1 * my_complex_number_2}')

my_number_1 = complex(12, 16)
my_number_2 = complex(-15, 28)
print(my_number_1 + my_number_2)
print(my_number_1 * my_number_2)