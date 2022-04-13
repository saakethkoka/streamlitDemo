import streamlit as st
import pandas as pd
from queries import *


if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Count')
if increment:
    st.session_state.count += 1

st.write(st.session_state.count)


df = pd.read_csv("crudeoil.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index(df.Date, inplace=True)



bid_prices = st.button('Bid Price')
ask_prices = st.button('Ask Price')





if bid_prices:
    new_df = df["Bid"]
    st.line_chart(new_df)
if ask_prices:
    new_df = df["Ask"]
    st.line_chart(new_df)


text = st.text_area("Add Comment here")

if text:
    addComment(text)

for i in getComments():
    st.write(i)
