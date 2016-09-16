""" This script
"""

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

tweet_list =[]

for r in rows:
   tweet_list.append(json.loads(r[0]))


print tweet_list[0]


