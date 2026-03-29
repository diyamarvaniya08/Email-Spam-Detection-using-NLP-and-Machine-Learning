# Email-Spam-Detection-using-NLP-and-Machine-Learning
A machine learning project that classifies messages as spam or not spam using Natural Language Processing techniques and a Naive Bayes model, with a Streamlit-based web app for real-time predictions.

# Overview
This project focuses on building a machine learning model to classify emails/messages as Spam or Ham(Not Spam) using Natural Language Processing (NLP) techniques.
It also includes a simple web application built with Streamlit to interactively test predictions.

Spam detection is widely used in real-world applications like Gmail and Outlook to filter unwanted or harmful emails automatically.

# Objectives
 - Classify messages into Spam and Not Spam
 - Perform text preprocessing and cleaning
 - Convert text data into numerical features
 - Train a machine learning model for text classification
 - Evaluate model performance
 - Deploy the model using a simple web interface
   
# Dataset
 - Dataset used: spam.csv
 - contains:
     - Category → Spam / Ham
     - Message → Text data

# Data Cleaning Steps
 - Removed duplicate records
 - Checked and handled missing values
 - Converted labels:
     - ham → Not Spam
     - spam → Spam

# Tech Stack
 - Python
 - Pandas
 - Scikit-learn
 - CountVectorizer (NLP)
 - Streamlit

# Workflow
  ## 1. Data Preprocessing
    - Removed duplicates
    - Handled null values
    - Renamed target labels
    
  ## 2. Train-Test Split
    - Split data into training and testing sets (80:20)
   
  ## 3. Feature Extraction
    - Used CountVectorizer to convert text into numerical features
    - Removed English stopwords
   
  ## 4. Model Building
    - Applied Multinomial Naive Bayes algorithm

   ## Why this model?
    - Works efficiently for text classification
    - Handles high-dimensional data well
       
  ## 5. Model Evaluation
    - Evaluated using accuracy score
    - Model Accuracy: 98.44%
  
  ## 6. Prediction
    - Example:
    - Input: "Congratulations, you won a lottery"
    - Output: Spam

# Web Application
    - A simple web app is created using Streamlit:
    - Features:
      - User can enter a message
      - Model predicts whether it is Spam or Not Spam
 
   ## Run the app:
   # streamlit run spamDetection.py
  
# Key Insights
 - Certain keywords strongly indicate spam (e.g., “free”, “win”, “Congratulations”)
 - Text preprocessing significantly improves model performance
 - Probabilistic models like Naive Bayes perform well on text data

# Model
 - Used Naive Bayes classifier for spam detection
 - Efficient for text classification problems
 - Performs well on high-dimensional data
