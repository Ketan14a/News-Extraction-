# importing pymongo for feeding News in MongoDB
from pymongo import MongoClient
import json

# Eastablishing the Connection 
db_client = MongoClient('localhost', 27017)

# Creating a Fresh Database for Storing News
db = db_client['news_db']

# Creating a Fresh Collection which acts analogous to a table in Relational DBMS
News_Collection = db['my_news_collection']


# Importing Tweets from JSON file into a list of dictionaries
news = []
count=0
for line in open('Cleaned_News.json', 'r'):
	try:
		news.append(json.loads(line))
	except Exception as e:
		print()
    
    

# Refershing the Collection Values
News_Collection.remove()

# Stotring the News into MongoDB
result = News_Collection.insert_many(news)


# Closing the MongoDB Connection
db_client.close()