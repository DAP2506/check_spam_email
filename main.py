import streamlit as st
from datetime import datetime
from model import result
# from model import initial_train

st.title('Spam Mail Detection Machine Learning Model')

# train = st.button('Train Model')
#
# if train:
#     initial_train()
mail = st.text_input(label="Enter mail content here:", value="", max_chars=None, key=None, type="default", label_visibility="visible")

submit = st.button('Show Result')

if submit:
    st.success('Executed Successfully')
    st.balloons()
    check = result(mail)
    st.title(check)
