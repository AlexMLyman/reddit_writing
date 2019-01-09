# Run this next. It will get data comment data from the posts identified in
# part 1.

import praw
import pickle
from praw.models import MoreComments


class Prompt:
    def __init__(self, score, id, url, body, title):
        self.score = score
        self.id = id
        self.url = url
        self.body = body
        self.title = title


class Comment:
    def __init__(self, score, id, body, length, ttr, positivity, toktex,
                 tagtex):
        self.score = score
        self.id = id
        self.body = body
        self.length = length
        self.ttr = ttr
        self.positivity = positivity
        self.toktex = toktex
        self.tagtex = tagtex

listofprompts = []
listofcomments = []
reddit = praw.Reddit(client_id='Insert Reddit client ID',
                     client_secret='Insert your secret code',
                     password='Insert your Reddit Passwied',
                     user_agent='Insert Descriptive user agent (don\'t lie)',
                     username='Insert Reddit username')

filename = 'promptpickle'

infile = open(filename, 'rb')
listofprompts = pickle.load(infile)
infile.close()


for n in listofprompts:
    submission = reddit.submission(id=n.id)
    i = 0
    for index, top_level_comment in enumerate(submission.comments):
        if isinstance(top_level_comment, MoreComments):
            continue
        # this stops infinite loops
        if index == 30:
            break
        c = Comment(top_level_comment.score, top_level_comment.id,
                    top_level_comment.body, 0, 0, 0, [], [])
        # this stops the program from adding modposts and deleted prompts
        if not c.body.startswith(('**Off', '\n**Off', '[deleted]',
                                 '[removed]')):
            i += 1
            listofcomments.append(c)
        # this limits me to 20 comments per prompt
        if i >= 20:
            break


filename = 'commentpickle'
outfile = open(filename, 'wb')
pickle.dump(listofcomments, outfile)

outfile.close()
