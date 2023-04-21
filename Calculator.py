# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B4CBmMkMGt6W_3CQnujxtynWwlyFB8MI
"""

# Калькулятор

print('q в качестве знака операции завершения программы')

while True:
  s = input('Введи знак (+, -, *, /, %:)')
  if s == 'q':
    break
  if s in ('+', '-', '*', '/', '%'):
    try:
      x = float(input('x ='))
      y = float(input('y ='))
    except ValueError:
      print('Вводи числа!')
      x = float(input('x ='))
      y = float(input('y ='))
    if s == '+':
      print('%.2f' % (x+y))
    elif s == '-':
      print('%.2f' % (x-y))
    elif s == '*':
      print('%.2f' % (x*y))
    elif s == '/':
      if y != 0:
        print('%.2f' % (x/y))
      else:
        print('Делить на 0 нелльзя!')
    elif s == '%':
      print("x - число, от которого берем процент")
      print("н - процент, который берем")
      print('%.2f' % (x/100*y))
  else:
    print('Неверный знак операции')