import numpy as np


def test_numpy():
    nd_array = np.array([1,2,3,4,5])
    print('nd : ', nd_array)
    twodim = np.array([[1,2,3],[4,5,6]])
    print('twodim : ', twodim)

    sparse =  [[2,3,4],[1,2,3]]
    sp_array = np.array(sparse)
    print('sparse : ', sp_array)

    print('typeof nd_array : ', type(nd_array))
    print('typeof sp_array : ', type(sp_array))

    print('축의 개수: ', nd_array.ndim)
    print('크기 : ', nd_array.shape)


    zeros = np.zeros((3, 4))
    print('zeros 3 4', zeros)

    ones = np.ones((5, 6))
    print('ones', ones)

    allseven = np.full((5, 6  ), 7)
    print('allseven', allseven)

    eyematrix = np.eye(10)
    print('eye matrix : ', eyematrix)

    random_matrix = np.random.random((3, 4))
    print('random matrix : ', random_matrix)

    zerotonine = np.arange(stop= 10, start=0)
    print('zero to ten : ', zerotonine)

    twobytwo = np.arange(start=2, stop=10, step=3)
    print('two by two : ', twobytwo)

    zerotwotwo_twodim = np.arange(stop=30).reshape(5,6)
    print('zero to two two : ', zerotwotwo_twodim)

    slicefirst = np.arange(10).reshape(2,5)[0]
    print('slice first : ', slicefirst)
    slice_fist = np.arange(10).reshape(2,5)[0]
    print('slice first : ', slice_fist)

    slicesecond = np.arange(10).reshape(2,5)[:,0]
    print('slice second : ', slicesecond)

    mat = np.array([[1, 2], [4, 5], [7, 8]])
    print(mat)
    # 1행 0열의 원소
    # => 0부터 카운트하므로 두번째 행 첫번째 열의 원소.
    print(mat[1, 0])

    # mat[[2행, 1행],[0열, 1열]]
    # 각 행과 열의 쌍을 매칭하면 2행 0열, 1행 1열의 두 개의 원소.
    # 이해가 안감 ㅋㅋㅋ
    indexing_mat = mat[[2, 1], [0, 1]]
    print(indexing_mat)

    # 사직연산
    first = np.array([1,2,3])
    second = np.array([4,5,6])

    sumtwo = np.add(first, second)
    subtwo = np.subtract(first, second)
    multwo = np.multiply(first, second)
    divtwo = np.divide(first, second)
    print('sum two : ', sumtwo)
    print('sub two : ', subtwo)
    print('mul two : ', multwo)
    print('div two : ', divtwo)

if __name__ == '__main__':
    test_numpy()

