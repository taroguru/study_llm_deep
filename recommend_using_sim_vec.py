import kagglehub
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nummpy as np

# Download latest version
path = kagglehub.dataset_download("rounakbanik/the-movies-dataset")

print("Path to dataset files:", path)
path += "/movies_metadata.csv"

data = pd.read_csv(path, low_memory=False)
# print (data.head(2))
data = data.head(20000)

print('overview 열의 결측값의 수 : ', data['overview'].isnull().sum())

# 결측값을 빈값으로 대체
data['overview'] = data['overview'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
print('TF-IDF 행 렬의 크기(shape) :', tfidf_matrix.shape)

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print('코 사인 유사도 연산 결과 :', cosine_sim.shape)

title_to_index = dict(zip(data['title'], data.index))
 # 영화 제목 Father of the Bride Part II의 인덱스를 리턴
idx = title_to_index['Father of the Bride Part II']
print(idx)

def get_recommendations(title, cosine_sim=cosine_sim):
    #선택한영화의타이틀로부터해당영화의인덱스를받아온다.
    idx =title_to_index[title]

    #해당영화와모든영화와의유사도를가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    #유사도에따라영화들을정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    #가장유사한10개의영화를받아온다.
    sim_scores = sim_scores[1:11]

    #가장유사한10개의영화의인덱스를얻는다.
    movie_indices = [idx[0] for idx in sim_scores]

    #가장유사한10개의영화의제목을리턴한다.
    return data['title'].iloc[movie_indices]


sim_movies = get_recommendations('The Dark Knight Rises')
print(sim_movies)


