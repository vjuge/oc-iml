import numpy as np
from scipy import stats
import pycountry
import matplotlib.pyplot as plt

agg_func = ['std', 'skew', 'kurtosis', 'mean', 'median', 'var', 'mad', 'prod', 'sum']


def isMultiMode(df, col):
    m = df[col].mode()
    if m.size == 1:
        return False
    else:
        return True


def getMultiModes(df, cols):
    index = cols
    res = []
    for col in cols:
        res.append(isMultiMode(df, col))
    return res


def dropOutlierIQR(df, col):
    Q1 = df[col].quantile(0.25)
    # print(Q1)
    Q3 = df[col].quantile(0.75)
    # print(Q3)
    IQR = Q3 - Q1
    # print(IQR)
    df[col] = df[col][df[col].between((Q1 - 1.5 * IQR), (Q3 + 1.5 * IQR))]


def dropOutliersIQR(df, cols):
    for col in cols:
        dropOutlierIQR(df, col)


# TODO use stats.zscore instead, ex: z = np.abs(stats.zscore(boston_df))
#  then np.where(z > 3)
def dropOutlierZscore(df, col):
    sigma3P = df[col].mean() + df[col].std() * 3
    sigma3N = df[col].mean() - df[col].std() * 3
    df[col] = df[col][df[col].between(sigma3N, sigma3P)]


def dropOutliersZscore(df, cols):
    for col in cols:
        dropOutlierZscore(df, col)


def stats_desc(df):
    print(df.agg(agg_func))


# by default apply IQR method, which seems to be faster and more efficient than Z-score
def removeOutlier(df, col, zscore=False):
    if (zscore):
        dropOutliersZscore(df, [col])
    else:
        dropOutliersIQR(df, [col])


def removeOutliers(df, cols, zscore=False):
    for col in cols:
        removeOutlier(df, col, zscore)


def extractCountry(s):
    s = str(s).upper()
    if (s.find(':') != -1):
        return s[str(s).find(':') + 1:]
    else:
        return s


def transformCountryCode(s):
    try:
        return pycountry.countries.get(name=s).alpha_2
    except BaseException as err:
        # print(f"corresponding country code for {s} not found")
        return s[:2]


def cleanCategory(s):
    s1 = extractCountry(s)
    s2 = transformCountryCode(s1)
    return s2


# test
# print(cleanCategory('en:France'))
# print(cleanCategory('en'))
# print(cleanCategory('en:United States'))
# print(cleanCategory("france"))
# print(cleanCategory("United States"))
# print(cleanCategory("magyarország"))

# plots boxplots for each column
def plotBoxes(df, cols):
    size = cols.size
    plt.figure(figsize=(20, size * 4))
    plt.title(f'analysis of {cols}')
    for i, col in enumerate(cols):
        plt.subplot(size, 1, i + 1)
        df[col].plot(kind='box', vert=False)
    plt.show


# plots histogram for each columns
def plotDist(df, cols):
    size = cols.size
    plt.figure(figsize=(20, size * 4))
    print('distribution of values')
    for i, col in enumerate(cols):
        # sns.displot(df, x=col, bins=200)
        plt.subplot(size, 1, i + 1)
        df[col].plot(kind='hist', bins=200, title=f'{col}')
    plt.show


def getStatisticsNutriscore(data, col, bins=20):
    print("-" * 20)
    print(col)
    print(data.shape)
    print(data['nutriscore_score'].agg(agg_func).T)
    data["nutriscore_score"].hist(bins=bins)
    plt.show()
    data.boxplot(column="nutriscore_score", vert=False)
    plt.show()
