import streamlit as st
import pandas as pd

st.title("emoji")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


# Read the data
df = pd.read_csv('confess_data.csv')

# Metrics
total, confession, poll = st.columns(3)
total.metric('Total Records', len(df))
confession.metric('Total Confessions', len(df[df['type']=='confession']))
poll.metric('Total Polls', len(df[df['type']=='poll']))
