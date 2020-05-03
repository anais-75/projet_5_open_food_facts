#!/usr/bin/python3
# coding: utf-8 
	
import operator
import mysql.connector
import requests
import json
from mysql.connector import errorcode
from constant import *
from methodes import *

# methods to connect to the database 

def init_cnx_mysql (user, password, host):
	cnx = mysql.connector.connect(user=user, password= password, host= host)
	return cnx

def close_cnx_mysql(cnx):
	cnx_mysql = cnx
	cnx_mysql.close()

def init_cursor_cnx ():
	cnx = init_cnx_mysql(USER_MYSQL, PASSWORD_MYSQL, HOST_MYSQL)
	cursor = cnx.cursor()
	return cursor

def close_cursor(cursor):
	#self.cursor = cursor
	cursor.close()

# we create our Database OffDB
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)        

# methode add  category in table category 
def insert_category (data):
	try:
		cnx = init_cnx_mysql(USER_MYSQL, PASSWORD_MYSQL, HOST_MYSQL)
		cursor = cnx.cursor()
		mySql_usedb= """USE offdb"""
		cursor.execute(mySql_usedb)
		
		mySql_insert_query = """ INSERT INTO category (idcategory,name) VALUES (%s,%s) """
                           
		cursor.executemany(mySql_insert_query, data)
		cnx.commit()
		print(cursor.rowcount, "Record inserted successfully into category table")

	except mysql.connector.Error as error:
		print("Failed to insert record into MySQL table {}".format(error))

	finally:
		if (cnx.is_connected()):
			cursor.close()
			cnx.close()
			print("MySQL connection is closed")

# methode sorting dictionary in order
def trie_dic (dic):
	mydict = {
	'brands': '',
	'code': '',
	'ingredients_text_fr': "", 
	'nutrition_grade_fr': '',
	'product_name_fr': '', 
	'quantity': '',
	'stores': '',
	'url': '',
	}
	
	for key in sorted(dic.keys()):

		if (key == 'brands'):
			 mydict['brands'] = dic[key]

		if (key == 'code'):
			 mydict['code'] = dic[key]
		
		if (key == 'ingredients_text_fr'):
			 mydict['ingredients_text_fr'] = dic[key]

		if (key == 'nutrition_grade_fr'):
			 mydict['nutrition_grade_fr'] = dic[key]			

		if (key == 'product_name_fr'):
			 mydict['product_name_fr'] = dic[key]

		if (key == 'quantity'):
			 mydict['quantity'] = dic[key]

		if (key == 'stores'):
			 mydict['stores'] = dic[key]	
				
		if (key == 'url'):
			 mydict['url'] = dic[key]
			 
		key, values =zip(*dic.items())
		
	return (mydict)

# method for adding products from one category	
def add_products_for_single_category (liste):
	try:
		cnx = init_cnx_mysql(USER_MYSQL, PASSWORD_MYSQL, HOST_MYSQL)
		cursor = cnx.cursor()
		mySql_usedb= """USE offdb"""
		cursor.execute(mySql_usedb)

		liste1 =[]
		liste2 =[]
		
		dic= {}
		dic1= {}
		
		for item in liste:
			dic = item	
			print ("TYPE_dic____: \n", type(dic1))			
			print ("DICT:\n", dic)
			dic1 = (trie_dic (dic))
			liste1.append(dic1)
		
		for item1 in liste1:
			dic1 = item1
			for key in sorted(dic1.keys()):
				key, values =zip(*dic1.items())
				print ("La FONCTION ZIP KEY:", key)
				print ("La FONCTION ZIP VALEURS:", values)
			liste2.append(values)
			print ("MA LISTE2:\n", liste2)
		add_product = """INSERT INTO products  (brands, code, ingredients_text_fr, nutrition_grade_fr, product_name_fr, quantity, stores, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
		
		cursor.executemany(add_product, liste2)
		cnx.commit()
		print(cursor.rowcount, "Record inserted successfully into Products table")
	
	except mysql.connector.Error as error:
		print("Failed to insert record into MySQL table {}".format(error))
	
	finally:
		if (cnx.is_connected()):
			cursor.close()
			cnx.close()
			print("MySQL connection is closed")

# method for adding products from multiple categories
def add_products_for_multiple_category():			
	m_list= get_data_into_offdb ()	
	for item in m_list :
		add_products_for_single_category (item)
		
			
# methode to add substitut 
def insert_substitute (data):
	try:
		cnx = init_cnx_mysql(USER_MYSQL, PASSWORD_MYSQL, HOST_MYSQL)
		cursor = cnx.cursor()
		mySql_usedb= """USE offdb"""
		cursor.execute(mySql_usedb)  

		mySql_insert_query = """INSERT INTO substitute (name,brand,nutriscore,url,ingredients,stores,barecode) 
                           VALUES ( %s, %s, %s, %s, %s, %s, %s) """
                           
		cursor.executemany(mySql_insert_query, data)
		cnx.commit()
		print(cursor.rowcount, "Record inserted successfully into Substitute table")

	except mysql.connector.Error as error:
		print("Failed to insert record into MySQL table {}".format(error))

	finally:
		if (cnx.is_connected()):
			cursor.close()
			cnx.close()
			print("MySQL connection is closed")


#get data by category
def get_data_by_category(category, nb):
	
	payload = {
		'action': 'process',
		'tagtype_0': 'categories',
		'tag_contains_0': 'contains',
		'tag_0': category,
		'tagtype_1': 'nutrition_grade',
		'tag_contains_1': 'contains',
		'fields': ','.join(FIELDS_API_PRODUCTS.keys()),
		'page_size': nb,
		'json': 'true'
	}
	req = requests.get(URL, params=payload)
	return req.json().get('products')

# methode to return list of product 	
def get_data_into_offdb ():
	liste =[]
	for key, value in CATEGORIES.items() :
		liste.append(get_data_by_category (value, NBR_PRODUCT))
	return liste
		
		
	
