"""
Написать фрагмент python кода, который модифицирует строку чисел var_string следующим образом:
- в начале строки идут нечетные числа в порядке возрастания
- далее идут четные числа в порядке убывания и выводит на печать измененную строку var_string.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику выполнения и не забывайте возращать результат return change_string

Пример
var_string = '1486371'
change_string = '1137864'
"""

def string_changer(var_string):
    new = ""
    _0k = 0
    _1k = 0
    _2k = 0
    _3k = 0
    _4k = 0
    _5k = 0
    _6k = 0
    _7k = 0
    _8k = 0
    _9k = 0
    _0 = '1'
    _1 = "3"
    _2 = "5"
    _3 = '7'
    _4 = '9'
    _5 = '8'
    _6 = '6'
    _7 = '4'
    _8 = '2'
    _9 = '0'

    for n in str(var_string):
        if n == _0:
            _0k += 1
        elif n == _1:
            _1k += 1
        elif n == _2:
            _2k += 1
        elif n == _3:
            _3k += 1
        elif n == _4:
            _4k += 1
        elif n == _5:
            _5k += 1
        elif n == _6:
            _6k += 1
        elif n == _7:
            _7k += 1
        elif n == _8:
            _8k += 1
        else :
            _9k += 1

    new = _0*_0k + _1*_1k + _2*_2k + _3*_3k + _4*_4k + _5*_5k + _6*_6k + _7*_7k + _8*_8k + _9*_9k
    return var_string


if __name__=='__main__':
    # проверка результатов
    assert string_changer(''), ''
    assert string_changer('4'), '4'
    assert string_changer('7'), '7'
    assert string_changer("0987654321"), 1357986420
    assert string_changer("712023334454480"), 133357844442200