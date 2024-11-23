
import matplotlib.pyplot as plt
import pandas as pd


def showplot():
    data = pd.DataFrame([1,2,3,4,5,6], columns=['name'], index=['a', 'b', 'c', 'd', 'e', 'f'])
    data_sec = pd.DataFrame([1,2,3,4,8,9], columns=['name'], index=['a', 'b', 'c', 'd', 'e', 'f'])

    plt.title('new plot_')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['Legend For Y', 'Legend For D'] )
    plt.plot(data)
    plt.plot(data_sec)
    plt.show()

if __name__ == '__main__':
    showplot()