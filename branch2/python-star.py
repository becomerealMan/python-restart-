#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:39:34 2021

@author: idohyeon
"""


rows=int(input("열의 개수:"))
print("역삼각형 패턴")

i=1
while(i<=rows):
    j=1
    while(j<=rows):
        if(j<i):
            print('',end=' ')
        else:
            print('*',end=' ')
        j=j+1
    i=i+1
    print()
# for i in range(1,rows + 1):
#     for j in r nage(1,rows+1):
#         if (j<=rows-i):
#             print('',end=' ')
#         else:
#             print('*',end=' ')
# print()            
# rows = int(input("Please Enter the Total Number of Rows  : "))

# print("Reverse Mirrored Right Triangle Star Pattern")
# i = 1
# while(i <= rows):
#     j = 1
#     while(j <= rows):
#         if(j < i):
#             print(' ', end = '  ')
#         else:
#             print('*', end = '  ')
#         j = j + 1
#     i = i + 1
#     print()