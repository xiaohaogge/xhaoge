# coding=gbk
'''
    ��ģ�����ڶ�ȡxlsx�ļ��е�����������һ����������Ϊһ��case��
'''



class GetData():
    pass


from openpyxl.reader.excel import load_workbook


# def readXlsx(path):
#     # ���ļ�
#     file = load_workbook(filename=path)
#     # file.sheetnames��ȡ���й����������
#     sheets = file.sheetnames
#     # print(sheets)
#     # �ó�һ�����file[sheets[0]]  file[sheetname]
#     # sheet = file[sheets[0]]
#     # sheet.max_row ����
#     # sheet.max_column ����
#     # sheet.title ������
#     sheetsDic = {}
#     for sheetName in sheets:
#         sheet = file[sheetName]
#         sheetList = []
#         for lineNum in range(1, sheet.max_row + 1):
#             lineList = []
#             for columnNum in range(1, sheet.max_column + 1):
#                 value = sheet.cell(row=lineNum, column=columnNum).value
#                 lineList.append(value)
#             sheetList.append(lineList)
#
#         sheetsDic[sheetName] = sheetList
#     return sheetsDic
#
#
# if __name__ == "__main__":
#     print(readXlsx(r"test.xlsx"))

import xlrd

worksheet = xlrd.open_workbook('test.xlsx')   #��excel�ļ�

sheet_names= worksheet.sheet_names()    #��ȡexcel�����й�������

sheet1 = worksheet.sheet_by_name('Sheet1')    #����Sheet����ȡ����

sheet1 = worksheet.sheet_by_index(1)     #����������ȡ���ݣ�����Ϊ0��ʼ��1��ʾ��ȡ�ڶ��Ź���������

rows = sheet1.row_values(1)   #��ʾ��ȡSheet2�е�4������

cols10 = sheet1.col_values(1)   #��ʾ��ȡSheet2�е�10�����ݣ����ݱ���Ϊlist��

print(sheet1,rows,cols10)