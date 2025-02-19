from multiples_and_factors import factors
import PySimpleGUI as sg

class Fraction:
    def __init__(self, numerator, denominator, whole=0):
        self.whole_number = whole
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return self.str()

    def str(self):
        if self.whole_number != 0 and self.numerator == 0:
            return str(self.whole_number)
        elif self.whole_number != 0:
            return "{} {}/{}".format(self.whole_number, self.numerator, self.denominator)
        else:
            return "{}/{}".format(self.numerator, self.denominator)

    def simplify(self, explain=False):
        temp = MathFractionHelper(None, None, explain)
        simplified = temp.simplify_helper(self.copy())
        self.numerator = simplified.numerator
        self.denominator = simplified.denominator

    def make_improper(self):
        self.numerator = self.whole_number * self.denominator + self.numerator
        self.whole_number = 0

    def copy(self):
        return Fraction(self.numerator, self.denominator, whole=self.whole_number)


class MathFractionHelper:
    def __init__(self, fraction1, fraction2, explain_mode=True):
        self.fraction1 = fraction1
        self.fraction2 = fraction2
        self.explain_mode = explain_mode

    def multiply(self):
        result = self.multiply_helper(self.fraction1.copy(), self.fraction2.copy())
        if self.explain_mode:
            text = """Solving {} * {}
            First, multiply the numerators together ({} * {} = {})
            Then, multiply the denominator together ({} * {} = {})
            The result is {}""".format(self.fraction1.str(),
                                       self.fraction2.str(),
                                       self.fraction1.numerator,
                                       self.fraction2.numerator,
                                       result.numerator,
                                       self.fraction1.denominator,
                                       self.fraction2.denominator,
                                       result.denominator,
                                       result.str())
            sg.popup(text, line_width=200, title='Multiplying Fractions Explanation')

        return result

    @staticmethod
    def multiply_helper(fraction1, fraction2):
        fraction1.make_improper()
        fraction2.make_improper()
        new_numerator = fraction1.numerator * fraction2.numerator
        new_denominator = fraction1.denominator * fraction2.denominator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        if self.fraction1 is not None:
            self.fraction1 = self.simplify_helper(self.fraction1)
        if self.fraction2 is not None:
            self.fraction2 = self.simplify_helper(self.fraction2)

    def simplify_helper(self, fraction):
        fraction_original = fraction.copy()
        numerator_factors = factors(fraction.numerator)
        numerator_factors_for_explain = numerator_factors.copy()

        denominator_factors = factors(fraction.denominator)
        denominator_factors_for_explain = denominator_factors.copy()

        numerator_factors.sort(reverse=True)
        div = None
        for factor in numerator_factors:
            if factor in denominator_factors:
                div = factor
                break

        fraction.numerator = int(fraction.numerator / div)
        fraction.denominator = int(fraction.denominator / div)

        fraction_improper = fraction.copy()

        if fraction.numerator > fraction.denominator:
            fraction.whole_number = int(fraction.numerator / fraction.denominator)
            fraction.numerator = int(fraction.numerator % fraction.denominator)
            mixed = True
        else:
            mixed = False

        if self.explain_mode:
            text = """Simplifying {}:
            First, we need to find the factors of the numerator and denominator:
            \t- The factors of the numerator are:\t\t{}
            \t- The factors of the denominator are:\t{}
            Now we need to determine the highest common factor:
            \t- The highest common factor is {}
            Therefore, we can divide both fractions by {}, resulting in {}""".format(fraction_original.str(),
                                                                                     numerator_factors_for_explain,
                                                                                     denominator_factors_for_explain,
                                                                                     div,
                                                                                     div,
                                                                                     fraction_improper.str())
            if mixed:
                text += '\nSince {} is more than one, we can rewrite it to {}'.format(fraction_improper, fraction.str())

            sg.popup(text, title='Simplifying Fraction Explanation', line_width=1000000)

        return fraction


frac_1 = Fraction(1022, 4095)
frac_2 = Fraction(8, 4)
m = MathFractionHelper(frac_1, frac_2)
m.simplify()
