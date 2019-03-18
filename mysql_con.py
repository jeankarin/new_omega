import MySQLdb
from tqdm import tqdm

def InsertData(sql):
	con = MySQLdb.connect('192.168.137.131','euromillon_user','Inicio15','EUROMILLON_TEST_DB')
	cur = con.cursor()

	for i in tqdm(range(len(sql))):
		try:
			cur.execute(sql[i])
			con.commit()
		except:
			con.rollback()
			print("Hay algun error, ejecutamos rollback")

	con.close()