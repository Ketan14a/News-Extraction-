# Importing PyMongo for accessing MongoDB
import pymongo

# Establishing the Connection to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["news_db"]
mycol = mydb["my_news_collection"]


# Accessing Tweets from MongoDB
for x in mycol.find():
  print("Source:"+x['Source_Name'])
  print("Author:"+str(x['Author']))
  print("Title:"+x['Title'])
  print("Description:"+x['Description'])
  print("Published Date:"+x['Published_Date'])
  print("Content:"+x['Content'])
  print()
  print()