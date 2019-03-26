import MySQLdb
from tqdm import tqdm

def InsertData(sql):
<<<<<<< HEAD
	con = MySQLdb.connect('172.17.0.2','euromillon_user','Inicio15','EUROMILLON_DB')
=======
	con = MySQLdb.connect('192.168.137.131','euromillon_user','Inicio15','EUROMILLON_DB')
>>>>>>> origin/master
	cur = con.cursor()

	for i in tqdm(range(len(sql))):
		try:
			cur.execute(sql[i])
			con.commit()
		except:
			con.rollback()
			print("Hay algun error, ejecutamos rollback")

	con.close()
