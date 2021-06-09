#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def add(num1,num2):
#     return num1+num2

res = int(input())
while 1:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+': res += n;
    elif op == '-': res -= n;
    elif op == '*': res *= n;
    elif op == '/': res //= n;
print(res)


