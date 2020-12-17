import abc
import random

class Numbers(abc.ABC):

    @abc.abstractmethod
    def __add__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __sub__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __mul__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __truediv__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self, other):
        raise NotImplementedError

    @abc.abstractmethod
    def __repr__(self, other):
        raise NotImplementedError

class Rational(Numbers):

    def __init__(self, nominator_number, denominator_number):
        self.nominator_number = nominator_number
        self.denominator_number = denominator_number

    def __add__(self, other):
        if isinstance(other,Complex):
            new_real_number = self.nominator_number/self.denominator_number + other.real_number
            new_imaginary_number = other.imaginary_number
            return Complex(round(new_real_number,1), new_imaginary_number)
        if isinstance(other,Rational):
            if self.denominator_number != other.denominator_number:
                new_nominator_number = self.nominator_number * other.denominator_number + other.nominator_number * self.denominator_number
                new_denominator_number = self.denominator_number * other.denominator_number
            else:
                new_nominator_number = self.nominator_number + other.nominator_number
                new_denominator_number = self.denominator_number
            return Rational(new_nominator_number, new_denominator_number)
        else:
            return Rational(self.nominator_number + other * self.denominator_number, self.denominator_number)

    __radd__ = __add__

    def __sub__(self, other):
        if self.denominator_number != other.denominator_number:
            new_nominator_number = self.nominator_number * other.denominator_number - other.nominator_number * self.denominator_number
            new_denominator_number = self.denominator_number * other.denominator_number
        else:
            new_nominator_number = self.nominator_number - other.nominator_number
            new_denominator_number = self.denominator_number
        return Rational(new_nominator_number, new_denominator_number)

    def __mul__(self, other):
        new_nominator_number = self.nominator_number * other.nominator_number
        new_denominator_number = self.denominator_number * other.denominator_number
        return Rational(new_nominator_number, new_denominator_number)

    def __truediv__(self, other):
        new_nominator_number = self.nominator_number * other.denominator_number
        new_denominator_number = self.denominator_number * other.nominator_number
        return Rational(new_nominator_number, new_denominator_number)

    def __str__(self):
        return f'{self.nominator_number}/{self.denominator_number}'

    def __repr__(self):
        return f'{self.nominator_number}/{self.denominator_number}'

    def rational_generator(number):
        return [Rational(random.randint(0,100),random.randint(0,100)) for i in range(number)]

class Complex(Numbers):

    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def __add__(self, other):
       if isinstance(other,Complex):
            new_real_number = self.real_number + other.real_number
            new_imaginary_number = self.imaginary_number + other.imaginary_number
            return Complex(round(new_real_number, 1), new_imaginary_number)
        elif isinstance(other,Rational):
            new_real_number = self.real_number + other.nominator_number/other.denominator_number
            new_imaginary_number = self.imaginary_number
            return Complex(round(new_real_number,1), new_imaginary_number)
        else:
            return Complex(self.real_number + other, self.imaginary_number)

    __radd__ = __add__

    def __sub__(self, other):
        new_real_number = self.real_number - other.real_number
        new_imaginary_number = self.imaginary_number - other.imaginary_number
        return Complex(round(new_real_number,1), new_imaginary_number)

    def __mul__(self, other):
        new_real_number = self.real_number * other.real_number
        new_imaginary_number = self.imaginary_number * other.imaginary_number
        return Complex(new_real_number, new_imaginary_number)

    def __truediv__(self, other):
        new_real_number = self.real_number / other.real_number
        new_imaginary_number = self.imaginary_number / other.imaginary_number
        return Complex(new_real_number, new_imaginary_number)

    def __str__(self):
        return f'{self.real_number}+{self.imaginary_number}i'

    def __repr__(self):
        return f'{self.real_number}+{self.imaginary_number}i'

    def complex_generator(number):
        return [Complex(random.randint(0,100),random.randint(0,100)) for i in range(number)]

def main():
    complex_number1 = Complex(10, 1)
    complex_number2 = Complex(5, 2)
    rational_number1 = Rational(2,3)
    rational_number2 = Rational(4,5)
    complex_number_sum = complex_number1 + complex_number2
    rational_number_sum = rational_number1 + rational_number2
    complex_rational_sum1 = complex_number1 + rational_number1
    complex_rational_sum2 = complex_number2 + rational_number2

    print('Pierwszy ułamek to: ', rational_number1)
    print('Drugi ułamek to: ', rational_number2)
    print('Pierwsza liczba zespolona to: ', complex_number1)
    print('Druga liczba zespolona to: ', complex_number2)
    print('Wynik dodawania liczb zespolonych: ', complex_number_sum)
    print('Wynik dodawania liczb ułamkowych: ', rational_number_sum)
    print(f'Wynik dodawania {complex_number1} i {rational_number1} : ', complex_rational_sum1)
    print(f'Wynik dodawania {complex_number2} i {rational_number2} : ', complex_rational_sum2)
    complex_lst = Complex.complex_generator(5)
    rational_lst = Rational.rational_generator(5)
    print(complex_lst)
    print(rational_lst)
    list_sum = complex_lst + rational_lst
    print(list_sum)

    # sum = Complex(0, 0)
    # for i in list_sum:
    #     sum += i
    print(sum(list_sum))




if __name__ == '__main__':
    main()