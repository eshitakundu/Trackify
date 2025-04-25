# import streamlit as st

# st.title("Welcome to Trackify")
# st.write("Login via Spotify to start your musical journey")

# # Mock login form
# with st.container():
#     st.subheader("Login with Spotify")
#     if st.button("Connect with Spotify", type="primary"):
#         st.session_state.logged_in = True
#         st.success("Login successful! (This is a demo)")
#         # In a real app, you would redirect to Spotify OAuth
        
# st.markdown("## About Trackify")
# st.write("Trackify analyzes your Spotify listening habits and provides insights about your music taste.")

# # App features showcase
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.markdown("### 📊 Analytics")
#     st.write("View your top artists and tracks")
# with col2:
#     st.markdown("### 🤖 Bot")
#     st.write("Get your music taste judged")
# with col3:
#     st.markdown("### 🌈 Moodify")
#     st.write("Share and receive music recommendations")