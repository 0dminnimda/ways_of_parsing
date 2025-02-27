from parser_sm import Parser_sm, StateMap


class Parser:
    string: str
    index: int
    numbers: list[str]
    last_number: int
    ops: list[str]
    _fsm: Parser_sm

    def __init__(self):
        self.string = ""
        self.index = 0
        self.numbers = []
        self.last_number = -1
        self.ops = []
        self._fsm = Parser_sm(self)

    def prepare(self, string: str):
        self.string = string
        self.index = 0
        self.numbers.clear()
        self.last_number = -1
        self.ops.clear()
        self._fsm = Parser_sm(self)

    def peek(self) -> str:
        if self.index >= len(self.string):
            return ""
        return self.string[self.index]

    def consume(self):
        self.index += 1

    def start_number(self):
        self.last_number = self.index

    def end_number(self):
        self.numbers.append(self.string[self.last_number:self.index])

    def save_op(self):
        self.ops.append(self.string[self.index])

    def next(self):
        self._fsm.next()

    def get_state(self):
        return self._fsm.getState()

    def is_finished(self) -> bool:
        s = self.get_state()
        return (
            s is StateMap.unexpected or
            s is StateMap.end
        )

    def has_not_matched(self) -> bool:
        return self.get_state() is StateMap.unexpected


_parser = Parser()

def get_math_expr_parts(text: str) -> tuple[list[str], list[str]]:
    _parser.prepare(text)

    while not _parser.is_finished():
        # print(_parser.get_state()._name)
        _parser.next()

    if _parser.has_not_matched():
        return [], []
    return _parser.numbers, _parser.ops


if __name__ == "__main__":
    print(get_math_expr_parts("821"))
    print(get_math_expr_parts("55+6-88"))
    print(get_math_expr_parts("821g"))
    print(get_math_expr_parts("55+6-h"))
