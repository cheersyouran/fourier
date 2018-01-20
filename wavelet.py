import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pywt

beginDate = '2016-02-01'

data = pd.read_csv('/Users/Youran/Projects/stock-pattern-search/data/800_data.csv')
data = data[data['DATE'] >= beginDate].head(300)[['CLOSE','DATE']]
index_list = data['CLOSE'].values


def wt(index_list, data, wavefunc, level, m, n):
    '''
    :param index_list: 待处理序列；
    :param data: 最后保存的dataframe便于作图
    :param wavefunc: 小波函数
    :param level: 分解层数
    :param m, n: 则选择了进行阈值处理的小波系数层数
    :return:
    '''

    # 按 level 层分解，使用pywt包进行计算， cAn是尺度系数 cDn为小波系数
    coeff = pywt.wavedec(index_list, wavefunc, mode='sym', level=level)
    sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0  # sgn函数

    for i in range(m, n + 1):  # 尺度系数不需要处理
        cD = coeff[i]
        # for j in range(len(cD)):
        #     Tr = np.sqrt(2 * np.log(len(cD)))  # 计算阈值
        #     if cD[j] >= Tr:
        #         coeff[i][j] = sgn(cD[j]) - Tr  # 向零收缩
        #     else:
        #         coeff[i][j] = 0  # 低于阈值置零

        if i not in [1, 2, 3, 4] :
            for j in range(len(cD)):
                coeff[i][j] = 0

    denoised_index = pywt.waverec(coeff, wavefunc)

    data['denoised_index'] = denoised_index

    data = data.set_index(data['DATE'])
    data.plot()
    print('finish')

if __name__ == '__main__':
    wt(index_list, data, 'db4', 4, 0, 4)