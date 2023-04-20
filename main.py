import streamlit as st
from datetime import datetime
from model import result, csv_result
# from model import initial_train
import csv
import pandas as pd
from io import StringIO

st.title('Spam Mail Detection Machine Learning Model')

# train = st.button('Train Model')
#
# if train:
#     initial_train()

# enter_mail = st.button('Enter mail and check spam')
# enter_csv = st.button('Enter csv file')


mail = st.text_input(label="Enter mail content here:", value="", max_chars=None, key=None, type="default", label_visibility="visible")
uploaded_file = st.file_uploader(label="Enter csv file here:", type=".csv" )

if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # # To read file as string:
    # string_data = stringio.read()

    # print(string_data)


    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    # df.columns
    # df.drop({'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'}, axis=1, inplace=True)
    # print(df['v2'])
    mails = df['v2']
    # print(mails)
    submit = st.button('Show Result')

    if submit:
        st.success('Executed Successfully')
        st.balloons()
        if mails.size != 0 or uploaded_file:
            check = csv_result(mails)
            st.write(check)

else:
    submit = st.button('Show Result')

    if submit:
        st.success('Executed Successfully')
        st.balloons()
        if mail:
            check = result(mail)
            st.title(check)
