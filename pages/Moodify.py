# import streamlit as st

# st.title("🌈 Moodify - Community Music Sharing")

# # Check if user is logged in
# if "logged_in" not in st.session_state or not st.session_state.logged_in:
#     st.warning("Please log in first to use Moodify")
#     st.page_link("pages/home.py", label="Go to Login", icon="🏠")
# else:
#     tabs = st.tabs(["Submit a Capsule", "Receive Capsules"])
    
#     with tabs[0]:
#         st.subheader("Create a Music Capsule")
#         st.write("Share a song with the community along with a message")
        
#         st.text_input("Song Title", placeholder="Enter song title")
#         st.text_input("Artist", placeholder="Enter artist name")
#         st.text_area("Your Message", placeholder="What does this song mean to you?")
        
#         mood = st.select_slider(
#             "What mood does this song represent?",
#             options=["Melancholy", "Calm", "Neutral", "Upbeat", "Energetic"]
#         )
        
#         st.checkbox("I want to receive capsules from others", value=True)
        
#         if st.button("Submit Capsule", type="primary"):
#             st.success("Your music capsule has been submitted to the community!")
    
#     with tabs[1]:
#         st.subheader("Discover Community Capsules")
#         st.write("Explore music shared by other Trackify users")
        
#         # Mock capsules
#         capsules = [
#             {"song": "Bohemian Rhapsody", "artist": "Queen", "message": "This song always reminds me of road trips with friends.", "mood": "Energetic"},
#             {"song": "Fix You", "artist": "Coldplay", "message": "Got me through some tough times.", "mood": "Melancholy"},
#             {"song": "Good Vibrations", "artist": "Beach Boys", "message": "Pure summer vibes!", "mood": "Upbeat"}
#         ]
        
#         filter_mood = st.multiselect(
#             "Filter by mood",
#             ["Melancholy", "Calm", "Neutral", "Upbeat", "Energetic"]
#         )
        
#         for capsule in capsules:
#             if not filter_mood or capsule["mood"] in filter_mood:
#                 with st.container():
#                     st.markdown(f"### {capsule['song']} by {capsule['artist']}")
#                     st.markdown(f"*Mood: {capsule['mood']}*")
#                     st.markdown(f"{capsule['message']}")
#                     st.button(f"Save {capsule['song']}", key=capsule['song'])
#                     st.divider()