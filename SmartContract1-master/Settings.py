class Settings:
    def __init__(self):
        self.DEBUG =True
        self.mode = "d"
        self.dbConfig={
        	'local':{
			    'host':"localhost",
				'user':'root',
				'passwd':"hjs123456",
				'database':"smartContractTree",
                'auth_plugin':"mysql_native_password"
        	}
        }
        self.DFA=True
settings = Settings()
