"""
 Написать фрагмент python кода, который будет находить в строке text слова палиндромы (слова, читающиеся одинаково в обоих направлениях) и выводить на печать количество найденых слов.

Примечание
в строке могут быть знаки припинания , . : ; ! ? которые не должны влиять на результат
регистр в слове не имеет значения слово "sos" и "Sos" считается палиндромом.

Пишите свой код в следующем окне, предполагая, что text уже определена. Описываете логику выполнения и не забывайте печатать результат print palindromes

Пример
text = "Swedish pop group ABBA, single SOS unique occo both palindromes."
palindromes = 4
"""

def polindrome(text):
    l = len(text)
    text = text.lower()
    i = 0
    num = 0

    for s in str(text)[1:len(text)-1]:
        if (text[i-1] == ',' or text[i-1] == '.' or text[i-1] == ':' or text[i-1] == ';' or text[i-1] == '!' or text[i-1] == '?' or text[i-1] == ' ') and (text[i-1] == text[i+1]):
            num -= 1
        elif text[i-1] == text[i+1]:
            num += 1
        else:
            num += 0
        i += 1
    return text


if __name__=='__main__':
    # проверка результатов
    assert polindrome("Swedish pop group ABBA, single SOS unique occo both palindromes."), 4
    assert polindrome("I'am a good person who love peoples"), 0
    assert polindrome("SuPer AbBa Sos Dump Bump Love Star Allat Ra Spirit"), 2