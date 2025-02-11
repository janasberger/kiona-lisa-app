import streamlit as st


def blurting_method():
    st.title("Blurting Method")

    tab_titles = ["Blurting", "Method"]
    tab1, tab2 = st.tabs(tab_titles)

    with tab1:
        st.markdown("Blurting Method")

    with tab2:
        col1, col2, col3, col4 = st.columns((1, 3, 4, 1))

        with col2:
            st.image("../pictures/blurting.png")

        with col3:
            st.markdown("text")
