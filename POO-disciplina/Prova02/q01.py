import psycopg2
from moduloq01 import menu

host = '192.168.1.8'
dbname = 'mydb'
user = 'postgres'
passwd = 'mypwd'

conn_string = 'host={} user={} dbname={} password={}'.format(host, user, dbname, passwd)

conn = psycopg2.connect(conn_string)

if conn :
	print('Connection stablished\n')

menu(conn)
