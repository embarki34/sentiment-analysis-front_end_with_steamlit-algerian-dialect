
# Sentiment Analysis Streamlit App

This Streamlit application provides a user-friendly interface for interacting with a sentiment analysis system. Users can predict sentiments, add comments, and view existing comments from a Flask API.

## Features

- **Predict Sentiment**: Analyze a given comment to determine if it's positive or negative.
- **Add Comment**: Submit a new comment along with the commenter's name to the database.
- **View Comments**: Retrieve and display all comments from the database with sentiment distribution.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Streamlit
- Requests
- Plotly
- Pandas

You can install the necessary packages using pip:

```bash
pip install streamlit requests plotly pandas
```

## Running the Application

1. **Start your Flask API** (make sure it's running on `http://localhost:5000`):

   ```bash
   python your_flask_app.py
   ```

2. **Run the Streamlit app:**

   ```bash
   streamlit run your_streamlit_app.py
   ```

3. Open your browser and navigate to `http://localhost:8501` to view the application.

## Application Structure

The application consists of several main functions corresponding to different pages:

- **Home Page**: Overview of the application's capabilities.
- **Predict Sentiment Page**: Input a comment and receive a sentiment prediction.
- **Add Comment Page**: Submit a comment and name to the database.
- **View Comments Page**: Retrieve and display all comments along with sentiment distribution.

## API Configuration

Make sure the API URL in the code is correctly set to your Flask API:

```python
API_URL = "http://localhost:5000"  # The URL of your Flask API
```

## API Endpoints

The app interacts with the following endpoints:

### 1. Predict Sentiment

**Endpoint:** `/predict`  
**Method:** `POST`  
**Request Body:**
```json
{
    "text": "Your comment here"
}
```
**Response:**
```json
{
    "prediction_label": "positive"
}
```

### 2. Add Comment

**Endpoint:** `/add_comment`  
**Method:** `POST`  
**Request Body:**
```json
{
    "comment_text": "Your comment here",
    "commenter_name": "Your name"
}
```
**Response:**
```json
{
    "message": "Comment added successfully"
}
```

### 3. Get Comments

**Endpoint:** `/comments`  
**Method:** `GET`  
**Response:**
```json
[
    {
        "commenter_name": "Name",
        "comment_text": "Your comment",
        "prediction": "positive",
        "creation_time": "2023-01-01T00:00:00Z"
    },
    ...
]
```

## Visualizations

The application includes a pie chart to visualize the sentiment distribution of the comments retrieved from the database, using Plotly.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Author

Omar
