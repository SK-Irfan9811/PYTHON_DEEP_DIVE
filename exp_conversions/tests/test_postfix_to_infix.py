import pytest

from exp_conversions.postfix_to_infix import PostfixToInfix


@pytest.fixture
def converter():
    return PostfixToInfix()


@pytest.mark.parametrize("expected_infix_exp,postfix_exp", [
    ("(A+B)", "AB+"),
    ("(A-B)", "AB-"),
    ("(A*B)", "AB*"),
    ("(A/B)", "AB/"),
    ("(A%B)", "AB%"),
    ("(A+(B*C))", "ABC*+"),
    ("((A*B)+C)", "AB*C+"),
    ("(A+(B/C))", "ABC/+"),
    ("((A/B)+(C*D))", "AB/CD*+"),
    ("((A+B)*C)", "AB+C*"),
    ("(A*(B+C))", "ABC+*"),
    ("((A+B)*(C-D))", "AB+CD-*"),
    ("(((A+B)*C)/D)", "AB+C*D/"),
    ("(A*(B+(C/D)))", "ABCD/+*"),
    ("((A+B)-C)", "AB+C-"),
    ("(((A*B)/C)+D)", "AB*C/D+"),
    ("(((A/B)+(C*D))-E)", "AB/CD*+E-"),
    ("((A+(B*C))-(D/E))", "ABC*+DE/-"),
    ("(A^B)", "AB^"),
    ("(A*(B^C))", "ABC^*"),
    ("((A+B)^C)", "AB+C^"),
    ("((A^B)+(C*D))", "AB^CD*+"),
    ("((-A)+B)", "A-B+"),
    ("(-(A+B))", "AB+-"),
    ("((-A)*B)", "A-B*"),
    ("(-((A+(B*C))/(D-(E^F))))", "ABC*+DEF^-/-"),
    ("A", "A"),
    ("(-A)", "A-"),
    ("(-(A+(B*(C-D))))", "ABCD-*+-"),
    ("((-A)-(B*C))", "A-BC*-")
])
def test_infix_convertion_from_postfix(postfix_exp, expected_infix_exp, converter):
    assert converter.convert_to_infix(postfix_exp) == expected_infix_exp
