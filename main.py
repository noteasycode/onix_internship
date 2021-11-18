from transliterate import translit


def convert_word_to_amt(word):
    amt = 0
    for char in word:
        if char.isalnum():
            amt += ord(char)
        amt += 0
    return amt


def vectorizer():
    with open('text.txt', 'r', encoding='utf-8') as file:
        sentences = [sentence for sentence in translit(
            str(file.read()), language_code='uk', reversed=True
        ).replace('\r', '').split('.') if sentence != '']
    words_in_sentence = []
    for sentence in sentences:
        words_in_sentence.append(sentence.split())
    resault = [[]] * len(words_in_sentence)
    for i in range(len(words_in_sentence)):
       for word in words_in_sentence[i]:
           resault[i].append(convert_word_to_amt(word))
    file.close()
    return resault


def main():
    print(vectorizer())


if __name__ == '__main__':
    main()
