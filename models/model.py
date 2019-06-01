
import sqlite3
import bcrypt


def query(sql, intent='get'):
	con = sqlite3.connect('wireframe.db')
	cursor = con.cursor()
	cursor.execute(sql)
	if intent != 'get':
		con.commit()
		return True
	else:
		return cursor.fetchall()

def register(username, password):
	password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
	result = query("INSERT INTO account (username, password) VALUES ('{}','{}')".format(username, password.decode('utf-8')),"post")
	return result

def login(username, password):
	password = password.encode()
	try:
		hashed = query(f"select password from account where username = '{username}'")[0][0].encode()
		if bcrypt.checkpw(password, hashed):
			return True
		else:
			return False
	except:
		return False