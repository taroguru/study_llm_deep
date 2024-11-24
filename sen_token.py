import nltk.tokenize as sent_tokenize
from nltk.tag import pos_tag
import kss
import nltk
nltk.download('averaged_perceptron_tagger_eng')
from konlpy.tag import Okt
from konlpy.tag import Kkma

import nltk
nltk.download('punkt_tab')

def text_sentence_tokenizer():
    text = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
    sentences = sent_tokenize.sent_tokenize(text)

    print('sentence tokenizer')
    for sentence in sentences:
        print(sentence)

    text = "I am actively looking for Ph.D. students. and you are a Ph.D student."
    sentences = sent_tokenize.sent_tokenize(text)

    print('sentence tokenizer')
    for sentence in sentences:
        print(sentence)

def korean_text_sentence_tokenizer():
    text = "'딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?"
    sentences = sent_tokenize.sent_tokenize(text)

    print('한글 토크나이저')
    for sentence in sentences:
        print(sentence)

    sentences = kss.split_sentences(text)
    print('kss 한글 토크나이저')
    for sentence in sentences:
        print(sentence)


def tag_text():
    text = "I am actively looking for Ph.D. students. and you are a Ph.D student."
    tokenizer = sent_tokenize.TreebankWordTokenizer()
    token_list =  tokenizer.tokenize(text)

    tagged_list = pos_tag(token_list)

    print('tagged list')
    for word in tagged_list:
        print(word)

def korean_tokenizer():
    text = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
    okt = Okt()

    tokenlist = okt.morphs(text)
    print('Okt')
    print(tokenlist)
    poslist = okt.pos(text)
    print('Okt pos')
    print(poslist)
    nounlist = okt.nouns(text)
    print('Okt noun')
    print(nounlist)



if __name__ == "__main__":
    text_sentence_tokenizer()
    korean_text_sentence_tokenizer()
    tag_text()
    korean_tokenizer()