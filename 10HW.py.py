"""
Урок 10. Построение графиков
Скрыть
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид.
 Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data_one_hot = data.apply(lambda x: x.astype('category').cat.codes)
data_one_hot = pd.concat([data_one_hot, 1 - data_one_hot], axis=1)
data_one_hot.columns = ['human', 'robot']
data_one_hot.head()