#主要是系统的一些配置和读写文件
import json
import datetime
import hashlib
import pickle
from datetime import datetime
class Settings:
    def __init__(self):
        self.DEBUG =True
        self.mode = "d"
        self.dbConfig={
            'nodelocal': {
                'host': "localhost",
                'user': 'root',
                'passwd': "123456xhh",
                'database': "smartContractTree",
                'auth_plugin': "mysql_native_password"
            },
        	'local':{
			    'host':"localhost",
				'user':'root',
                'port':"5100",
				'passwd':"123456xhh",
                'contractdatabase':"contract",
				'database':"smartContractTree",
                'auth_plugin':"mysql_native_password",
                'debug':"True",
        	}

        }
        self.DFA=True
    def get_id(self,username ,contract_name):
        str_now = datetime.now().strftime("%Y%m%d%H%M%S")
        str_id = username + contract_name + str_now
        str_hash = hashlib.sha256(str_id.encode()).hexdigest()
        return str_hash[-8:]

    def process_code(self,filename):
        st = ''
        with open('./data/code/' + filename, 'r') as fs:
            lines = fs.readlines()
            for line in lines:
                line = line.replace(' ', '&nbsp;&nbsp;')
                st = st + line.strip() + '<br>'
            return st
    def read_file(self,filename):
        with open(filename, 'r') as fs:
            data = json.load(fs)
        return data
#存储没有化简的状态机的结果
def saveResultToFile(DFA,dfaNodes,rootId,leavesIdsList,file):
    dfaResultDict = {
        'DFA': DFA,
        'dfaNodes': dfaNodes,
        'rootId' : rootId,
        'leavesIdsList' : leavesIdsList,
    }
    write_file = open(file, 'wb')
    pickle.dump(dfaResultDict, write_file)
    write_file.close()
#在多个条款时读取状态机的结果
def readResultFromFile(file):
    with open(file, 'rb') as f:
        dfaResult = pickle.load(f)
    return dfaResult
def saveChoiceToFile(choices,file):
    choicesResultDict = {
        'choices': choices,
    }
    write_file = open(file, 'wb')
    pickle.dump(choicesResultDict, write_file)
    write_file.close()
def readChoicesFromFile(file):
    with open(file, 'rb') as f:
        choicesResult = pickle.load(f)
    return choicesResult

settings = Settings()
