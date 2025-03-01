# Regular expressions

[RU](#регулярные-выражения)

A very nice place to explore them is regex101.com  
Also here is a good guide: https://docs.python.org/3/howto/regex.html  

Python built-in regular expression library does not support capturing multiple strings per group,
that's why I used third-party library `regex` in this example. It just add functionality,
so if you know built-in `re`, you already can use `regex`.

## How to run

```console
$ python main.py
821 -> ['821'] []
55+6-88 -> ['55', '6', '88'] ['+', '-']
821g -> [] []
55+6-h -> [] []
```

You can easily see how the math expressions are split into their parts here. And how erronious inputs return just empty arrays.

# Регулярные выражения

Хороший сайт, чтобы исследовать регулярки это regex101.com  
А вот хороший гайд: https://docs.python.org/3/howto/regex.html  

Встроенная библиотека регулярных выражений Python не поддерживает захват нескольких строк для одной группы,
поэтому я использовал стороннюю библиотеку `regex` в этом примере. Она просто добавляет функциональность,
поэтому если вы знаете встроенную `re`, вы уже можете использовать `regex`.

## Как запустить

```console
$ python main.py
821 -> ['821'] []
55+6-88 -> ['55', '6', '88'] ['+', '-']
821g -> [] []
55+6-h -> [] []
```

Как видите, математические выражения разделяются на состовляющие их части. И как вводные данные с ошибками превращаются в пустые массивы.
