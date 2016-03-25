"""
Подсчет гласный букв 'a', 'e', 'i', 'o', 'u' в строке "Python hAs an amazing fEature" . Программа не чувствительная к регистру.
"""

def counter(text):
    count_this = 'aeiou'
    # напсать код здесь
    counted = 0
    return counted


if __name__=='__main__':
    # проверка результатов
    assert counter('Python hAs an amazing fEature') == 10
    assert counter('Miss you my Dear friend!"') == 7