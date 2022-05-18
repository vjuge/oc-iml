import streamlit as st
import pandas as pd
import numpy as np
import requests


def request_prediction(data):
    headers = {"Content-Type": "application/json"}

    data_json = {'content': data}
    response = requests.request( method='POST', headers=headers, url="https://ociml-module5.herokuapp.com/tags", json=data_json)

    if response.status_code != 200:
        raise Exception(
            "Request failed with status {}, {}".format(response.status_code, response.text))

    return response.json()

st.title('StackOverflow')
st.header('questions tagging utility')

txt = st.text_area('Text to analyze', 
'''I 'm trying to build a simple recommendations system for my college project.
In the project we are "rebuilding" YouTube - building our version of it which should act about the same.
Everything works good, but the only thing we couldn't build is the Side Bar with the Recommended Videos.
I researched about Recommendations System, and I know about Collaborative Based Filtering and Content-Based Filtering.
However I could not find a guide about implementation of such a system, WITHOUT the use of Machine Learning.
Would be glad to have any help with such a guide.
No matter which progarmming language (but if possible, better to have JS, Python, C/C++).
Thanks a lot!''', 500)
predict_btn = st.button('Checkout Tags')

if predict_btn:
        data = txt
        pred = None
        pred = request_prediction(data)
        print(pred)
        st.write('tags found using unsupervised model : {}'.format(pred['unsupervised']))
        st.write('tags found using supervised model : {}'.format(pred['supervised']))
        


