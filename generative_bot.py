#We are attempting to make a simple freqdist text geneator
import nltk

from random import randint


with open('rawdatadump.txt', 'r', encoding = 'utf8') as myfile:
    text=myfile.read()
text = text.replace('"', '')

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')
tokenized_content = tokenizer.tokenize(text)


cfreq = nltk.ConditionalFreqDist(nltk.bigrams(tokenized_content))
cprob = nltk.ConditionalProbDist(cfreq, nltk.MLEProbDist)

criteria = ['.', 't', '?', ',', "'", 's']
responselength = randint(100,500)
word = "in"
for index in range(responselength):
    word = cprob[word].generate()
    if word not in criteria:
        print(' '+ word, end = '')
    else:
        print(word, end = '')

