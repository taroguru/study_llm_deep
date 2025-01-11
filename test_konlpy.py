from konlpy.tag import Okt

okt = Okt()

def build_bag_of_words(document):
    document = document.replace('.', '')
    tokenized_document = okt.morphs(document)
    word_to_index ={}

    bow =[]
    
    for word in tokenized_document:
        if word not in word_to_index.keys():
            word_to_index[word]= len(word_to_index)
            # BoW에전부기본값1을넣는다.
            bow.insert(len(word_to_index)-1,1)
        else:
            #재등장하는단어의인덱스
            index= word_to_index.get(word)
            #재등장한단어는해당하는인덱스의위치에1을더한다.
            bow[index]= bow[index]+1
    return word_to_index, bow


doc1 = "정부가 발표하는 물가상승률과 소비자가 느끼는 물가 상승률은 다르다."
vocab, bow = build_bag_of_words(doc1)
print('vocabulrary: ', vocab)
print('bag of words: ', bow)
