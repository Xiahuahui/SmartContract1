import time
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user='root',
	passwd="hjs123456",
	database="smartContractTree"
	)
mycursor = mydb.cursor()

def timer(n):
	selectSql = "select count(*) from `Gnode`"
	mycursor.execute(selectSql)
	startnum = mycursor.fetchall()
	startnum = startnum[0][0]
	while(True):
		mycursor.execute(selectSql)
		endnum = mycursor.fetchall()
		endnum = endnum[0][0]
		print(startnum-endnum)
		startnum=endnum
		time.sleep(n)

if __name__ == '__main__':
	timer(1)
