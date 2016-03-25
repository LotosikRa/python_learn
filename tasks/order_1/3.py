"""
Подсчет гласный букв 'a', 'e', 'i', 'o', 'u' в строке "Python hAs an amazing fEature" . Программа не чувствительная к регистру.
"""

def counter(text):
    count_this = 'aeiou'
    text = text.lower()
    counted = sum(text.count(char) for char in count_this)
    return counted


if __name__=='__main__':
    # проверка результатов
    assert counter('Python hAs an amazing fEature') == 10
    assert counter('Miss you my Dear friend!"') == 7