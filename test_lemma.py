from lxml.html.diff import token
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

import nltk
nltk.download('wordnet')

# 영어에서의 표제어, 어간 추출

# lemma : 표제어. 기본 사전형 단어

def test_lemmatization():
    lemmatizer = WordNetLemmatizer()

    words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has',
             'starting']
    lemmatizer.lemmatize('dies', 'v')
    lemmatizer.lemmatize('watched', 'v')
    lemmatizer.lemmatize('has', 'v')

    print('표제어 추출 전 :', words)
    print('표제어 추출 후 :', [lemmatizer.lemmatize(word) for word in words])

# stem : 어간.
# stemming : 어간 추출

def test_stemming():
    stemmer = PorterStemmer()
    sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
    token_list = word_tokenize(sentence)
    words = [stemmer.stem(word) for word in token_list]

    print('어간 추출 전 :', token_list)
    print('어간 추출 후 :', words)


# 활용 : 용언(동사, 형용사)의 어간이 어미를 가지는 일
# 규칙 활용 : 어미에 따라 어간이 변하지 안흠. 잡(어간)+다(어미)
# 불규칙 활용 : 어미에 따라 어간이 변할 수 있음. ex) 돕-다, 돕/도우
# ex) 선생님은 우리를 항상 잘 도와주신다.

if __name__ == "__main__":
    test_lemmatization()
    test_stemming()