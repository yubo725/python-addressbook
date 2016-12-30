import sqlite3
from person import Person

class DBUtils:

	def __init__(self):
		self.DB_NAME = 'data.db3'
		self.TABLE_NAME = 'addressbook'
		pass

	def is_table_exists(self, table_name):
		conn = sqlite3.connect(self.DB_NAME)
		cur = conn.cursor()
		cur.execute('select count(*) from sqlite_master where type=? and name=?', ('table', ''.join(table_name)))
		item = cur.fetchone()
		result = True
		if item[0] == 0:
			result = False
		cur.close()
		conn.close()
		return result

	def create_table(self):
		if self.is_table_exists(self.TABLE_NAME):
			return False
		else:
			conn = sqlite3.connect(self.DB_NAME)
			cur = conn.cursor()
			cur.execute('''create table %s(
					id integer primary key autoincrement,
					name text not null,
					phonenumber text not null,
					address text
				)''' % self.TABLE_NAME)
			conn.commit()
			cur.close()
			conn.close()
			return True

	def add_record(self, person):
		if not isinstance(person, Person):
			return False
		else:
			conn = sqlite3.connect(self.DB_NAME)
			cur = conn.cursor()
			sql = 'insert into %s(name, phonenumber, address) values(?, ?, ?)' % self.TABLE_NAME
			cur.execute(sql, (person.name, person.phone, person.addr))
			conn.commit()
			cur.close()
			conn.close()
			return True

	def delete_record(self, record_id):
		if not isinstance(record_id, int):
			print 'record_id invalid!'
			return False
		else:
			conn = sqlite3.connect(self.DB_NAME)
			cur = conn.cursor()
			sql = 'delete from %s where id=%s' % (self.TABLE_NAME, record_id)
			cur.execute(sql)
			conn.commit()
			cur.close()
			conn.close()
			print 'delete record success!'
			return True

	def get_all_records(self):
		conn = sqlite3.connect(self.DB_NAME)
		cur = conn.cursor()
		cur.execute('select * from %s' % self.TABLE_NAME)
		result = []
		for row in cur:
			person = Person(row[1], row[2], row[3])
			person.id = row[0]
			result.append(person)
		cur.close()
		conn.close()
		return result

	def search(self, keyword):
		conn = sqlite3.connect(self.DB_NAME)
		cur = conn.cursor()
		query = '\'%' + keyword + '%\''
		sql = 'select * from %s where name like %s' % (self.TABLE_NAME, query)
		cur.execute(sql)
		result = []
		for row in cur:
			person = Person(row[1], row[2], row[3])
			person.id = row[0]
			result.append(person)
		cur.close()
		conn.close()
		return result