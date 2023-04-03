from nltk import word_tokenize, pos_tag

sentence = str(input())
tokenized = word_tokenize(sentence)
result = [word for word, tag in pos_tag(tokenized) if tag in ['VB', 'VBD', 'VBN', 'VBP', 'VBZ', 'VBG']]
print(result)
