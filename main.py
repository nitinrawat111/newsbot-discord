import discord
import os
import logging
from datetime import timedelta
from datetime import date
from datetime import datetime
from newsapi import NewsApiClient

#Initializing NewsApiClient
newsApi = NewsApiClient(api_key = os.environ['NEWSAPIKEY'])
#Configuring logging
logging.basicConfig(level=logging.WARNING)
#Initialising Discord Client
client = discord.Client()

async def parseJsonHeadlineToString(jsonHeadline, urlNeeded):
  #Single backticks to show title in a single code block
  headlineString = "`" + jsonHeadline["title"] + "`"
  
  #Enclosing rest of headline in triple backticks to show in a code block.
  #Be careful of \n as it separates these backticks from the single closing backtick above
  headlineString += "\n```"

  #Adding description to headline
  headlineString +=  jsonHeadline["description"] 
  
  #Adding Article Author to the headlineString
  headlineString += "\nAuthor: " + str(jsonHeadline["author"])

  #Creating a datetime object for the publish time
  publishDateTime = datetime.strptime(jsonHeadline["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
  #Extracted time is in Z timezone. Adding +5:30 offset to convert to IST
  publishDateTime += timedelta(hours = 5, minutes = 30)
  headlineString += "\nPublished on: " + str(publishDateTime) + " IST"

  #Adding Source to the headline
  headlineString += "\nSource: " + str(jsonHeadline["source"]["name"])
  
  #Closing triple backticks
  headlineString += "```"

  #If url is requested(q is commanded instead to qs or top is commanded instead of tops)
  #then, we add the url to the headline
  if(urlNeeded):
    headlineString += "Link: " + str(jsonHeadline["url"])

  return headlineString

async def getHeadlinesFromJson(jsonData, urlNeeded):
  headlines = []
  
  totalResults = jsonData["totalResults"]
  if(totalResults == 0):
    return ["No results Found!"]
  
  totalResults = 5 if totalResults > 5 else totalResults
  for i in range(totalResults):
      jsonHeadline = jsonData["articles"][i]
      headlines.append( await parseJsonHeadlineToString(jsonHeadline, urlNeeded) )
  return headlines

async def getTopHeadlines(urlNeeded):
  jsonData = newsApi.get_top_headlines(language = 'en')
  return await getHeadlinesFromJson(jsonData, urlNeeded)

async def getHeadlinesFromQuery(query, urlNeeded):
  to_date = date.today()
  from_date = to_date - timedelta(days = 7)
  jsonData = newsApi.get_everything(q = query, language = 'en', from_param = str(from_date), to = str(to_date), sort_by = 'relevancy')
  return await getHeadlinesFromJson(jsonData, urlNeeded)

@client.event
async def on_ready():
  print('Logged on as {0.user}!'.format(client))

async def sendMultipleMessages(messages, channel):
  for each_message in messages:
    await channel.send(each_message)

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  
  if(message.content == "$top"):
    topHeadlines = await getTopHeadlines(urlNeeded = True);
    await sendMultipleMessages(topHeadlines, message.channel)
  
  if(message.content == "$tops"):
    topHeadlines = await getTopHeadlines(urlNeeded = False);
    await sendMultipleMessages(topHeadlines, message.channel)
  
  if(message.content.startswith("$q ")):
    query = message.content[3:]
    queryResults = await getHeadlinesFromQuery(query, urlNeeded = True)
    await sendMultipleMessages(queryResults, message.channel)
  
  if(message.content.startswith("$qs ")):
    query = message.content[4:]
    queryResults = await getHeadlinesFromQuery(query, urlNeeded = False)
    await sendMultipleMessages(queryResults, message.channel)

client.run(os.environ['TOKEN'])