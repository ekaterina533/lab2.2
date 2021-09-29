#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
 s = input("Введите слово, или предложение:")
 count = 0
 a = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
 if c in s.intersection(a):
  count= count+1
 print("Количество гласных равно:",count)

