class Parser:
    string: str
    index: int
    numbers: list[str]
    ops: list[str]

    def __init__(self):
        self.string = ""
        self.index = 0
        self.numbers = []
        self.ops = []

    def prepare(self, string: str):
        self.string = string
        self.index = 0
        self.numbers.clear()
        self.ops.clear()

    def peek(self) -> str:
        if self.index >= len(self.string):
            return ""
        return self.string[self.index]

    def consume(self):
        self.index += 1

    def parse_number(self) -> bool:
        i = self.index
        while self.peek().isdigit():
            self.consume()

        s = self.string[i:self.index]
        if len(s) > 0:
            self.numbers.append(s)
            return True
        return False

    def parse_operator(self) -> bool:
        c = self.peek()
        if c == "+" or c == "-":
            self.consume()
            self.ops.append(c)
            return True
        return False

    def parse_expr(self) -> bool:
        if not self.parse_number():
            return False

        while self.peek() != "":
            if not self.parse_operator():
                return False

            if not self.parse_number():
                return False

        return True


_parser = Parser()

def get_math_expr_parts(text: str) -> tuple[list[str], list[str]]:
    _parser.prepare(text)
    if not _parser.parse_expr():
        return [], []
    return _parser.numbers, _parser.ops


if __name__ == "__main__":
    print(get_math_expr_parts("821"))
    print(get_math_expr_parts("55+6-88"))
    print(get_math_expr_parts("821g"))
    print(get_math_expr_parts("55+6-h"))
