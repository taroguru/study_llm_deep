import numpy as numpy
import pandas as pd


def test_series():
    series = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
    print('시리즈 출력')
    print('-'*18)
    print(series)

    # 시리즈 인덱스 출력
    print('시리즈 인덱스 출력')
    print('-'*18)
    print('시리즈의 인덱스 : {}'.format( series.index) )
    print('시리즈의 값 : {}'.format( series.values) )

def test_dataframe():
    # 데이터프레임에 사용할 열(columns)과 행 인덱스(index) 정의
    columns = ['이름', '나이', '성별']  # 열 이름 리스트
    indexes = ['a', 'b', 'c', 'd']    # 행 인덱스 리스트
    
    # 실제 데이터 값을 2차원 리스트로 정의
    data = [['홍길동', 10, '남'],   # a행 데이터
            ['김철수', 20, '남'],   # b행 데이터 
            ['이영희', 30, '여'],   # c행 데이터
            ['박영수', 40, '남']]   # d행 데이터

    # pandas DataFrame 객체 생성
    # data: 실제 데이터 값
    # index: 행 인덱스 
    # columns: 열 이름
    dataframe = pd.DataFrame(data, index=indexes, columns=columns)
    
    # 생성된 데이터프레임 출력
    print('데이터프레임 출력')
    print(dataframe)

    changed_frame = pd.DataFrame(data, columns=['름이', '이나', '별성'])
    print('changed data frame column name')
    print(changed_frame)

    # test declare dictionary
    data = {
        '학번':[123, 234, 456],
        '이름':['찰수', '용이', '민자'],
        '점수':[12, 23, 45]
    }
    dictionary_dataframe = pd.DataFrame(data)
    print('show dictionary type : ')
    
    print(data)
    print(dictionary_dataframe)
    



    print('find data in dataframe')
    print('head 2 : ', dataframe.head(2))
    print('tail 2 : ', dataframe.tail(2))
    print('show all name :  ', dataframe['이름'])

    csv_df = pd.read_csv('example.csv')
    print('read from csv')
    print(csv_df)
    print('show index')
    print(csv_df.index)
if __name__ == "__main__":
    test_dataframe()
    






