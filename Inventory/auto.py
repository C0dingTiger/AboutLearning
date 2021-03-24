#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-02 11:55:03
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
# import xlrd 
import openpyxl
import pandas as pd

# book = xlrd.open_workbook("test.xls")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
# sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=3, colx=3)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))

print(os.listdir("."))

excel = pd.read_excel('test.xlsx',engine='openpyxl')
print(excel)
