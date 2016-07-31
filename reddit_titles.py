#!/usr/bin/env python

import argparse
import sys

try:
    import praw
except ImportError:
    print("You must 'sudo pip install praw'")
    sys.exit(1)
try:
    from textblob import TextBlob
except ImportError:
    print("You must 'sudo pip install textblob'")
    sys.exit(1)

def get_sentiment(text):
    ''
    textblob seems to be more accurate for sentiment analysis
    you also won't get a ratelimit/slowdown since its all local
    '''
    sentiment = TextBlob(text).sentiment.polarity
    #I'm using the polarity, and manually separating it
    if sentiment > 0.2:
        return "postive"
    elif sentiment < -0.2:
        return "negative"
    return "neutral"

def check_subs(reddit, subs):
    '''
    i took away the limit, just because unless youre doing something special
    its annoying to have argeparse just for it since it shouldnt change much
    '''
    
    #added a subreddit sentiment average to compare different subreddits automatically
    sub_sents = []

    for sub in subs:
        #changed some variable names because i like being extra clear, you dont need to keep them
        posts = reddit.get_subreddit(args.subreddit).get_top(limit=10)
        titles = [post.title.encode('utf-8') for post in posts]
        total = 0
        for title in titles:
            sentiment = get_sentiment(title)
            print("{:<8} {:<10}".format(sentiment, title))
            total += sentiment
        sub_sents.append(total/len(posts))
    
    #merge the two lists into a dict
    avg_sents = {}
    for sub, sent in zip(subs, sub_sents):
        avg_sent[sub] = sent
    return avg_sents

def extremes(avg_sents):
    #im not sure if this works well, and its definitely written poorly, but you get the idea. just for fun
    #feel free to remove this if it doesnt work properly
    neg_key = avg_sents.keys()[0]
    neg = avg_sents.values()[0]
    pos_key = neg_key
    pos = neg
    for key, val in avg_sents:
        if val < neg:
            neg_key = key
            neg = val
        elif val > pos:
            pos_key = key
            pos = val
    return [neg_key, neg], [pos_key, pos]

if __name__ == '__main__':
    #using a file for the subreddits allows you to check multiple subreddits easier
    with open('subreddits.txt') as file:
        #for subreddits.txt, just put a single sub name on each line with no whitespace other than \n
        subs = file.readlines()

    #using a version number helps reddit stop from considering you a spam bot, theyre really picky
    reddit = praw.Reddit(user_agent='Test Script v.01 by /u/goodDayM')
    
    #get a dictionary with the average sentiment for each sub (is /r/news negative? lets see!)
    avg_sents = check_subs(reddit, subs)
    
    #find and print the most extreme subs (most positive and most negative)
    pos, neg = extremes(avg_sents)
    print('pos:', pos)
    print(neg:', neg)
    
    #check out the all the results
    print(avg_sents)
    

