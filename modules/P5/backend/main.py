from typing import Any, Optional, List
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class Document(BaseModel):
    content: str

class Tags(BaseModel):
    unsupervised: list[str]
    supervised: list[str]

print("loading model ...")
with open('./vectorizer', 'rb') as v:
    vectorizer = pickle.load(v)

with open('./classifier', 'rb') as v:
    clf = pickle.load(v)

with open('./mlb_t', 'rb') as v:
    mlb_t = pickle.load(v)

with open('./cv', 'rb') as v:
    cv = pickle.load(v)



app = FastAPI(
    title="Tag modelization API", openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.post("/tags", response_model=Tags)
async def tags(doc: Document):
    data = {
        'unsupervised' : predict_tf(doc.content),
        'supervised' : predict_clf(doc.content)
    }
    return Tags(**data)

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")


def predict_tf(doc: str) -> list[str]:  
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

def predict_clf(doc: str) -> list[str]:
    pred = [' '.join(pred) for pred in mlb_t.inverse_transform(clf.predict(cv.transform(doc.split())))]
    return list(filter(None, pred))

