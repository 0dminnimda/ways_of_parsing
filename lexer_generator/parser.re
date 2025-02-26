def get_math_expr_parts(text: str) -> tuple[list[str], list[str]]:
    # mark an end with null terminator
    yyinput = text.encode("ascii") + b"\0"
    yycursor = 0  # index

    # list of saved indices
%{mtags format = '\n    @@ = []'; %}

%{
    re2c:YYMTAGP = "@@.append(yycursor)";
    re2c:YYMTAGN = ""; // do nothing
    re2c:yyfill:enable = 0;
    re2c:encoding:utf8 = 1;
    re2c:indent:top = 1;
    re2c:tags = 1;

    number = [0-9]+;
    op = [+-];
    pair = #pair_start op #pair_center number #pair_end;
    number @num_end pair* [\x00] {
        numbers = [text[:num_end]]
        ops = []
        for s, c, e in zip(pair_start, pair_center, pair_end):
            ops.append(text[s:c])
            numbers.append(text[c:e])
        return numbers, ops
    }
    * { return [], [] }
%}
