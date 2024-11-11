import pytest

from exp_conversions.infix_to_prefix import InfixToPrefix


@pytest.fixture
def converter():
    return InfixToPrefix()


@pytest.mark.parametrize('infix,expected_prefix', [
    ("A+B", "+AB"),  # Simple addition
    ("A-B", "-AB"),  # Simple subtraction
    ("A*B", "*AB"),  # Simple multiplication
    ("A/B", "/AB"),  # Simple division
    ("A^B", "^AB"),  # Exponentiation
    ("A+B-C", "-+ABC"),  # Addition and subtraction
    ("A+(B-C)", "+A-BC"),  # Parentheses
    ("(A+B)*C", "*+ABC"),  # Multiplication of a sum
    ("A+B*C", "+A*BC"),  # Operator precedence
    ("A*(B+C)", "*A+BC"),  # Nested parentheses
    ("(A-B)/(C+D)", "/-AB+CD"),  # Division of differences
    ("A+B*C-D", "-+A*BCD"),  # Multiple operators
    ("A^B^C", "^A^BC"),  # Right associative
    ("(A+B)*C-D", "-*+ABCD"),  # Parentheses with subtraction
    ("A*-B*C", "**A-BC"),  # Unary operator
    ("-A+B", "+-AB"),  # Unary operator before variable
    ("A+(-B)", "+A-B"),  # Negative variable
    ("-(A+B)", "-+AB"),  # Unary minus with parentheses
    ("(A-B)*C+D", "+*-ABCD"),  # Multiplication and addition
    ("(A+B)-(C-D)", "-+AB-CD"),  # Subtracting sums
    ("A/(B*C)", "/A*BC"),  # Division of product
    ("(A+B)/(C-D)", "/+AB-CD"),  # Complex nested expressions
    ("A^(B*C)", "^A*BC"),  # Exponentiation with product
    ("A+B-C*D", "-+AB*CD"),  # Mixed operations
    ("A+(B*(C/D^E))", "+A*B/C^DE"),  # Complex with exponentiation
    ("-((A+B)*-(C+D))/(E^F)", "/-*+AB-+CD^EF"),  # More complex example
    ("(A+(B-(C/D^E)))*F", "*+A-B/C^DEF"),  # Provided example
    ("-A", "-A"),  # Unary minus before a single operand
    ("+A", "+A"),  # Unary plus before a single operand
    ("-A+B", "+-AB"),  # Unary minus with addition
    ("A+-B", "+A-B"),  # Unary minus after operand
    ("-A-B", "--AB"),  # Two unary minuses
    ("A*-B", "*A-B"),  # Multiplication with unary minus
    ("-A*B", "*-AB"),  # Multiplication where unary minus precedes operand
    ("-A+B*C", "+-A*BC"),  # Mixed unary with multiplication
    ("A+(B--C)", "+A-B-C"),  # Nested unary with parentheses
    ("(A+-B)*-C", "*+A-B-C"),  # Nested operations with unary operators
    ("A*(-B+C)", "*A+-BC"),  # Unary in parentheses
    ("-((A+B)*C)", "-*+ABC"),  # Unary operator affecting the whole expression
    ("--A", "--A"),  # Double negation
    ("A+-B+-C", "++A-B-C"),  # Multiple unary minuses
    ("-A+-B+-C", "++-A-B-C"),  # Unary minuses at the start
    ("-(A)+-(B)*-(C)", "+-A*-B-C"),  # Multiple unary with multiplication
])
def test_prefix_conversion(infix, expected_prefix, converter):
    actual_prefix = converter.convert_to_prefix(infix)
    print(converter.__dict__)
    assert actual_prefix == expected_prefix
