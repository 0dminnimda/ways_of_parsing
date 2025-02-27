# to allow multiple captures per group
import regex as re  # pip install regex


NUM = r"([0-9]+)"
OP = r"([+-])"
# ?: makes group not capture, we already capture num and op separately, no need for joint capture
PAIRS = r"(?:" + OP + NUM + r")*"
RE = r"^" + NUM + PAIRS + r"$"
# or
r"^([0-9]+)(?:([+-])([0-9]+))*$"
#  group1     group2 group3


# cache regular expression to reuse it
PATTERN = re.compile(RE)


def get_math_expr_parts(text: str) -> tuple[list[str], list[str]]:
    match = PATTERN.match(text)
    if match is None:
        return [], []
    return match.captures(1) + match.captures(3), match.captures(2)


if __name__ == "__main__":
    for case in "821", "55+6-88", "821g", "55+6-h":
        nums, ops = get_math_expr_parts(case)
        print(case, "->", nums, ops)
