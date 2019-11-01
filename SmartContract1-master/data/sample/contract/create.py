import xlrd
from datetime import date,datetime
def read_excel(filename):
    filename = filename + ".xlsx"
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    row = sheet.nrows
    col = sheet.ncols
    print("行数",row,"列数",col)
    contract_name = sheet.cell(1, 1).value
    print(contract_name)
    party_a = sheet.cell(2, 2).value
    print(party_a)
    sig_a = "lll"
    party_b = sheet.cell(3, 2).value
    print(party_b)
    sig_b = "lll"
    valid_time = ""
    object_desc = ''
    content = []
    for i in range(8,row):
        res = {}
        res['person'] = sheet.cell(i, 1).value
        res['premise'] = sheet.cell(i, 2).value
        res['res'] = sheet.cell(i, 3).value
        res['time'] = ""
        content.append(res)
    print(content)

if __name__ == '__main__':
    read_excel("pw")
