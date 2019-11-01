import mysql.connector      # pip install mysql-connector
from Settings import settings
class ContractRepository:
    def __init__(self):
        pass
    def get_connect(self):
        USER = settings.dbConfig['local']['user']
        PASSWORD = settings.dbConfig['local']['passwd']
        DATABASE =settings.dbConfig['local']['contractdatabase']
        conn = mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE)
        return conn

    def save_user(self,username, password):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute('insert into users(name, pass) values(%s, %s)', (username, password))
            conn.commit()
        except Exception as e:
            print(e)
            if conn:
                conn.rollback()
        finally:
            cursor.close()
            conn.close()
    def get_pass(self,username):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            # 这里使用(username)会报错
            cursor.execute('select pass from users where name = %s', (username,))
            password = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        if not password:
            return password
        else:
            return password[0][0]

    def save_contract(self,username, contract_name, contract_id, party_a, sig_a, party_b, sig_b, valid_time, object_desc, content):
        # calculate the contract_id
        #contract_id = util.get_id(username, contract_name)
        try:
            sql = "insert into contract_content(username, contract_name, contract_id, party_a, sig_a, party_b, sig_b, valid_time, object_desc, content)" + \
                "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql, (username, contract_name, contract_id, party_a, sig_a, party_b, sig_b, valid_time, object_desc, content))
            conn.commit()
        except Exception as e:
            print(e)
            if conn:
                conn.rollback()
        finally:
            cursor.close()
            conn.close()
    def get_user_contracts(self,username):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute('select contract_id, contract_name, party_a, party_b, valid_time, object_desc from contract_content where username = %s order by id desc', (username,))
            contracts = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return contracts


    def get_contract(self,username, contract_id):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute('select * from contract_content where username = %s and contract_id = %s', (username, contract_id))
            contracts = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        print("夏华辉")
        print(contracts)
        return contracts[0]

    def edit_contract(self,username, contract_name, contract_id, party_a, sig_a, party_b, sig_b, valid_time, object_desc, content):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute('delete from contract_content  where username = %s and contract_id = %s', (username, contract_id))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        self.save_contract(username, contract_name, contract_id, party_a, sig_a, party_b, sig_b, valid_time, object_desc,
                          content)
contractdb = ContractRepository()
if __name__ == '__main__':
    contract = ContractRepository()
    contract.save_user('xhh',123)