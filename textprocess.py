# 단어 분류
import nltk.tokenize as work_tokenize
from nltk.tokenize import TreebankWordTokenizer

def main():
    source_text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

    text = "This is a sentence. This is another sentence."
    sentences = work_tokenize.sent_tokenize(text)

    print('sentence tokenizer')
    for sentence in sentences:
        print(sentence)

    words = work_tokenize.word_tokenize(text)
    print('word tokenizer')
    for word in words:
        print(word)
    sec_words = work_tokenize.word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop.")
    print('second word tokenizer')

    for word in sec_words:
        print(word)

    print('third word tokenizer')
    third_word = work_tokenize.wordpunct_tokenize(source_text)
    for word in third_word:
        print(word)

    # 표준. Penn Treebank Tokenization.
    print('forth word tokenizer')
    tokenizer = TreebankWordTokenizer()
    forth = tokenizer.tokenize(source_text)
    for word in forth:
        print(word)



if __name__ == "__main__":
    main()