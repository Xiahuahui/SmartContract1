class Settings:
    def __init__(self):
        self.DEBUG =True
        self.mode = "db"
        self.dbConfig={
        	'local':{
			    'host':"localhost",
				'user':'root',
				'passwd':"hjs123456",
				'database':"smartContractTree"
        	}
        }
        self.DFA=True
settings = Settings()