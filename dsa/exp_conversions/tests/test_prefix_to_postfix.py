import pytest

from exp_conversions.prefix_to_postfix import PrefixToPostfix


@pytest.fixture
def converter():
    return PrefixToPostfix()


@pytest.mark.parametrize('expected_postfix,prefix', [
    ("AB+", "+AB"),
    ("ABC*+", "+A*BC"),
    ("AB+C*", "*+ABC"),
    ("ABCD^*+", "+A*B^CD"),
    ("ABC/+D*", "*+A/BCD"),
    ("AB+CDE-**", "*+AB*C-DE"),
    ("ABCD/+*E-", "-*A+B/CDE")
]
                         )
def test_prefix_to_postfix(expected_postfix, prefix, converter):
    assert converter.convert_to_postfix(prefix) == expected_postfix
