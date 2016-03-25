"""
написать программу которая будет выводить строку в обратном порядке
original = "I like this World"
result = "dlroW siht ekil I"
"""

def reverser(text):
    result = text[::-1]  # напсать код здесь
    return result


if __name__=='__main__':
    # проверка результатов
    assert reverser('I like this World') == 'dlroW siht ekil I'
    assert reverser('Love is ...') == '... si evoL'