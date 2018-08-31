# -*- coding: utf-8 -*-

num_b = 3

for i in range(3):
    num_a = 1
    for j in range(5):
        if num_a / num_b == 1:
            print('2', end = '')
        elif num_a / num_b == 5:
            print('2', end = '')
        elif num_a / num_b == 2 and num_b == 2:
            print('2', end = '')
        else:
            print('1', end = '')
        num_a += 1
    num_b -= 1
    print('')

#ちょ～汚えｗ
