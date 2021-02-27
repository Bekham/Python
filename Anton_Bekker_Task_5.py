from random import randrange


def get_jokes(count):
    """Generating a given number of jokes"""
    jokes = []
    text = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    text.append(nouns)
    text.append(adverbs)
    text.append(adjectives)
    while count:
        num_word = []
        joke = ''
        for i in range(0, len(text)):
            num_word.append(randrange(len(text[i])))
            joke += text[i][num_word[i]] + ' '
            text[i].remove(text[i][num_word[i]])
        jokes.append(joke)
        count -= 1
    return jokes


print(get_jokes(4))
