#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
 s = input("Введите слово, или предложение:")
 count = 0
 a = {'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'}
 for n in s:
    if n in a:
        count += 1
 print("Количество гласных равно:")
 print(count)

