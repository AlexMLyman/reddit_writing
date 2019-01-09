# this takes your pickle created in the last step and turns it into one large
# text document for the bot to generate from.

import pickle


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

filename = 'commentpickle'

infile = open(filename, 'rb')
listofcomments = pickle.load(infile)
infile.close()

with open('rawdatadump.txt', 'w', encoding='utf8') as my_file:
    for comment in listofcomments:
        print(comment.body, file=my_file)
