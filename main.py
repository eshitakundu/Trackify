import streamlit as st

st.set_page_config(page_title="Trackify Theme Test", page_icon="🎵", layout="centered")

st.title("🎶 Trackify Theme Test")

st.header("This is a Heading (Gotham-Bold)")
st.write("This is regular body text (Gotham-Book).")

st.markdown(
    """
    <h3 style='color:#1DB954;'>This should be Spotify Green 💚</h3>
    <p style='font-family:Gotham-Book;'>If this text looks smooth and nice, your Gotham-Book font is working!</p>
    """,
    unsafe_allow_html=True
)

if st.button("Check Button Style"):
    st.success("✅ Button styling and theme colors working!")

st.link_button("Spotify Link Test", "https://open.spotify.com/")
