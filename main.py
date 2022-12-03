"""Văn Ngọc Công Sang"""
"""MSSV:0950080111"""
"""Lớp: 09CNTT03"""

"""Bai1"""
# t = int(input("Nhập số test: "))
# lst = []
# if 0 < t <= 100:
#        for i in range(1, t+1):
#               lst.append(input("Input: "))
# for i in range(t):
#        print(f"Test {i} : \n", lst[i].title())

"""Bai 2"""
# nguyenam=0
# phuam=0
# t = int(input("Nhập số test: "))
# lst = []
# if 0 < t <= 100:
#        for i in range(1, t+1):
#               lst.append(input("Input: "))
#
#
# for i in range(t):
#     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
#                     or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#                 nguyenam = nguyenam + 1
#     else:
#                 phuam = phuam + 1
#     print(f"text {i}:",end="\n")
#
#     print(f"{nguyenam}", end="\n")
#     print(f"{phuam}", end="\n")

#
# """bai 3"""
# def a():
#     str = input("Nhập chữ: ")
#     word = str.split()
#     return len(word)
#
#
# t = int(input("Nhập so text: "))
# if 0 < t <= 100:
#     for i in range(t):
#         print(f"Test {i+1}: {a()}")
#
# """bai 4"""
# t = int(input("Nhập số text: "))
# if t > 0 and t <= 100:
#     for i in range(1, t + 1):
#         str_word = input("Nhập chữ: ")
#         print(str_word.replace("\t", " "))

"""bai 6"""
# def thay_the(s1, s2, s3):
#     print(s1.replace(s2, s3))
#
#
# m = int(input("nhập vào số lần thực hiện: "))
# if 0 < m <= 100:
#     for i in range(m):
#         s1 = input("nhập chuỗi vào đây: ")
#         s2 = input("nhập chuỗi thay thế cũ: ")
#         s3 = input("nhập chuỗi thay thế mới: ")
#         print(f"test {i + 1}:", end="\n")
#         thay_the(s1, s2, s3)
# """cau 7"""
# n = int(input("nhap so text: "))
# for i in range(1, n+1):
#     word = [x for x in input().split()]
#     s = set()
#     print(f"test {i}: ")
#     for i in range:
#         if i not in s:
#             print(f'{i} ', end='')
#             s.odd(i)
#     print()
#
#
# """cau 8"""
# def dem_tu(s1):
#     str = s1.split(" ")
#     count = {}
#     for i in str:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     for i in sorted(count, key=count.get, reverse=False):
#         print(f"{i}-{count[i]}")
#
# r = int(input("nhập vào số lần: "))
# if 0 < r <= 100:
#     for i in range(r):
#         s1 = input("nhập chuỗi: ")
#         print(f"test {i + 1}:", end="\n")
#         dem_tu(s1)
