# индивидуальное задание вариант 18
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
 u = set("abcdefghiIjklmnopqrstuvwxyz")
 a = {"b", "c", "g", "I", "w"}
 b = {"e", "g", "h", "q", "w"}
 c = {"c", "d", "k", "l", "y"}
 d = {"a", "g", "h", "u", "v", "z"}
 x = (a.intersection(c)).union(b)
 print(f"x = {x}")
 bn = u.difference(a)
 cn = bn.intersection(d)
 y = cn.union(c.difference(b))
 print(f"y = {y}")
