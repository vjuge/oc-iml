import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

print("load model ...")
with open('./utils/vectorizer', 'rb') as v:
    vectorizer = pickle.load(v)


#***** prediction
def predict(doc: str) -> list[str]:  
    tf1_new = TfidfVectorizer(analyzer='word', ngram_range=(1,2), stop_words = "english", lowercase = True,
                            max_features = 5000, vocabulary = vectorizer.vocabulary_)
    T = tf1_new.fit_transform(np.array([doc]))
    T = pd.DataFrame(T.T.todense())
    T[0].sort_values(ascending=False)
    # take the 3 most interesting keywords
    indexes = T[0].sort_values(ascending=False)[:5]
    # print(indexes)
    ret = []
    for i, val in indexes.items():
        # print(i)
        # print(indexes[0].index[i])
        if (val > 0): 
            ret.append(vectorizer.get_feature_names_out()[i])
            # print(vectorizer.get_feature_names_out()[i])
    return ret
    