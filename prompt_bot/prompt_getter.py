import praw


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

submissisons = subreddit.top(limit=None)
for submission in submissisons:
    n = Prompt(submission.score, submission.id, submission.url,
               submission.selftext, submission.title)
    # this filters out non writing prompts
    if n.title.startswith('[WP]'):
        listofprompts.append(n)

filename = 'titlecorpus.txt'
with open(filename, 'w', encoding='utf8') as my_file:
    for m in listofprompts:
        print(m.title, file=my_file)
