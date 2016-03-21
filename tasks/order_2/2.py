"""
Написать фрагмент python кода, который будет находить в строке var_string подстроку, упорядоченною в алфавитном порядке, максимальной длины. Если длины строк совпадают печатаем первую найденную.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику и не забываем печатать результат return longest

Пример
var_string = "sabrrtuwacaddabra"
longest = "abrrtuw"
"""

def substring_sorted(var_string):
    return


if __name__=='__main__':
    # проверка результатов
    assert substring_sorted(''), ''
    assert substring_sorted('longestsubstringinalphabeticalorderis'), 'abet'
    assert substring_sorted('longestsubstringinalphabeticalloorderis'), 'alloor'
    assert substring_sorted('longestsubstringinalphabeticalorderismosty'), 'mosty'