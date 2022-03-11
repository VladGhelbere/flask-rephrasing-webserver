from googletrans import Translator
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint
import nltk.data

translator = Translator()

def translate_text(text, to_language):
    translation = translator.translate(text, dest=to_language)
    return translation.text

class words_master():
    def __init__(self):
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        self.valid_replacements = ['JJ','NN','VB']

    def change_words(self, text_block):
        output_text = ''
        print(text_block)
        en_text = translate_text(text_block, 'en')
        print(en_text)
        tokenized_text = self.tokenizer.tokenize(en_text)
        words_text = word_tokenize(en_text)
        tagged_text = nltk.pos_tag(words_text)
        #print(tagged_text)
        
        for i in range(0,len(words_text)):
            replacements = []

            # Only replace nouns with nouns, vowels with vowels etc.
            for syn in wordnet.synsets(words_text[i]):

                if tagged_text[i][1] in self.valid_replacements:
                    word_type = tagged_text[i][1][0].lower()
                    if syn.name().find("."+word_type+"."):
                        # extract the word only
                        r = syn.name()[0:syn.name().find(".")]
                        replacements.append(r)

            #print(replacements)
            if len(replacements) > 0:
                # Choose a random replacement
                replacement = replacements[randint(0,len(replacements)-1)]
                output_text = output_text + " " + replacement
            else:
                # If no replacement could be found, then just use the original word
                output_text = output_text + " " + words_text[i]

        print(output_text)
        ro_text = translate_text(output_text, 'ro')
        print(ro_text)
        return ro_text

    def change_words_simplified(self, text_block):
        print(text_block)
        slight_text = translate_text(translate_text(text_block, 'en'), 'ro')
        print(slight_text)
        return slight_text

#text_in = "Dl. Vlad nu este prea fericit cu situatia actuala a pietei."
#wm = words_master()
#wm.change_words(text_in)
#wm.change_words_simplified(text_in)
