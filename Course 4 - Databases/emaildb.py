import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE counts (email TEXT, count INTEGER)''')

fname = input('Enter file name:')
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    