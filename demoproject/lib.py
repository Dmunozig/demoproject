### FUN FACT:
### Scotland has 421 words about snow. This function will print 421 variations of the input word
### Some examples: sneesl (to start raining or snowing); feefle (to swirl); flinkdrinkin (a light snow).
### To avoid making 421 different words, lets assume some are spelled the same but have different pronounciations!
import string
import random

def snow_word_multiplier(word):
    # input must be string
    snowed_words = [word]
    for i in range(420):
        variation = word + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        snowed_words.append(variation)
    print(snowed_words)
    print('-------------------------------')
    print('-------------------------------')
    print('Fun fact: there are 421 scottish words for snow!')
    print(f"Here are {len(snowed_words)} scottish ways of saying {word} (kinda)")
    return(snowed_words)