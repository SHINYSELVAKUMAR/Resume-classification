#name = twitter_sentiment_tacosushi
#Import the necessary methods from tweepy library as well as json and time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import time
import pandas as pd


#We authenticate ourselves as having a twitter app
#Variables that contains the user credentials to access Twitter API 
access_token = "927546846897094657-1RvAm3mnNcQ6Ad2aBjLU7tSd6pJwNYF"
access_secret = "CxwE7Ry8NuOF94cFq4pDxhxTcSsYVktQali7RZrZxZpG9"
consumer_key = "V0eccRgT2KaD5VfVp3Ghseh2U"
consumer_secret = "6q1nRqoGmFNMQIH2tggTFpIV4BbLbjC3jEk44xJGP1zNKO2VJQ"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)




#We begin searching our query
#Put your search term
searchquery = "sad"

users =tweepy.Cursor(api.search,q=searchquery).items()
count = 0
start = 0
errorCount=0

#We will be storing our data in file called: happy.json
#file = open('test.json', 'wb') 

#here we tell the program how fast to search 
waitquery = 100      #this is the number of searches it will do before resting
waittime = 2.0          # this is the length of time we tell our program to rest
total_number = 100    #this is the total number of queries we want
justincase = 1         #this is the number of minutes to wait just in case twitter throttles us



text = [0] * total_number
secondcount = 0
idvalues = [1] * total_number
 #1 is happy; 2 is sad; 3 is angry; 4 is fearful
#Below is where the magic happens and the queries are being made according to our desires above
while secondcount < total_number:
    try:
        user = next(users)
        count += 1
        
        #We say that after every 100 searches wait 5 seconds
        if (count%waitquery == 0):
            time.sleep(waittime)
            #break

    except tweepy.TweepError:
        #catches TweepError when rate limiting occurs, sleeps, then restarts.
        #nominally 15 minnutes, make a bit longer to avoid attention.
        print("sleeping....")
        time.sleep(60*justincase)
        user = next(users)
        
        
    except StopIteration:
        break
    try:
        #print "Writing to JSON tweet number:"+str(count)
        text_value = user._json['text']
        
        language = user._json['lang']
        
        #print(text_value)
        #print(language)
        
        if "RT" not in text_value:
            if language == "en":
                text[secondcount] = text_value
                secondcount = secondcount + 1
                print("current saved is:")
                print(secondcount)

    except UnicodeEncodeError:
        errorCount += 1
        print("UnicodeEncodeError,errorCount ="+str(errorCount))


print("Creating dataframe:")

d = {"text": text, "id": idvalues}
df = pd.DataFrame(data = d)
print(df)
df.to_csv('upset.csv', header=True, index=False, encoding='utf-8')

print("completed")


