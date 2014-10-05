#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys, api, time

db_host = 'localhost'
usuario = 'YOUR_MYSQL_USER_HERE'
clave = 'YOUR_MYSQL_PASS_HERE'
base_de_datos = 'YOUR_DB_NAME_HERE'
db = mdb.connect(host=db_host, user=usuario, passwd=clave,db=base_de_datos)

# Hago listado de las peliculas en la db de tmdb: pelis_a
with db:
	cur = db.cursor()
	cur.execute("SELECT * FROM test")
	rows = cur.fetchall()
	pelis_a = []
	for row in rows:
		pelis_a.append(int(row[0]))
	a = set(pelis_a)

# Hago listado de las peliculas en la db de pelis: pelis_b
with db:
	cur = db.cursor()
	cur.execute("SELECT * FROM pelis")
	rows = cur.fetchall()
	pelis_b = []
	for row in rows:
		j = int(row[10])
		# el id 0 no lo anexo
		if j == 0:
			pass
		else:
			pelis_b.append(j)
	b = set(pelis_b)

# Obtengo las diferencias (id de pelis que no existen en tmdb)
# c = a - b
c = b.difference(a)

# Creo el fichero lista_c.txt
file_wget = open('lista_c.txt','a')
for i in c:
	try:
	    path1 = api.api2img(i,'poster_path')
	    file_wget.write(str(path1) + '\n')
	    path2 = api.api2img(i,'backdrop_path')
	    file_wget.write(str(path2) + '\n')
	    time.sleep(0.5)
	except:
		pass
file_wget.close()

# Inserto los datos de lista_c en la db de tmdb
with db:
	cur = db.cursor()
 	for i in c:
 		try:
	 		id_w = i
	 		backdrop_path_w = api.api2data(i,'backdrop_path')[1:]
	 		genres_w = api.api2data(i,'genres')	
	 		original_title_w = api.api2data(i,'original_title')
	 		poster_path_w = api.api2data(i,'poster_path')[1:]
	 		release_date_w = api.api2data(i,'release_date')
	 		runtime_w = api.api2data(i,'runtime')
	 		title_w = api.api2data(i,'title')
	 		vote_average_w = api.api2data(i,'vote_average')
	 		#values_w = (i, backdrop_path_w, genres_w, original_title_w, poster_path_w, release_date_w, runtime_w, title_w, vote_average_w)
	 		values_w = (i, backdrop_path_w, poster_path_w, title_w)
	 		cur.execute("INSERT INTO test VALUES(%s, %s, %s, %s)", values_w)
		except:
			pass