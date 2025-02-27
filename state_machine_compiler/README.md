# State machine compiler

[RU](#компилятор-конечных-автоматов)

The idea is for each state to have `next` function that will progress it to the next state. No need for anything more complicated, we just always progress further in our parser.

Usually descriptions of parsers are stored in a separate file and used in the main code. It's easier to deal with code generation in that way.

Also scm comes with `lib` directory, which contains code, that is used by the generated state machine. For simplicity I copied it here (`statemap.py`), no need to install it as a python library.

## How to generate

[`parser.sm`](./parser.sm) is a description of the state machine, from it scm generates [`parser_sm.py`](./parser_sm.py) which is used in the [`main.py`](./main.py), the actual parser.

```console
java -jar "path/to/Smc.jar" -python parser.sm
```

## How to run

```console
$ python main.py
(['821'], [])
(['55', '6', '88'], ['+', '-'])
([], [])
([], [])
```

You can easily see how the math expressions are split into their parts here. And how erronious inputs return just empty arrays.

# Компилятор конечных автоматов

Идея в том, чтобы для каждого состояния была функция `next`, которая переводит его в следующее состояние. Нет необходимости в чем-то более сложном, мы просто всегда движемся вперед в нашем парсере.

Обычно описание парсера хранятся в отдельном файле и импортируется в основной код. Так проще работать со сгенерированным кодом.

Также scm поставляется с папкой `lib`, которая содержит код, используемый сгенерированным конечным автоматом. Для простоты я скопировал его сюда (`statemap.py`), нет необходимости устанавливать его как библиотеку python.

## Как сгенерировать

[`parser.sm`](./parser.sm) - это описание конечного автомата, на основе которого scm генерирует [`parser_sm.py`](./parser_sm.py), который используется в [`main.py`](./main.py) - парсере.

```console
java -jar "path/to/Smc.jar " -python parser.sm
```

## Как запустить

```console
$ python main.py
(['821'], [])
(['55', '6', '88'], ['+', '-'])
([], [])
([], [])
```

Как видите, математические выражения разделяются на состовляющие их части. И как вводные данные с ошибками превращаются в пустые массивы.
