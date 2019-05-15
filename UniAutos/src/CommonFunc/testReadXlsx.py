#!/usr/bin/python
# -*- coding: utf-8 -*-



import xlrd

# 设置路径
path = 'nima.xlsx'
# 打开execl
workbook = xlrd.open_workbook(path)


# 输出Excel文件中所有sheet的名字
print(workbook.sheet_names())
# 根据sheet索引或者名称获取sheet内容
Data_sheet = workbook.sheets()[0]  # 通过索引获取
# Data_sheet = workbook.sheet_by_index(0)  # 通过索引获取
Data_sheet_find_byname = workbook.sheet_by_name(u'测试用例')  # 通过名称获取
print(Data_sheet.name,Data_sheet_find_byname)  # 获取sheet名称
rowNum = Data_sheet.nrows  # sheet行数
colNum = Data_sheet.ncols  # sheet列数
print(rowNum,colNum)
# 获取所有单元格的内容
x = []
for i in range(colNum):
    x.append(Data_sheet.cell_value(0,i))
print(x)
paramete = []
for i in range(1,rowNum):
    d = {}
    for z in range(colNum):
        d[x[z]]=Data_sheet.cell_value(i,z)
        paramete.append(d)
print(paramete)

list = []
for i in range(rowNum):
    rowlist = []
    for j in range(colNum):
        rowlist.append(Data_sheet.cell_value(i, j))
    list.append(rowlist)
print(list)
# 输出所有单元格的内容
for i in range(rowNum):
    for j in range(colNum):
        print(list[i][j], '\t\t', end="")
    print()
# 获取整行和整列的值（列表）
rows = Data_sheet.row_values(0)  # 获取第一行内容
cols = Data_sheet.col_values(1)  # 获取第二列内容
print (rows)
print (cols)
# 获取单元格内容
cell_A1 = Data_sheet.cell(0, 0).value
cell_B1 = Data_sheet.row(0)[1].value  # 使用行索引
cell_C1 = Data_sheet.cell(0, 1).value
cell_D2 = Data_sheet.col(1)[1].value  # 使用列索引
print(cell_A1, cell_B1, cell_C1, cell_D2)
# 获取单元格内容的数据类型
# ctype:0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print('cell(0,0)数据类型:', Data_sheet.cell(0, 0).ctype)
print('cell(1,0)数据类型:', Data_sheet.cell(1, 0).ctype)
print('cell(1,1)数据类型:', Data_sheet.cell(1, 1).ctype)
print('cell(1,2)数据类型:', Data_sheet.cell(1, 2).ctype)

# 获取单元格内容为日期的数据
# date_value = xlrd.xldate_as_tuple(Data_sheet.cell_value(1,0),workbook.datemode)
# print(type(date_value), date_value)
# print('%d:%d:%d' % (date_value[0:1]))