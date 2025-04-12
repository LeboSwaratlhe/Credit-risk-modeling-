import streamlit as st

# Set page title and icon
st.set_page_config(page_title="My Portfolio", page_icon="🌟")

# Define the navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "About Me", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.write("""
    Hi, I am Lebogang 🌟  
    **Data Scientist | Aspiring AI and ML Engineer**  

    Welcome to my portfolio! Use the navigation menu on the left to explore more about me, my projects, and how to get in touch.
    """)

    # Add the GIF
    try:
        st.image(r"data science pic.webp", caption="Welcome to my world!", width=400)
    except FileNotFoundError:
        st.error("Image not found! Please check the file path.")

    # Add a section for Technical Skills and Expertise
    st.header("Technical Skills and Expertise")
    st.write("""
    Here are some of the key areas I specialize in:
    """)

    # Single-column layout
    st.write("""
    - 🤖 **Machine Learning**: Skilled in developing predictive models and classification systems.  
    - 📊 **Data Analysis**: Expertise in regression analysis, feature engineering, and statistical modeling.  
    - 📝 **Natural Language Processing (NLP)**: Proficient in text processing and classification tasks.  
    - 🐍 **Technical Proficiency**: Scikit-learn, Pandas, NLTK, Computer Vision.  
    - 🧑‍💻 **Programming Languages**: Python, R, SQL.  
    - 🧠 **Deep Learning**: Proficient in designing and training neural networks using TensorFlow and Keras.   
    - 🛠️ **Collaboration and Tools**: Proficient in Git and Jupyter Notebooks for collaborative development.  
    - ⚙️ **Web Development**: Streamlit.  
    - 🌟 **Soft Skills**: Team Leadership, Project Management, Communication, Adaptability, Storytelling.  
    """)

    st.write("""
    Feel free to explore my projects and reach out if you'd like to collaborate or connect!
    """)

# About Me Page
elif page == "About Me":
    st.title("About Me")
    st.write("""
    Hi, I am Lebogang 🌟  
    **Data Scientist | Aspiring AI and ML Engineer**  

    I am a passionate and detail-oriented Mathematics and Statistics graduate with an Honours degree in Statistics. My academic foundation, combined with my technical expertise in data science, equips me to transform complex data into actionable insights that drive decision-making and innovation.
    I am eager to continue growing in the field of data science and statistics, contributing to impactful projects, and making a meaningful difference through data.
    """)

    # Display logos
    st.header("Key Skills and Expertise")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg", width=60, caption="Jupyter Notebook")
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg", width=60, caption="Power BI")
    with col3:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/r/r-original.svg", width=60, caption="R")
    with col4:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg", width=60, caption="MySQL")
    with col5:
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg", width=60, caption="Scikit-Learn")
    with col6:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg", width=60, caption="Pandas")
    with col7:
        st.image("https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg", width=60, caption="NumPy")

    # Add an image with error handling
    try:
        st.image(r"my image.jpg", caption="That's me!", width=200)
    except FileNotFoundError:
        st.error("Image not found! Please check the file path.")

    # Add Education Section
    st.header("Education")

    # University of Pretoria
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"up logo.png", width=200)
    with col2:
        st.write("""
        - **Bachelor of Science (BSc) in Mathematical Statistics**  
          *University of Pretoria | Graduated in 2023*  
          - Final year coursework: Multivariate Analysis, Stochastic Processes, Statistics, The Science of Data, Actuarial Statistics, and Financial Engineering.  
        """)

    # University of South Africa (UNISA)
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"unisa logo.png", width=100)
    with col2:
        st.write("""
        - **Bachelor of Science (BSc) Honours Degree in Statistics**  
          *University of South Africa | Current*  
          - Focused on Research Project in Statistics, Linear Models, Regression, Time Series, Inference, Generalized Linear Models, Multivariate Statistical Techniques, Nonparametric Regression.  
        """)

    # Explore AI Academy
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"explore ai.png", width=200)
    with col2:
        st.write("""
        - **Data Science Learnership**  
          *Explore AI Academy, Sand Technologies | Current*  
          - Focused on Microsoft Excel, Preparing Data, Data Visualization on Power BI, Exploratory Data Analysis, Python, Regression, Natural Language Processing (NLP), Classification, and Unsupervised Learning.  
        """)

    # Certifications
    st.header("Certifications")
    st.write(""" 
      - **Standard Bank Corporate Investment Banking Job Simulation** - [Forage, January 2023](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/Standard%20Bank%20/gPeqXLCuhf9mvqLN2_Standard%20Bank_dFzuf2nfLfaPuw4DQ_1672699277443_completion_certificate.pdf)  
         - Completed a job simulation assessing a hypothetical client, Sea Harvest, who required a lending solution as a Debt Solutions Analyst. 
         - Prepared a 1-page company profile presented to the credit committee. 
         - Completed research using the annual report and third-party sources to develop a balanced view of our client’s business and future performance. 
         - Created a financial model in Excel forecasting the client’s expected future performance. 
         - Presented to my manager about market current affairs and the implications of them. 
      - **JPMorgan Chase & Co. Quantitative Research Job Simulation** - [Forage, January 2024](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/J.P.%20Morgan/bWqaecPDbYAwSDqJy_JPMorgan%20Chase%20&%20Co._dFzuf2nfLfaPuw4DQ_1705616526417_completion_certificate.pdf)  
         - Completed a simulation focused on quantitative research methods. 
         - Analysed a book of loans to estimate a customer’s probability of defaults. 
         - Used dynamic programming to convert FICO scores into categorical data to predict defaults.
    """)

# Projects Page
elif page == "Projects":
    st.title("Projects")
    st.write("Here are some of the projects I've worked on:")

    # Project 1: Credit Risk Modeling
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"credit risk pic.webp", width=350)  # Replace with your project image
    with col2:
        st.write("""
        ### **Credit Risk Modeling**  
        - **Role**: Data Scientist and Project Manager  
        - **Description**: Built a Credit Risk Model to predict the likelihood of a borrower defaulting on a loan.  
        - **Tech Stack**: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn), Machine Learning (Logistic Regression, Decision Trees, Random Forest)  
        - **Link**: [GitHub](https://github.com/LeboSwaratlhe/Credit-risk-modeling-.git)  
        """)

    # Project 2: News Article Classification
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"news article pic.png", width=350)  # Replace with your project image
    with col2:
        st.write("""
        ### **News Article Classification**  
        - **Role**: Tead Team and Data Scientist   
        - **Description**: Built a machine learning-based news classification system to categorize articles for a news outlet.  
        - **Tech Stack**: Natural Language Processing (NLP), Classification Algorithms (SVM, Naive Bayes), Python (NLTK, Scikit-learn), TensorFlow, MLFlow  
        - **Link**: [GitHub](https://github.com/LeboSwaratlhe/Group_5_Classification_Project.git)  
        """)

    # Project 3: Predicting CO2 Emissions
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"co2 pic.png", width=350)  # Replace with your project image
    with col2:
        st.write("""
        ### **Predicting CO2 Emissions from the Agri-food Sector**  
        - **Role**: Data Analyst  
        - **Description**: Built predictive models to estimate CO₂ emissions from agricultural activities and pinpoint major emission sources.  
        - **Tech Stack**: Regression Analysis, Feature Engineering, Python (Scikit-learn, Pandas)  
        - **Link**: [GitHub](https://github.com/LeboSwaratlhe/RegressionExplorers24Team6.git)  
        """)

    # Project 4: Anime Recommender System
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"anime.png", width=350)  # Replace with your project image
    with col2:
        st.write("""
        ### **Anime Recommender System**  
        - **Role**: Team Lead and Machine Learning Engineer  
        - **Description**: Built a collaborative and content-based recommender system for anime titles, predicting user ratings based on historical preferences.  
        - **Tech Stack**: Collaborative Filtering, Content-Based Filtering, Python (Scikit-learn, Pandas, Streamlit)  
        - **Link**: [GitHub](https://github.com/LeboSwaratlhe/Anime-Recommender-System-Project-2025.git)  
        - **Deployed app**: [Streamlit](https://group2-2407ftds.streamlit.app/)
        """)
        
# Project 5: Bank Customer Churn Predictive 
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(r"bank customer.png", width=350)  # Replace with your project image
    with col2:
        st.write("""
        ### **Bank Customer Churn Predictive project**  
        - **Role**: Data Scientist 
        - **Description**: This project develops a predictive model to identify bank customers at risk of churning (discontinuing services)  
        - **Tech Stack**: 
        - **Link**: [GitHub](https://github.com/LeboSwaratlhe/Bank-Customer-Churn-Prediction.git)  
        - **Deployed app**: [Streamlit](https://leboswaratlhe-bank-customer--bankcustomerchurnprediction-sw8vcj.streamlit.app/)
        """)        

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("""
    I’d be delighted to hear from you! Whether you have inquiries, prospects, or simply want to connect, don’t  hesitate to get in touch using the contact information below. I’m always eager to explore exciting projects, partnerships, or any other possibilities.
    
    Feel free to reach out to me!  
    - **Email**: [lebogangswaratlhe@gmail.com](mailto:lebogangswaratlhe@gmail.com) 
    - **LinkedIn**: [Lebogang Swaratlhe](https://www.linkedin.com/in/lebogang-swaratlhe-b67415197/)  
    - **GitHub**: [Lebo Swaratlhe](https://github.com/LeboSwaratlhe)  
    """)