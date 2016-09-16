""" This script gets the table with the twitter data from sql, and loads it into a format that is readable by pythin
by using json to convert each line into a dictionary)"""


import pyodbc
import json

# DSN means data source name
connection = pyodbc.connect('DSN=kubricksql')
cursor = connection.cursor()

cursor.execute('select Tweet from dbo.Friday1609')

rows = cursor.fetchall() # gets all the rows from the tweet column

tweet_list =[]

# This creates a list of dictionaries
for r in rows:
    tweet_list.append(json.loads(r[0]))




