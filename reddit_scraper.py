# Run this first! It will grab the top x posts of all time from the target
# subreddit 

import praw
import pickle


class Prompt:
    def __init__(self, score, id, url, body, title):
        self.score = score
        self.id = id
        self.url = url
        self.body = body
        self.title = title
listofprompts = []

reddit = praw.Reddit(client_id='Insert Reddit client ID',
                     client_secret='Insert your secret code',
                     password='Insert your Reddit Passwied',
                     user_agent='Insert Descriptive user agent (don\'t lie)',
                     username='Insert Reddit username')

subreddit = reddit.subreddit('WritingPrompts')

# 108 is a magic number. I didn't have the time to limit this correctly, so
# this quick fix let me get 100 prompts. If you want more or less, change the
# number
submissisons = subreddit.top(limit=108)
for submission in submissisons:
    n = Prompt(submission.score, submission.id, submission.url,
               submission.selftext, submission.title)
    # this filters out non writing prompts
    if n.title.startswith('[WP]'):
        listofprompts.append(n)

filename = 'promptpickle'
outfile = open(filename, 'wb')
pickle.dump(listofprompts, outfile)

outfile.close()
