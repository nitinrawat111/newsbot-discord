import discord
import os
import logging
import datetime
from datetime import date
from newsapi import NewsApiClient

#Initializing NewsApiClient
newsApi = NewsApiClient(api_key = os.environ['NEWSAPIKEY'])
#Configuring logging
logging.basicConfig(level=logging.WARNING)
#Initialising Discord Client
client = discord.Client()

async def parseJsonHeadlineToString(jsonHeadline, urlNeeded):
  headlineString = jsonHeadline["title"]
  if(urlNeeded):
    headlineString += "\nLink: " + str(jsonHeadline["url"])
  headlineString += "\nAuthor: " + str(jsonHeadline["author"])
  headlineString += "\nPublished on: " + str(jsonHeadline["publishedAt"])
  headlineString += "\nSource: " + str(jsonHeadline["source"]["name"])
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
  from_date = to_date - datetime.timedelta(days = 7)
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
  if(message.author != client.user):
    if(message.content == "$top"):
      topHeadlines = await getTopHeadlines(urlNeeded = True);
      await sendMultipleMessages(topHeadlines, message.channel)
    elif(message.content == "$tops"):
      topHeadlines = await getTopHeadlines(urlNeeded = False);
      await sendMultipleMessages(topHeadlines, message.channel)
    elif(message.content.startswith("$q ")):
      query = message.content[3:]
      queryResults = await getHeadlinesFromQuery(query, urlNeeded = True)
      await sendMultipleMessages(queryResults, message.channel)
    elif(message.content.startswith("$qs ")):
      query = message.content[4:]
      queryResults = await getHeadlinesFromQuery(query, urlNeeded = False)
      await sendMultipleMessages(queryResults, message.channel)

client.run(os.environ['TOKEN'])