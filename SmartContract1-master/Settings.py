class Settings:
    def __init__(self):
        self.DEBUG =True
        self.mode = "db"
        self.dbConfig={
        	'local':{
			    'host':"localhost",
				'user':'root',
				'passwd':"123456xhh",
				'database':"smartContractTree",
                'auth_plugin':"mysql_native_password"
        	}
        }
        self.DFA=True
settings = Settings()