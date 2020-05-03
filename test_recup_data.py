#!/usr/bin/python3
# coding: utf-8
import os
import mysql.connector
import requests
import json
from mysql.connector import errorcode

from constant import *
from methodes import *

	
if __name__ == "__main__":
	
	get_data_from_offdb ()
