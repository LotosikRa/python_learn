"""
Написать фрагмент python кода, который будет находить в строке var_string подстроку, упорядоченною в алфавитном порядке, максимальной длины. Если длины строк совпадают печатаем первую найденную.

Пишите свой код в следующем окне, предполагая, что var_string уже определена. Описываете логику и не забываем печатать результат return longest

Пример
var_string = "sabrrtuwacaddabra"
longest = "abrrtuw"
"""

def substring_sorted(var_string):
    var_string = var_string.lower()
    lv = len(var_string)

    def tffor2(s1, s2):  # будет определять стоят ли две буквы в правильном порядке
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        i1 = 26
        i2 = 26
        for a1 in alphabet:  # назначает номер первой
            if s1 == a1:
                s1 = i1
            i1 -= 1
        for a2 in alphabet:      # назначает номер второй
            if s2 == a2:
                s2 = i2
            i2 -= 1
        if s1 >= s2:  # определяет последовательность
            return True
        else:
            return False

    def maxl(l1,l2):  # возвращает максимальную из двух.
        if l1 < l2:
            return l2
        else:
            return l1

    def maxs(mj,j0):  #определяю первый символ максимальной строки
        if l1 < l2:
            return j0
        else:
            return mj

    j0 = 0  #индекс (порядковй номер) буквы
    l1 = 0  #изначально максимальная длина равна 0
    mj = 0  #изначально символ с максимальной длиной подстроки равен 0
    for s0 in var_string[:-1]:
        j = j0  # j будет меняться для определения длины
        l2 = 0  # для каждой буквы длина изначально равна 0
        s1 = s0
        s2 = var_string[j0+1]
        while tffor2(s1,s2):  # находим длину подстроки
            l2 += 1
            if j == lv-1:  # чтобы не выходить за пределы строки
                break
            s1 = s2
            s2 = var_string[j+1]  #ERROR
            j += 1
        j0 += 1
        mj = maxs(mj,j0)  # находит символ с максимальной строкой
        l1 = maxl(l1,l2)  # находит длинейшую строку

    mstr = var_string[mj-1:mj+l1-1]
    return mstr


if __name__=='__main__':
    # проверка результатов
    assert substring_sorted(''), ''
    assert substring_sorted('longestsubstringinalphabeticalorderis'), 'abet'
    assert substring_sorted('longestsubstringinalphabeticalloorderis'), 'alloor'
    assert substring_sorted('longestsubstringinalphabeticalorderismosty'), 'mosty'