import fuc
import numpy as np
import theano


def embeding(df, n20_column, gn20_column, target):
    bases = ['A', 'C', 'G', 'T']
    base_dict = dict(zip(bases, range(4)))  # {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}

    n = len(df)

    X = np.zeros((n, 1, 4, 23))  # align 后，最长为23位，不足23的pad为0

    N20 = df[n20_column].values
    GN20 = df[gn20_column].values
    v = df[target].values

    for i in range(n):
        if i % 5000 == 0:
            print(i)
        # if i > 10000:  # to simplify
        #     break
        n20 = N20[i]
        gn20 = GN20[i]
        if "N" in gn20 or "N" in n20:
            continue
        # 之前传进来的Y值没有什么用，这里主要是对GN20和N20做get_align操作
        align = fuc.get_align(gn20, n20)
        for b in range(len(align)):
            for c in range(4):
                X[i, 0, c, b] = align[b][c]

    X = X.astype(theano.config.floatX)
    Y = np.asarray(df[target].values,
                   dtype=theano.config.floatX)[:, np.newaxis]

    return X, Y, 20