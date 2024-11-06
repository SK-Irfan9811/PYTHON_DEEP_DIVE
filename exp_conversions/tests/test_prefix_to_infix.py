import pytest

from exp_conversions.prefix_to_infix import PrefixToInfix


@pytest.fixture
def converter():
    return PrefixToInfix()


@pytest.mark.parametrize('expected_infix,prefix_exp,', [
    ("(A+B)", "+AB"),  # Simple addition
    ("(A-B)", "-AB"),  # Simple subtraction
    ("(A*B)", "*AB"),  # Simple multiplication
    ("(A/B)", "/AB"),  # Simple division
    ("(A^B)", "^AB"),  # Exponentiation
    ("((A+B)-C)", "-+ABC"),  # Addition and subtraction
    ("(A+(B-C))", "+A-BC"),  # Parentheses
    ("((A+B)*C)", "*+ABC"),  # Multiplication of a sum
    ("(A+(B*C))", "+A*BC"),  # Operator precedence
    ("(A*(B+C))", "*A+BC"),  # Nested parentheses
    ("((A-B)/(C+D))", "/-AB+CD"),  # Division of differences
    ("((A+(B*C))-D)", "-+A*BCD"),  # Multiple operators
    ("(A^(B^C))", "^A^BC"),  # Right associative
    ("(((A+B)*C)-D)", "-*+ABCD"),  # Parentheses with subtraction
    ("(A+(-B))", "+A-B"),  # Negative variable
    ("(-(A+B))", "-+AB"),  # Unary minus with parentheses
    ("(((A-B)*C)+D)", "+*-ABCD"),  # Multiplication and addition
    ("((A+B)-(C-D))", "-+AB-CD"),  # Subtracting sums
    ("(A/(B*C))", "/A*BC"),  # Division of product
    ("((A+B)/(C-D))", "/+AB-CD"),  # Complex nested expressions
    ("(A^(B*C))", "^A*BC"),  # Exponentiation with product
    ("((A+B)-(C*D))", "-+AB*CD"),  # Mixed operations
    ("(A+(B*(C/(D^E))))", "+A*B/C^DE"),  # Complex with exponentiation
    ("((A+(B-(C/(D^E))))*F)", "*+A-B/C^DEF"),  # Provided example
    ("(-A)", "-A"),  # Unary minus before a single operand
    ("(A+(-B))", "+A-B"),  # Unary minus after operand
    ("(-(A-B))", "--AB"),  # Two unary minuses
    ("(A*(-B))", "*A-B"),  # Multiplication with unary minus
    ("(A+(B-(-C)))", "+A-B-C"),  # Nested unary with parentheses
    ("(-((A+B)*C))", "-*+ABC"),  # Unary operator affecting the whole expression
    ("(-(-A))", "--A"),  # Double negation
])
def test_prefix_to_infix(prefix_exp, expected_infix, converter):
    assert converter.convert_to_infix(prefix_exp) == expected_infix
