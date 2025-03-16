import streamlit as st

# Set page title and icon
st.set_page_config(page_title="My Portfolio", page_icon="🌟")

# Add a title
st.title("My Portfolio")

# Add a header
st.header("About Me")
st.write("""
Hi I am Lebogang 🌟
Data Scientist | Aspiring AI and ML engineer. 
I am a passionate data and detail-oriented Mathematics and Statistics graduate with an Honours degree in Statistics. My academic foundation, combined with my technical expertise in data science, equips me to transform complex data into actionable insights that drive decision-making and innovation.

I possess strong technical skills in SQL, Python, Power BI, and Machine Learning, which I have applied to solve real-world problems and deliver data-driven solutions. My experience spans data analysis, predictive modeling, and visualization, enabling me to communicate insights effectively to both technical and non-technical stakeholders.

Beyond technical expertise, I bring strong interpersonal skills to the table. I have a proven track record in team leadership, project management, and communication, which allow me to collaborate effectively with cross-functional teams and lead projects to successful completion. I thrive in dynamic environments where I can leverage both my analytical mindset and my ability to connect with people.

I am eager to continue growing in the field of data science and statistics, contributing to impactful projects, and making a meaningful difference through data.

""")

# Add an image
st.image("C:\Users\lebog\Documents\Data Science portfolio\Data-Science-Portfolio\my image.jpg", caption="That's me!", width=200)

# Add a section for skills
st.header("Skills and expertise")
st.write("""
- Python 
- PowerBI
- SQL 
- R 
- Mathematics and Statistics 
- Financial Engineering 
- Data Analysis
- Machine Learning
- Web Development
- Regression
- Natural Learning Process (NLP) and classification 
- Sci-learn, pandas and numpy
- Team Leadership and Project Management
- Presentation skills and communication

""")

# Add a section for projects
st.header("Projects")
st.write("""
### Project 1: Credit Risk Modeling 
- **Description**: The project is based on building a Credit Risk Model to predict the likelihood of a borrower defaulting on a loan.
- **Tech Stack**: -  Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
                  - Machine Learning (Logistic Regression, Decision Trees, Random Forest)
- **Link**: https://github.com/LeboSwaratlhe/Credit-risk-modeling-.git

### Project 2: Analysis News Article 
- **Description**: Built a machine learning-based news classification system to categorize articles for a news outlet.
- **Tech Stack**: - Natural Language Processing (NLP) and classification algorithms (SVM, Naive Bayes, etc)
                  - Python (NLTK, scikit-learn).
                  - Machine learning (Tensorflow, neural networks, MLFlow) 
- **Link**: https://github.com/LeboSwaratlhe/Group_5_Classification_Project.git


### Project 3: Predicting CO2 Emissions from the Agri-food Sector
- **Description**: Built predictive models to estimate CO₂ emissions from agricultural activities and pinpoint major emission sources.
- **Tech Stack**: - Regression analysis, 
                  - feature engineering
                  - Python (scikit-learn, pandas).
- **Link**: https://github.com/LeboSwaratlhe/RegressionExplorers24Team6.git

### Project 4: Anime Recommender System 
- **Description**: built a collaborative and content-based recommender system for a collection of anime titles, capable of accurately predicting how a user will rate an anime title that they have not viewed, based on their historical preferences
- **Tech Stack**:- Collaborative filtering and content-based filtering (recommender system) 
                 - Python (scikit-learn, pandas, Streamlit)
                 
- **Link**: https://github.com/LeboSwaratlhe/Anime-Recommender-System-Project-2025.git

""")


# Add a section for contact information
st.header("Contact Me")
st.write("""
Feel free to reach out to me!
- **Email**: lebogangswaratlhe@gmail.com
- **LinkedIn**: Lebogang Swaratlhe
- **GitHub**: Lebo Swaratlhe 
""")


