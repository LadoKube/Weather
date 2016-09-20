""" This script takes a table from sql and inserts each row as a document in a MongoDB collection"""

from twython import TwythonStreamer
import pyodbc
import json
from collections import defaultdict

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DSN means data source name
connection = pyodbc.connect('DSN=kubricksql')
cursor = connection.cursor()

cursor.execute('select Tweet from dbo.Tweeps')

rows = cursor.fetchall() # gets all the rows from the tweet column

tweet_listM =[]

for r in rows:
   tweet_listM.append(json.loads(r[0]))  # sql returns the table as a tuple, so need to refer to tuple element properly (r[0])

import pymongo

# create a mongo client
from pymongo import MongoClient
client = MongoClient()

# Going to create a test database for the purposes of this exercise
db = client.test_tweets

# create a weather database
db = client.weather
for i in range(len(tweet_listM)):
    db.tweets.insert_one(tweet_listM[i])


# Now we have copied the sql table into the mongoDB collection