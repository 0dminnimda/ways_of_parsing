from parser import get_math_expr_parts

if __name__ == "__main__":
    for case in "821", "55+6-88", "821g", "55+6-h":
        nums, ops = get_math_expr_parts(case)
        print(case, "->", nums, ops)
