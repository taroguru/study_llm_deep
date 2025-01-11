from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import nltk

nltk.download('stopwords')

def test_stopword():
    stopword_list = stopwords.words('english')
    print('영어 불용어 개수 :', len(stopword_list))
    print(stopword_list)
    print(stopword_list[:20])

    example_sentence = "Family is not an important thing. It's everything."
    stop_words = set(stopword_list)

    token_list = word_tokenize(example_sentence)

    result = []

    for word in token_list:
        if word not in stop_words:
            result.append(word)

    print('원문 :', token_list)
    print('불용어 제거 문장 :', result)

# 한국어 불용어 : https://www.ranks.nl/stopwords/korean
def test_korean_stopword():
    okt = Okt()

    example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
    stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"
    stop_words = set( stop_words.split(' ') )
    token_lists = okt.morphs(example)

    result = [token for token in token_lists if token not in stop_words]

    print('원문 :', token_lists)
    print('불용어 제거 문장 :', result)

if __name__ == "__main__":
    test_stopword()
    test_korean_stopword()