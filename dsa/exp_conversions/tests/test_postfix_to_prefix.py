import pytest

from exp_conversions.postfix_to_prefix import PostfixToPrefix


@pytest.fixture
def converter():
    return PostfixToPrefix()


@pytest.mark.parametrize('postfix_exp,expected_prefix', [
    ("AB+", "+AB"),
    ("ABC*+", "+A*BC"),
    ("AB+C*", "*+ABC"),
    ("ABCD^*+", "+A*B^CD"),
    ("ABC/+D*", "*+A/BCD"),
    ("AB+CDE-**", "*+AB*C-DE"),
    ("ABCD/+*E-", "-*A+B/CDE")
]
                         )
def test_postfix_to_prefix(postfix_exp, expected_prefix, converter):
    assert converter.convert_to_prefix(postfix_exp) == expected_prefix
