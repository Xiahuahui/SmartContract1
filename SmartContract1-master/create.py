import xlrd
import util
import db
import json
def read_excel(filename,username):
    filename = './sample/contract/'+ filename + ".xlsx"
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    row = sheet.nrows
    col = sheet.ncols
    print("行数",row,"列数",col)
    contract_name = sheet.cell(1, 1).value
    print(contract_name)
    contract_id = util.get_id(username, contract_name)
    party_a = sheet.cell(2, 2).value
    print(party_a)
    sig_a = "lll"
    party_b = sheet.cell(3, 2).value
    print(party_b)
    sig_b = "lll"
    valid_time = "2019-08-14"
    object_desc = ''
    content = []
    for i in range(8,row):
        res = {}
        res['person'] = sheet.cell(i, 1).value
        res['premise'] = sheet.cell(i, 2).value
        res['res'] = sheet.cell(i, 3).value
        res['time'] = ""
        print(sheet.cell(i, 3).value)
        content.append(res)
    print(content)
    db.save_contract(username, contract_name, contract_id, party_a, sig_a,
                     party_b, sig_b, valid_time, object_desc,
                     json.dumps(content))

if __name__ == '__main__':
    filename = input("输入合同的名称：")
    username = input("输入用户姓名：")
    read_excel(filename,username)
