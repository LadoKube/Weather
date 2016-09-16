from twython import TwythonStreamer
import pyodbc
import json

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

connection = pyodbc.connect('DSN=sqldsn') # connect to a particular db using DSN
cur = connection.cursor() # Initializing a cursor

cur.execute("select tweets from dbo.Tweets") # Executing a query on that cursor

data = cur.fetchall() # gets all the rows

tweets =[]

# save the rows fetched in a list in json format
for row in data:
   tweets.append(json.loads(row[0])) # Cursor returns tuple, 0 is the first value(dict) in tuple

for t in tweets:
   pass
   # print t # loop through the  list and print

frame = DataFrame(tweets)
frame.split()