#!/usr/bin/env python

import argparse
import json
import sys
import urllib

try:
    import praw
except ImportError:
    print("You must 'sudo pip install praw'")
    sys.exit(1)

def sentiment(text):
    try:
        data = urllib.urlencode({"text": text})
    except Exception as e:
        print("Warning: %s" % e)
        print(text)
        return ""
    u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
    the_page = json.load(u)
    return the_page['label']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Reddit Titles')
    parser.add_argument('subreddit', type=str,
                        help='Name of subreddit, e.g. "news"')
    parser.add_argument('-n', type=int, default=10,
                        help='Number of titles')
    args = parser.parse_args()

    r = praw.Reddit(user_agent='Test Script by /u/goodDayM')
    submissions = r.get_subreddit(args.subreddit).get_top(limit=args.n)
    titles = [x.title.encode('utf-8') for x in submissions]
    for t in titles:
       s = sentiment(t)
       print("{:<8} {:<10}".format(s, t))

