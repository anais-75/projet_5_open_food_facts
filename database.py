#!/usr/bin/python3
# coding: utf-8
import os
import mysql.connector
from mysql.connector import errorcode

from constant import*
from methodes import*




if __name__ == "__main__":
	
	'''This script fil SQL allows to create an Offdb database if it does not 
	exist then creates and associates the tables Category, Product, Substitut
	'''
	with open('offdbscript.sql', "r") as fil:
		lines = fil.readlines()
		query =" ".join(lines)
		
	fil.close()
	
	cnx = init_cnx_mysql(USER_MYSQL, PASSWORD_MYSQL, HOST_MYSQL)
	cursor = cnx.cursor()
	
	try:
		cursor.execute("USE {}".format(DB_NAME))
	except mysql.connector.Error as err:
		print("Database {} does not exists.".format(DB_NAME))
		if err.errno == errorcode.ER_BAD_DB_ERROR:
			create_database(cursor)
			print("Database {} created successfully.".format(DB_NAME))
			cnx.database = DB_NAME

		else:
			print(err)
			exit(1)
	try:
		for result in cursor.execute(query, multi=True):
			pass
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
			print("already exists.")
		else:
			print(err.msg)
	else:
		print("OK")			

	close_cursor(cursor)
	close_cnx_mysql(cnx)
	cnx.disconnect()

	

	
