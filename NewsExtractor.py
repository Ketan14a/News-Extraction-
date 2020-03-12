
# Importing the required libraries
import requests
import pandas as pd
import json


# Newsapi Credentials
url = "https://newsapi.org/v2/everything"
key = "f84816786cb94a23b3f6d5dbaef62b85"
    
       


# Determining the parameters
my_parameters = { 

       'q':'Canada Education OR Dalhousie University OR Monction OR Toronto OR Halifax OR University OR Canada',
       'pageSize': 100,
       'apikey':key,
       'language':'en',
       'from':'2020-03-02'

   }

# Fetching News
responses = requests.get(url,params=my_parameters)
news_in_json = responses.json()
my_articles = news_in_json['articles']



# Cleaning the extracted News

Names = []
Authors = []
Titles = []
Descriptions = []
Published_At_List = []
Contents = []


# Appending everything from JSON format to Python List for flexible processing
for i in range(len(my_articles)):
    Names.append(my_articles[i]['source']['name'])
    Authors.append(my_articles[i]['author'])
    Titles.append(my_articles[i]['title'])
    Descriptions.append(my_articles[i]['description'])
    Published_At_List.append(my_articles[i]['publishedAt'])
    Contents.append(my_articles[i]['content'])




News_List = []

# Cleaning the Date and News Content
for i in range(len(my_articles)):
    temp = Published_At_List[i]
    temp = temp[0:10] 
    Published_At_List[i]=temp
    temp = str(Contents[i])
    temp = temp.replace('\r','')
    temp = temp.replace('\n','')
    temp = temp.replace('<li>','')
    temp = temp.replace('</li>','')
    cut_index = temp.find('[')
    temp = temp[:cut_index]
    Contents[i]=str(temp)   



    
# Converting News Lists into a single Pandas DataFrame 
for i in range(len(my_articles)):
    temp = []
    temp.append(Names[i])
    temp.append(Authors[i])
    temp.append(Titles[i])
    temp.append(Descriptions[i])
    temp.append(Published_At_List[i])
    temp.append(Contents[i])
    News_List.append(temp)


# Exporting to a JSON file
cols = ['Source_Name','Author','Title','Description','Published_Date','Content']
news_df = pd.DataFrame(News_List,columns=cols)
news_df.to_json('Cleaned_News.json',orient='records',lines=True)

