from typing import Callable
import sympy as sp

# Single variable Calculus

def get_derivative_sv_symbolic(math_formula: str, latex:bool=False) -> sp.Expr:
    """
    Calculate the symbolic derivative of a mathematical formula.

    Example:
        math_formula = "x**2 + 3*x + 2"
        result = get_derivative_symbolic(math_formula)
        print("Symbolic Difference Quotient:", result)

    Supported mathematical operations and symbols:
    - Basic arithmetic operations:
        + Addition (`+`): e.g., "x + 2"
        + Subtraction (`-`): e.g., "x - 3"
        + Multiplication (`*`): e.g., "x * 2"
        + Division (`/`): e.g., "x / 2"
        + Exponentiation (`**`): e.g., "x**2"
    - Functions:
        + Trigonometric functions: e.g., "sin(x)", "cos(x)", "tan(x)"
        + Exponential functions: e.g., "exp(x)"
        + Logarithmic functions: e.g., "log(x)", "log10(x)"
        + Square root: e.g., "sqrt(x)" or "x**(1/2)"
        + Absolute value: e.g., "abs(x)"
    - Special constants:
        + Pi: `sp.pi`
        + Euler's number: `sp.E`
    - Fractions and Decimals:
        + Fractions: e.g., "1/2", "3/4"
        + Decimals: e.g., "0.5", "3.14"
    - Variables and symbols:
        + Variables: e.g., "x", "y", "z"
    - Equality and Inequality:
        + Equal: e.g., "x == 2"
        + Not equal: e.g., "x != 2"
        + Less than: e.g., "x < 2"
        + Greater than: e.g., "x > 2"
    
    Parameters:
    - math_formula (str): The mathematical formula as a string.
    
    Returns:
    - sp.Expr: The simplified symbolic derivative of the input formula.
    """
    x = sp.symbols('x')
    dx = sp.symbols('dx')

    # Convert the input string expression to a sympy expression
    expression = sp.sympify(math_formula)

    # Calculate the difference quotient (f(x + dx) - f(x)) / dx
    difference_quotient = (expression.subs(x, x + dx) - expression) / dx

    # Simplify the expression
    simplified_quotient = sp.simplify(difference_quotient)

    limit_quotient = sp.limit(simplified_quotient, dx, 0)

    if latex == True:
        return sp.latex(limit_quotient)
    else:
        return limit_quotient


def get_derivative_sv_numeric(math_function: Callable[[float], float], x_val: float, dx: float=1e-5) -> float:
    """
    Calculate the numerical derivative of a mathematical function at a given point

    Example usage
        math_function = lambda x: x**2 + 3*x + 2 ()
        x_val = 2  # Point at which to evaluate the derivative
        result = get_derivative_numeric(math_function, x_val)
        # equal to
        result = get_derivative_numeric(lambda x: x**2 + 3**x), x_val)
        print("Numeric Difference Quotient:", result)
    """
    # Calculate the difference quotient numerically
    f_x_plus_dx = math_function(x_val + dx)
    f_x = math_function(x_val)

    difference_quotient = (f_x_plus_dx - f_x) / dx

    return difference_quotient