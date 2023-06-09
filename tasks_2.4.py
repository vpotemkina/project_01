# -*- coding: utf-8 -*-
"""tasks_2.4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NjCoyO8Vq75P27ar7-JLTgjtb3KtzPl9
"""

# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
  if s != '':
    s1, s2 = '', ''
    i = 0
    for i in range(len(s)):
      if s[i] != '!':
        s1 += s[i]
#        print(i)
  else:
    print('Пустая строка!')
    return -1
  return s1
  pass

s = input("Введите строку:")
print('Результат работы ф-ции:', remove_exclamation_marks(s))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s != '':
      if s[-1] == '!':
        s = s[:-1]
    else:
      print('Пустая строка!')
      return -1
    return s 
    pass

s = input("Введите строку:")
print('Результат работы ф-ции:', remove_last_em(s))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    list_s = []
    s1 = ''
    if s != '':
      list_s = s.split(' ')
 #     print(list_s)
      for i1 in range(len(list_s)):
        count = 0
        for i2 in range(len(list_s[i1])):
#          print(list_s[i1][i2])
          if list_s[i1][i2] == '!':
            count = count + 1
        if count != 1:
          s1 = s1 + ' ' + list_s[i1]
    else:
      print('Пустая строка!')
      return -1
    return s1 
    pass

s = input("Введите строку:")
print('Результат работы ф-ции:', remove_word_with_one_em(s))