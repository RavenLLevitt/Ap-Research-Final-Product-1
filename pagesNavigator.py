import streamlit as st
import PlaceWhereYouAddCards
import PlaceWhereYouDoReviews

PAGES = {
    "Do reviews": PlaceWhereYouDoReviews,
    "Addwords": PlaceWhereYouAddCards
}

st.sidebar.title("Navigation")
#fix your english
# add_selectbox = st.sidebar.selectbox("Which Page would you like to visit?",["Do reviews", "Addwords"])

selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()