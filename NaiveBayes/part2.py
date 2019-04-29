

import pandas as pd
import string

#import my csv file
df = pd.read_csv('unsmile.csv')

#Remove any rows with a "nan" in them
df = df.dropna(axis=0, how = 'any')

#Make it so that any non readable text gets converted into nothing
def removetext(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

#Here I am doing the actual removing
df['text'] = df['text'].apply(removetext)
print("LIST OF TWEETS(DATAFRAME):")
print(df['text'])

#Make all my texts lower case
df['text'] = df['text'].apply(lambda x: x.lower())
#print(df['text'])

#Get rid of all weird punctuation and extra lines
df['text'] = df['text'].apply(lambda x: x.replace('.',' '))
df['text'] = df['text'].apply(lambda x: x.replace('\n',' '))
df['text'] = df['text'].apply(lambda x: x.replace('?',' '))
df['text'] = df['text'].apply(lambda x: x.replace('!',' '))
df['text'] = df['text'].apply(lambda x: x.replace('"',' '))
df['text'] = df['text'].apply(lambda x: x.replace(';',' '))
df['text'] = df['text'].apply(lambda x: x.replace('#',' '))
df['text'] = df['text'].apply(lambda x: x.replace('&amp',' '))
df['text'] = df['text'].apply(lambda x: x.replace(',',' '))

#Here I get each unique keyword from my dataframe
array = df['text'].str.split(' ', expand=True).stack().value_counts()
print("GET EACH UNIQUE KEYWORD FROM MY DATAFRAME")
print(array)

#I make a dataframe of the words and the frequency with which the words appear 
d = {'word': array.index, 'frequency':array}
df2 = pd.DataFrame(data = d)
print("TERM FREQUENCIES")
print(df2)

#I get rid of any words that are mentioned less than 10 times
df2['frequency'] = df2['frequency'][df2['frequency'] > 10]
print("Remove words which freuencies are less than 10") 
#print(df2['frequency'] )
#Remove any rows with a "nan" in them
df2 = df2.dropna(axis=0, how = 'any')
print(df2)
#Drop any obvious signs of these words being :(
df2 = df2.drop([':(','https://t',':((', ':(((', ':((((', ':(((((', ':', '(', ''])
print("drop any obvious signs of these words being :(")
print(df2)
#Convert my dataframe into a csv file
df2.to_csv('unsmile_words.csv', header=True, index=False, encoding='utf-8')




