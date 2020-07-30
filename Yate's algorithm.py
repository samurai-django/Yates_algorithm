
import pandas as pd
import numpy as np
import sys



df = pd.read_csv("C:/Users/m19ss/Documents/Q2 2020/matsu labo/Yate's sample.csv", index_col="Yate's")
df_church = pd.read_csv("C:/Users/m19ss/Documents/Q2 2020/matsu labo/church_data.csv", index_col="church_data")
index_b = df.index
index = index_b.tolist()

church = df_church['row1']
church_row1 = church.tolist()
c = df['row1']
row1 = c.tolist()
index_church_b = df_church.index
index_church = index_church_b.tolist()



def yates_algorithm(x, n, a):

    data = x
    # 対比計算 Contast
    l = 0
    contrast = []
    for l in range(n):
        even1 = x[::2]
        odd1 = x[1::2]

        r1 = len(even1)
        y_plus = []
        j = 0
        for j in range(r1):
            y_plus.append(even1[j] + odd1[j])
        y_minus = []
        k = 0
        for k in range(r1):
            y_minus.append(- even1[k] + odd1[k])

        contrast = y_plus + y_minus
        x = contrast
    z = []
    z = contrast

    # 効果計算 Effect
    effect = []
    z = list(map(lambda x:x/8, contrast))
    effect = z

    # Sun Of Square
    p = []
    p = np.power(contrast, 2)
    sum_of_square = []
    sum_of_square = p / 2**n

    new_df = pd.DataFrame(data, columns=['データ'], index=a)

    new_df['対比'] = contrast
    new_df['効果'] = effect
    new_df['SS'] = sum_of_square

    return print(new_df)

contrast = yates_algorithm(row1, 3, index)
church_contrast = yates_algorithm(church_row1, 4, index_church)

