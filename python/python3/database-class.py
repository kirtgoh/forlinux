#!/usr/bin/python3

import sqlite3

class database():

	def __init__(self, **kwargs):
		self.filename = kwargs.get('filename', 'test.db')
		self.table = kwargs.get('table', 'test')

	def __iter__(self):
		cursor = self._db.execute('select * from {} order by t1'.format(self._table))
		for row in cursor:
			yield dict(row)
		
	def sql_do(self, sql, *params):
		self._db.execute(sql, params)
		self._db.commit()

	def insert(self, row):
		self._db.execute('insert into {} (t1, i1) values (?, ?)'.format(self._table), (row['t1'], row['i1']))
		self._db.commit()

	def retrieve(self, t1):
		cursor = self._db.execute('select * from {} where t1 = (?)'.format(self._table), (t1,))
		return dict(cursor.fetchone())

	def update(self, row):
		self._db.execute('update {} set i1 = ? where t1 = ?'.format(self._table), (row['i1'], row['t1']))
		self._db.commit()

	def delete(self, t1):
		self._db.execute('delete from {} where t1 = ?'.format(self._table), (t1,))
		self._db.commit()

	@property
	def filename(self):
		return self._filename

	@filename.setter
	def filename(self, name):
		self._filename = name

		# create database
		self._db = sqlite3.connect(self._filename)

		# determine how the row will be returned
		self._db.row_factory = sqlite3.Row

	@filename.deleter
	def filename(self):
		self.close()

	@property
	def table(self):
		return self._table

	@table.setter
	def table(self, t):
		self._table = t 

	@table.deleter
	def table(self):
		self._table = 'test'

	def close(self):
		self._db.close()
		del self._filename

def main():

	db = database(filename = 'test.db', table = 'test')

	# create table
	print('Create table test')
	db.sql_do('drop table if exists test')
	db.sql_do('create table test (t1 text, i1 int)')

	print('Create rows')
	db.insert(dict(t1 = 'one', i1 = 1))
	db.insert(dict(t1 = 'two', i1 = 2))
	db.insert(dict(t1 = 'three', i1 = 3))
	db.insert(dict(t1 = 'four', i1 = 4))
	for row in db: print(row)

	print('Retrieve rows')
	print(db.retrieve('one'), db.retrieve('two'))

	print('Update rows')
	db.update(dict(t1 = 'one', i1 = 101))
	db.update(dict(t1 = 'four', i1 = 402))
	for row in db: print(row)
    
	print('Delete rows')
	db.delete('one')
	db.delete('two')
	for row in db: print(row)

if __name__ == '__main__':
	main()

