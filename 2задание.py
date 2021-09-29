#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
 a=input("Введите слово:")
 b=input("Введите ещё одно слово:")
 c = set(a).intersection(set(b))
 print(c)
