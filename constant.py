#!/usr/bin/python3
# coding: utf-8 


# constants to use API Open Food Fact 
URL = 'https://fr.openfoodfacts.org/cgi/search.pl'
NBR_PRODUCT = 3

CATEGORIES = {
    'yaourts': 'Yaourts',
    'laits': 'Laits de vache',
    'chocolats': 'Chocolats noirs',
    'compotes':'Compotes',
    'gateaux' :'Gâteaux',
    'confitures':'Confitures'		
}

PRODUCT_ATTRIBUTES = {
        "category": "Catégorie",
        "brand": "Marque",
        "name": "Nom",
        "full_name": "Nom complet",
        "quantity": "Conditionnement",
        "nutriscore": "Nutriscore",
        "url": "Lien vers la fiche OpenFoodFacts",
        "ingredients": "Ingrédients",
        "stores": "Magasins"
    }

FIELDS_API_PRODUCTS = {
    'product_name_fr': 'name',
    'generic_name_fr': 'full_name',
    'brands': 'brand',
    'quantity': 'quantity',
    'url': 'url',
    'stores': 'stores',
    'nutrition_grade_fr': 'Nutri-Score',
    'ingredients_text_fr': 'ingredients',
    'category': 'category',
	'code': 'code'
    }

''' https://wiki.openfoodfacts.org/API/Read/Search#Parameters
    https://trello.com/c/fcb8gxe9/3-r%C3%A9cup%C3%A9ration-des-donn%C3%A9es-open-food-facts-au-format-json
'''	
PAYLOAD = {
            'action': 'process',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': CATEGORIES,
            'tagtype_1': 'nutrition_grade',
            'tag_contains_1': 'contains',
            'fields': ','.join(FIELDS_API_PRODUCTS.keys()),
            'page_size': 200,
			'json': 'true',
        }

#constants to use DB MySQL
DB_SCHEMA = 'offdb_script29032020.sql'

USER_MYSQL = 'yas'
PASSWORD_MYSQL = '!Yasmina01!'
HOST_MYSQL = '127.0.0.1'
DB_NAME = 'offdb'
TABLE_CATEGORY = 'category'
TABLE_PRODUCT = 'products'
TABLE_SUBSTITUTE = 'substitute'
