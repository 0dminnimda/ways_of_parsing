# Lexer generator

[RU](#генератор-лексеров)

Usually descriptions of parsers are stored in a separate file and used in the main code. It's easier to deal with code generation in that way.

This is the example for re2c, look into it's docs: https://re2c.org/manual/manual.html

## How to generate

[`parser.re`](./parser.re) is a description of the parser, from it re2c generates [`parser.py`](./parser.py) which is the actual parser.

```console
path/to/re2c parser.re --lang python -o parser.py
```

Or you can just use their online playground: https://re2c.org/playground and copy paste the code, no need to install anything

## How to run

```console
$ python main.py
821 -> ['821'] []
55+6-88 -> ['55', '6', '88'] ['+', '-']
821g -> [] []
55+6-h -> [] []
```

You can easily see how the math expressions are split into their parts here. And how erronious inputs return just empty arrays.

# Генератор лексеров

Обычно описание парсера хранятся в отдельном файле и импортируется в основной код. Так проще работать со сгенерированным кодом.

Этот пример использует re2c, вот документация: https://re2c.org/manual/manual.html

## Как сгенерировать

[`parser.re`](./parser.re) — это описание парсера, из него re2c генерирует [`parser.py`](./parser.py), который и является фактическим парсером.

```console
path/to/re2c parser.re --lang python -o parser.py
```

Также можно просто сгенерировать онлайн: https://re2c.org/playground и ничего устанавливать не нужно

## Как запустить

```console
$ python main.py
821 -> ['821'] []
55+6-88 -> ['55', '6', '88'] ['+', '-']
821g -> [] []
55+6-h -> [] []
```

Как видите, математические выражения разделяются на состовляющие их части. И как вводные данные с ошибками превращаются в пустые массивы.
