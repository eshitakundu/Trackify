# import streamlit as st

# st.title("🤖 Track Judge")

# # Check if user is logged in
# if "logged_in" not in st.session_state or not st.session_state.logged_in:
#     st.warning("Please log in first to use Track Judge")
#     st.page_link("pages/home.py", label="Go to Login", icon="🏠")
# else:
#     st.write("Let our AI judge your music taste!")
    
#     # Mode selection
#     judge_mode = st.radio(
#         "Select judge mode:",
#         ["🔥 Roast Bot (Brutal honesty)", "✨ Sweet Bot (Kind feedback)"]
#     )
    
#     # Track selection (mock)
#     st.subheader("Select a track to judge")
#     track_options = ["Your most played track", "Your recent favorite", "Random from your library", "Custom track"]
#     selected_track = st.selectbox("Track selection", track_options)
    
#     if selected_track == "Custom track":
#         st.text_input("Enter track name")
#         st.text_input("Enter artist name")
    
#     # Judge button
#     if st.button("Judge My Taste!", type="primary"):
#         st.divider()
        
#         if judge_mode == "🔥 Roast Bot (Brutal honesty)":
#             st.markdown("### 🔥 Roast Bot says:")
#             st.markdown("""
#             Oh wow, you actually listen to *that* unironically? 
#             I guess someone has to keep those one-hit wonders employed. 
#             Your taste is as basic as a pumpkin spice latte in October.
#             """)
#         else:
#             st.markdown("### ✨ Sweet Bot says:")
#             st.markdown("""
#             What a thoughtful selection! This track shows your appreciation for 
#             meaningful lyrics and innovative production. Your music taste reflects 
#             your creative and open-minded personality!
#             """)