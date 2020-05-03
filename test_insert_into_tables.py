#!/usr/bin/python3
# coding: utf-8
import os
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

from constant import*
from methodes import*

'''Ici j'ai mis que 7 colonnes car la première est  en "AUTO_INCREMENT":   `idproducts` INT(15) NOT NULL AUTO_INCREMENT,'
cela signifie qu'a chaque fois qu'on fait appele à cette methode d'ajout de produit -->
on ajoute à la suite et la colonne "idproducts" s'incrémente de façon automatique'
'''

data = [{
		'stores': 'Magasins U,Bi1', 
		'code': '3045320008401', 
		'quantity': '350 g e', 
		'url': 'https://fr.openfoodfacts.org/produit/3045320008401/confiture-allegee-fraises-andros',
		'ingredients_text_fr': 'fraises, sucre, gélifiant : pectine de fruits.', 
		'brands': 'Andros', 
		'product_name_fr': 'Confiture Allégée Fraises', 
		'nutrition_grade_fr': 'c', 
		'generic_name_fr': 'Confiture extra de fraises allégée en sucres'
			}, 
		{'product_name_fr': 'Confiture fraise Intense', 
		'brands': 'Bonne Maman', 
		'generic_name_fr': 'Confiture extra de fraises allégée en sucres', 
		'nutrition_grade_fr': 'c', 
		'quantity': '335 g', 
		'code': '3608580823445', 
		'stores': 'Intermarché, Magasins U', 
		'ingredients_text_fr': 'Fraises, sucre, jus de cassis, jus de citrons concentré, gélifiant : pectine de fruits', 
		'url': 'https://fr.openfoodfacts.org/produit/3608580823445/confiture-fraise-intense-bonne-maman'
			}, 
		{'product_name_fr': 'Confipote Fraise', 
		'brands': 'Materne', 
		'generic_name_fr': 'Confiture de fraises allégée en sucres', 
		'nutrition_grade_fr': 'c', 'quantity': '350 g', 
		'code': '3021762383306', 
		'stores': 'Auchan,Carrefour,Magasins U', 
		'ingredients_text_fr': "fraises 68,5%, sucre, gélifiant: pectine de fruit, acidifiant: acide citrique, correcteur d'acidité: citrate de calcium.", 
		'url': 'https://fr.openfoodfacts.org/produit/3021762383306/confipote-fraise-materne'
			}]


				
if __name__ == "__main__":

	add_products_for_multiple_category()
	
	
