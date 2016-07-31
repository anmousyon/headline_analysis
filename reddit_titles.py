#!/usr/bin/env python

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
    '''
    textblob seems to be more accurate for sentiment analysis
    you also wont get a ratelimit/slowdown since its all local
    '''
    sentiment = TextBlob(text).sentiment.polarity
    return sentiment

def simple_sent(sentiment):
    '''simplifies sent to neg, neut, pos'''
    #I'm using the polarity, and manually separating it
    if sentiment > 0.05:
        return "postive"
    elif sentiment < -0.05:
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
        posts = reddit.get_subreddit(sub.strip()).get_top(limit=10)
        total = 0
        counter = 0
        for post in posts:
            sentiment = get_sentiment(post.title)
            print("{:<8} {:<10}".format(simple_sent(sentiment)+':', post.title))
            total += sentiment
            counter += 1
        sub_sents.append(total/counter)

    #merge the two lists into a dict
    avg_sents = {}
    for sub, sent in zip(subs, sub_sents):
        avg_sents[sub.strip()] = simple_sent(sent)
    return avg_sents

def extremes(avg_sents):
    '''
    im not sure if this works well, and its definitely written poorly
    feel free to remove this if it doesnt work properly
    '''
    neg_key = None
    neg = 0
    pos_key = None
    pos = 0
    for key, val in avg_sents.items():
        if not neg_key:
            neg_key = key
            neg = val
            pos_key = key
            pos = val
            continue
        if val < neg:
            neg_key = key
            neg = val
        elif val > pos:
            pos_key = key
            pos = val
    return neg_key, pos_key

def main():
    '''changed this to main because of the renaming issues'''
    #using a file for the subreddits allows you to check multiple subreddits easier
    with open('subreddits.txt') as file:
        #for subreddits.txt, just put a single sub name on each line
        subs = file.readlines()

    #using a version number helps reddit stop from considering you a spam bot, theyre really picky
    reddit = praw.Reddit(user_agent='Test Script v.01 by /u/goodDayM')

    #get a dictionary with the average sentiment for each sub (is /r/news negative? lets see!)
    avg_sents = check_subs(reddit, subs)

    #find and print the most extreme subs (most positive and most negative)
    neg_key, pos_key= extremes(avg_sents)
    print('most positive:', pos_key)
    print('most negative:', neg_key)

    #check out the all the results
    print(avg_sents)

main()
