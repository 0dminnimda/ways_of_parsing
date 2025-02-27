# Hardwritten parser

[RU](#рукописный-парсер)

Here I return just `bool` on each parser rule (`parse_x()`), because it's a simple partser, if I were trying something more complicated, I may return a value, not just `bool`. Data is collected in the `Parser` class and returned by the function that `prepare`s the parser, not in a parser rule.

Also I made parser a global variable `_parser`, and just have `prepare` function, that is called each time when we start the parsing.

## How to run

```console
$ python main.py
(['821'], [])
(['55', '6', '88'], ['+', '-'])
([], [])
([], [])
```

You can easily see how the math expressions are split into their parts here. And how erronious inputs return just empty arrays.

# Рукописный парсер

Здесь я возвращаю только `bool` для каждого правила парсера (`parse_x()`), потому что это простой парсер, и если бы я попробовал что-то более сложное, я бы возвращал значение, а не просто `bool`. Данные собираются в классе `Parser` и возвращаются функцией, которая его подготавливает (`prepare`), а не в правилах.

Также я сделал парсер глобальной переменной `_parser` и просто добавил функцию `prepare`, которая вызывается каждый раз, когда мы начинаем синтаксический анализ.

## Как запустить

```console
$ python main.py
(['821'], [])
(['55', '6', '88'], ['+', '-'])
([], [])
([], [])
```

Как видите, математические выражения разделяются на состовляющие их части. И как вводные данные с ошибками превращаются в пустые массивы.
