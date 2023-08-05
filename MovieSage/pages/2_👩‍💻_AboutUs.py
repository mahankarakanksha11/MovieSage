import streamlit as st
from PIL import Image

def about_us_page():
    st.title("About Us")
    st.markdown("<h3 style='color: #329ea8;'>Welcome to our Movie Recommender App!</h3>", unsafe_allow_html=True)
    st.write("Our mission is to help you discover the best movies based on your preferences.")
    st.write("We use state-of-the-art recommendation algorithms to provide personalized movie recommendations for you.")
    st.write("Our app considers various factors like your movie ratings, genres, and movie preferences to offer tailored suggestions.")
    st.write("We are continuously improving our recommendation engine to ensure accurate and enjoyable movie suggestions.")

    st.header("Meet the Team")
    image = Image.open('./meta/logo.jpeg')
    image = image.resize((290, 220), )
    st.image(image, caption='Team')
    st.write("Our team is made up of movie enthusiasts and machine learning experts.")
    st.write("We are passionate about movies and technology, and that's why we built this app.")
    st.write("We are dedicated to delivering the best movie recommendations and making your movie-watching experience more delightful.")

    st.write("Thank you for using our <span style='font-family: cursive;'>Movie Recommender App</span>. Enjoy your movie journey!", unsafe_allow_html=True)



def main():
    about_us_page()

if __name__ == "__main__":
    main()
