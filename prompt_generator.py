# This will generate writing prompts based on the training corpus 

import markovify
import nltk
import re


class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = ["::".join(tag) for tag in nltk.pos_tag(words)]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# This will be however many prompts you want to generate
n = 100

with open("titlecorpus.txt", encoding='utf8') as my_file:
    text = my_file.read()

text_model = markovify.Text(text)

with open("bot_generated_prompts.txt", 'w', encoding='utf8') as my_file:
    for i in range(n):
        print('[WP] ' + text_model.make_sentence(), file=my_file)
