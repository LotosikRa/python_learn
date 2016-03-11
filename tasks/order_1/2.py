"""
Реализовать возврат строки оставляя только каждый 3 символ
Пример:
original = '123456 7 890 abc'
change = '36 0b'
Исходные данные:
original = "123123abc 2311 a c"
change =
"""

def changer(text):
    result = ''  # напсать код здесь
    return result


if __name__=='__main__':
    # проверка результатов
    assert changer('123456 7 890 abc') == '36 0b'
    assert changer('123123abc 2311 a c"') == '33c3 c'