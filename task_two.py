"""
Задача 2.
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    """
    Класс для операций с комплексными числами
    """

    def __init__(self, real=0., imaginary=0.):
        """
        Конструктор класса
        :param real: целая часть числа
        :param imaginary: мнимая часть числа
        """
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        """
        Переопредяем метод для более красивого вывода
        """
        # NOTE: если мнимая часть отрицательная, то выводим знак минус перед числом, а само число берем по модулю
        return f'{self.real} {"+" if self.imaginary > 0 else "-"} {abs(self.imaginary)}j'

    def __add__(self, other):
        """
        Переопределяем операцию "+"
        """
        return ComplexNumber(
            real=self.real + other.real,
            imaginary=self.imaginary + other.imaginary,
        )

    def __iadd__(self, other):
        """
        Переопределяем операцию "+="
        """
        self.real += other.real
        self.imaginary += other.imaginary
        return self

    def __mul__(self, other):
        """
        Переопределяем операцию "*"
        """
        return ComplexNumber(
            real=self.real * other.real - self.imaginary * other.imaginary,
            imaginary=self.imaginary * other.real + self.real * other.imaginary,
        )

    def __imul__(self, other):
        """
        Переопределяем операцию "*="
        """
        # создаем временную переменную для хранения целой части числа
        real = self.real * other.real - self.imaginary * other.imaginary
        # создаем временную переменную для хранения мнимой части числа
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        self.real = real
        self.imaginary = imaginary
        return self


if __name__ == '__main__':
    # Создаем 2 экземпляра комплексных чисел
    cn1 = ComplexNumber(12.3, -2.6)
    cn2 = ComplexNumber(10, 1.54)
    print(f'Первое число: {cn1}')
    print(f'Второе число: {cn2}')

    # Проверка операций сложения
    print(f'({cn1}) + ({cn2}) = {cn2 + cn1}')
    cn1 += cn2
    print(f'Тест для оператора "+=": {cn1}')

    # Проверка операций умножения
    print(f'({cn1}) * ({cn2}) = {cn1 * cn2}')
    cn1 *= cn2
    print(f'Тест для оператора "*=": {cn1}')
