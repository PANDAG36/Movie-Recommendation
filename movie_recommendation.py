import pandas as pd
import streamlit as st

df = pd.read_csv("cleaned_imdb_movies.csv")



st.header("MOVIES RECOMMENTIONS", text_alignment="center")


Genre = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']


def movie_recom(df, intrests):
    the_index = [ ]
    for i, genre in enumerate(df):
        if all(intrest in genre for intrest in intrests):
            the_index.append(i)
        # else:
        #     return None
            
    return the_index

def movie_recom_list(the_index):
    lis = []
    for i in the_index:
        movie_rec = df.iloc[i]
        lis.append(movie_rec[["orig_title", "score", "overview", "orig_lang", "date_x"]])
    return lis

            

st.subheader("Enter Your Choice: ", text_alignment="left")

genre_selected = st.multiselect(
    "What Genre are you lokking For?",
    Genre,
    default = Genre[1],
    max_selections=5
)

# st.subheader(genre_selected)

all_movies = df[["orig_title", "score", "overview", "orig_lang", "date_x"]]

st.subheader("MOVIES YOU MIGHT LIKE:")
st.divider()

venom = movie_recom(df["genre"], genre_selected)

# if len(venom) > 1:
#     spiderman = movie_recom_list(venom)
#     st.dataframe(spiderman, hide_index=True, height=1000, width=700)
# else:
#     st.write("No Match Found")

spiderman = movie_recom_list(venom)

# for i in spiderman:
#     st.header(i["orig_title"],text_alignment="center")
#     if st.button("Click for Details"):
#         st.subheader(i["overview"])
#         st.subheader("MOVIE SCORE")
#         st.write(i["score"])
#         st.subheader("Language:", i["orig_lang"], " ", "Release date: ", i["date_x"])
#         st.divider()
if len(venom) > 1:
    for idx, i in enumerate(spiderman):
        st.header(i["orig_title"])

        if st.button("More Details", key=idx):  # unique key
            st.subheader(i["overview"])
            st.subheader(f"MOVIE SCORE: {i["score"]}.")
            st.subheader(f"Language:{ i["orig_lang"]} | Release date: {i["date_x"]}.")
            st.divider()
else:
    st.write("No Match Found")
    st.divider()