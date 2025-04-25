# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title("📊 Your Music Dashboard")

# # Check if user is logged in
# if "logged_in" not in st.session_state or not st.session_state.logged_in:
#     st.warning("Please log in first to view your dashboard")
#     st.page_link("pages/home.py", label="Go to Login", icon="🏠")
# else:
#     # Mock data for demonstration
#     st.subheader("Your Top Artists")
#     artists_data = pd.DataFrame({
#         'Artist': ['Artist 1', 'Artist 2', 'Artist 3', 'Artist 4', 'Artist 5'],
#         'Plays': [423, 389, 312, 287, 241]
#     })
#     st.bar_chart(artists_data.set_index('Artist'))
    
#     st.subheader("Your Top Tracks")
#     tracks_data = pd.DataFrame({
#         'Track': ['Track 1', 'Track 2', 'Track 3', 'Track 4', 'Track 5'],
#         'Plays': [156, 132, 121, 98, 87]
#     })
#     st.bar_chart(tracks_data.set_index('Track'))
    
#     st.subheader("Listening Activity")
#     chart_data = pd.DataFrame(
#         np.random.randn(30, 1),
#         columns=['listening_hours']
#     )
#     st.line_chart(chart_data)