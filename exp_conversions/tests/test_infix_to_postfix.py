import pytest

from exp_conversions.infix_to_postfix import InfixToPostfix


@pytest.fixture
def converter():
    return InfixToPostfix()


@pytest.mark.parametrize('infix, expected_postfix', [
    ("A+B", "AB+"),
    ("A-B", "AB-"),
    ("A*B", "AB*"),
    ("A/B", "AB/"),
    ("A%B", "AB%"),
    ("A+B*C", "ABC*+"),
    ("A*B+C", "AB*C+"),
    ("A+B/C", "ABC/+"),
    ("A/B+C*D", "AB/CD*+"),
    ("(A+B)*C", "AB+C*"),
    ("A*(B+C)", "ABC+*"),
    ("(A+B)*(C-D)", "AB+CD-*"),
    ("((A+B)*C)/D", "AB+C*D/"),
    ("A*(B+(C/D))", "ABCD/+*"),
    ("A+B-C", "AB+C-"),
    ("A*B/C+D", "AB*C/D+"),
    ("A/B+C*D-E", "AB/CD*+E-"),
    ("A+B*C-D/E", "ABC*+DE/-"),
    ("A^B", "AB^"),
    ("A*B^C", "ABC^*"),
    ("(A+B)^C", "AB+C^"),
    ("A^B+C*D", "AB^CD*+"),
    ("-A+B", "A-B+"),
    ("A+(-B)", "AB-+"),
    ("-(A+B)", "AB+-"),
    ("-A*B", "A-B*"),
    ("A+-B*C", "AB-C*+"),
    ("A*-B+C", "AB-*C+"),
    ("A*-(B+C)", "ABC+-*"),
    ("A+(-B*C)/D", "AB-C*D/+"),
    ("-A*-B", "A-B-*"),
    ("((A+B)*-(C+D))/(E^F)", "AB+CD+-*EF^/"),
    ("-((A+B)*(C-D))/E", "AB+CD-*-E/"),
    ("-((A+B*C)/(D-E^F))", "ABC*+DEF^-/-"),
    ("A", "A"),
    ("-A", "A-"),
    ("-A+(B*-C)", "A-BC-*+"),
    ("-(-A+B)*C", "A-B+-C*"),
    ("-A+-B+C", "A-B-+C+"),
    ("-(A+B*(C-D))", "ABCD-*+-"),
    ("-A*-(B+C)", "A-BC+-*"),
    ("-A-B*C", "A-BC*-")
])
def test_infix_to_postfix(infix, expected_postfix, converter):
    assert converter.convert_to_postfix(infix) == expected_postfix
