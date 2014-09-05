#!/usr/bin/python3

import sqlite3

def main():
	db = sqlite3.connect('test.db')
	# how the row will be returned
	db.row_factory = sqlite3.Row
	db.execute('drop table if exists test')
	db.execute('create table test (t1 text, i1 int)')
	db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
	db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
	db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
	db.execute('insert into test (t1, i1) values (?, ?)', ('four', 4))
	db.commit()

	cursur = db.execute('select * from test order by t1')
	for row in cursur:
		print(dict(row))

if __name__ == '__main__':
	main()

