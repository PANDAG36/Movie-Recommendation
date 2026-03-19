import pandas as pd
import streamlit as st

df = pd.read_csv("cleaned_imdb_movies.csv")

st.header("MOVIE RECOMMENTIONS")

df["genre"].unique

