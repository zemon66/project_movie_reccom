Movie Recommender App

This is a simple movie recommendation web application built using Streamlit, a popular Python library for creating interactive web apps with minimal code. The app provides movie recommendations based on user-selected movies, using a content-based recommendation system.

Features:

Movie Selection: Users can search for a movie from a dataset of movies.

Recommendation: After selecting a movie, the app generates a list of recommended movies based on similarity scores calculated using content-based filtering.

Interactive User Interface: The application has an intuitive and user-friendly interface, making it easy for users to discover new movies.

How to Use:
Select a movie from the dropdown list.
Click the "Recommend" button to view a list of recommended movies similar to your selection.
Data Sources:

The movie dataset is loaded from a movies.pkl file.
Movie similarity scores are calculated and loaded from a similarity.pkl file.
Getting Started:

Clone this repository to your local machine using Git.
Install the required Python packages by running pip install -r requirements.txt.
Run the app using streamlit run movie_app.py.
Contributions and Issues:
Contributions and suggestions for improvements are welcome! If you encounter any issues or have ideas for enhancements, please open an issue or submit a pull request.
