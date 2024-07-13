import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "http://localhost:5000"  # The URL of your Flask API

def home_page():
    st.title("🌟 Sentiment Analysis System")
    st.write("Welcome to our Sentiment Analysis System! This application allows you to:")
    st.markdown("- 🔮 Predict the sentiment of a given comment (positive or negative)")
    st.markdown("- ➕ Add a new comment to the database")
    st.markdown("- 📢 View all comments in the database along with their sentiment distribution")

    st.write("To get started, please select an option from the navigation sidebar.")


def predict_sentiment_page():
    st.title("🔮 Predict Sentiment")

    comment_text = st.text_area("Enter a comment for sentiment analysis:")

    if st.button("Predict 🔍", key="predict_sentiment"):
        if comment_text:
            response = requests.post(f"{API_URL}/predict", json={"text": comment_text})

            if response.status_code == 200:
                result = response.json()
                predicted_label = result['prediction_label']

                # Display the predicted label in a larger font and colored
                st.markdown(
                    f"""
                    <div style="text-align: center; margin-top: 20px;">
                        <span style="font-size: 24px; font-weight: bold; color: {'green' if predicted_label == 'positive' else 'red'};">
                            {predicted_label.upper()} 💬
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.error(f"Error: {response.status_code} ❌", icon="🚨")
        else:
            st.warning("Please enter a comment. 📝", icon="⚠️")

def add_comment_page():
    st.header("➕ Add Comment to Database")
    comment_text = st.text_area("Enter a comment to add to the database:", key="add_comment_text")
    commenter_name = st.text_input("Enter your name:", key="commenter_name")
    if st.button("Add Comment 📨", key="add_comment"):
        if comment_text and commenter_name:
            response = requests.post(f"{API_URL}/add_comment", json={"comment_text": comment_text, "commenter_name": commenter_name})
            if response.status_code == 201:
                st.success("Comment added successfully. 🎉")
            else:
                st.error(f"Error: {response.status_code} ❌")
        else:
            st.warning("Please enter both a comment and your name. 📝")

def view_comments_page():
    st.title("📢 View Comments from Database")

    if st.button("Retrieve Comments 📥", key="retrieve_comments"):
        response = requests.get(f"{API_URL}/comments")

        if response.status_code == 200:
            comments = response.json()
            sentiment_counts = {'positive': 0, 'negative': 0}
            comment_data = []

            for comment in comments:
                comment_data.append(comment)
                if comment['prediction'] == 'positive':
                    sentiment_counts['positive'] += 1
                elif comment['prediction'] == 'negative':
                    sentiment_counts['negative'] += 1

            # Plot sentiment distribution
            df = pd.DataFrame.from_dict(sentiment_counts, orient='index', columns=['count'])
            fig = px.pie(df, values='count', names=df.index, title='🚧 Sentiment Distribution 🚧', hole=0.3)
            fig.update_traces(marker=dict(colors=['#4CAF50', '#F44336']))
            st.plotly_chart(fig, use_container_width=True)

            # Show comments
            st.subheader("💬 Comments")
            for comment in comment_data:
                if comment['prediction'] == 'positive':
                    color = 'green'
                    emoji = '👍'
                elif comment['prediction'] == 'negative':
                    color = 'red'
                    emoji = '👎'
                else:
                    color = 'lightgrey'
                    emoji = '🤷‍♂️'

                with st.container():
                    st.markdown(f"""
                        <div style="background-color: {color}; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
                            <div style="display: flex; align-items: center; justify-content: space-between;">
                                <div>
                                    <span style="font-weight: bold;">Commenter Name:</span> {comment['commenter_name']} {emoji}
                                </div>
                                <div>
                                    <span style="font-weight: bold;">Sentiment:</span> {comment['prediction'].upper()}
                                </div>
                            </div>
                            <div style="margin-top: 10px;">
                                <span style="font-weight: bold;">Comment:</span> {comment['comment_text']}
                            </div>
                            <div style="margin-top: 10px;">
                                <span style="font-weight: bold;">Date:</span> {comment['creation_time']}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

        else:
            st.error(f"Error: {response.status_code} ❌")

# Sidebar for navigation
st.sidebar.title("🗺️ Navigation")

# Navigation buttons with unique keys
if st.sidebar.button("Home 🏠", key="nav_home"):
    st.session_state.page = "Home"
if st.sidebar.button("Predict Sentiment 🔮", key="nav_predict_sentiment"):
    st.session_state.page = "Predict Sentiment"
if st.sidebar.button("Add Comment ➕", key="nav_add_comment"):
    st.session_state.page = "Add Comment"
if st.sidebar.button("View Comments 📢", key="nav_view_comments"):
    st.session_state.page = "View Comments"

# Initialize session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Render the selected page
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Predict Sentiment":
    predict_sentiment_page()
elif st.session_state.page == "Add Comment":
    add_comment_page()
elif st.session_state.page == "View Comments":
    view_comments_page()