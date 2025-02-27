from parser import get_math_expr_parts

if __name__ == "__main__":
    print(get_math_expr_parts("821"))
    print(get_math_expr_parts("55+6-88"))
    print(get_math_expr_parts("821g"))
    print(get_math_expr_parts("55+6-h"))
